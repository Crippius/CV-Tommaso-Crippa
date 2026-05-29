#!/usr/bin/env python3
"""Assemble resume.tex from a named profile and optionally compile it."""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
PROFILES = ROOT / "profiles"
TEMPLATE = ROOT / "resume_template.tex"
OUTPUT = ROOT / "resume.tex"

PROFILE_FLAGS = {
    "data-engineer": {"de": True,  "hpc": False, "phd": False},
    "hpc":           {"de": False, "hpc": True,  "phd": False},
    "phd":           {"de": False, "hpc": False, "phd": True},
}


def load_yaml(path: Path) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def read_tex(path: Path) -> str:
    return path.read_text()


def build_courses(course_ids: list[str], all_courses: dict) -> str:
    names = []
    for cid in course_ids:
        if cid not in all_courses:
            print(f"Warning: unknown course id '{cid}'", file=sys.stderr)
            continue
        names.append(all_courses[cid])

    if not names:
        return ""

    return "{\\small " + ", ".join(names) + "}\n"


def build_skills_list(skill_ids: list[str], all_skills: dict) -> str:
    names = []
    for sid in skill_ids:
        if sid not in all_skills:
            print(f"Warning: unknown skill id '{sid}'", file=sys.stderr)
            continue
        names.append(all_skills[sid])
    if not names:
        return ""
    return "{\\small " + ", ".join(names) + "}\n"


def build_tex_blocks(ids: list[str], directory: Path, label: str) -> str:
    parts = []
    for item_id in ids:
        path = directory / f"{item_id}.tex"
        if not path.exists():
            print(f"Warning: {label} file not found: {path}", file=sys.stderr)
            continue
        parts.append(read_tex(path))
    return "\n".join(parts)


def assemble(profile_name: str) -> str:
    profile_path = PROFILES / f"{profile_name}.yaml"
    if not profile_path.exists():
        sys.exit(f"Error: profile '{profile_name}' not found at {profile_path}")

    profile = load_yaml(profile_path)
    all_courses = load_yaml(CONTENT / "courses.yaml")
    all_skills = load_yaml(CONTENT / "skills.yaml")

    tagline = profile.get("tagline", "")
    experiences = build_tex_blocks(profile.get("experiences", []), CONTENT / "experiences", "experience")
    projects = build_tex_blocks(profile.get("projects", []), CONTENT / "projects", "project")
    courses = build_courses(profile.get("courses", []), all_courses)

    prog_ids = profile.get("skills", {}).get("tech_stack", [])
    tool_ids = profile.get("skills", {}).get("infrastructure", [])
    skills_prog = build_skills_list(prog_ids, all_skills["tech_stack"])
    skills_tools = build_skills_list(tool_ids, all_skills["infrastructure"])

    flags = PROFILE_FLAGS.get(profile_name, {})
    flag_lines = [
        f"\\newif\\if{name}\\{name}{'true' if flags.get(name, False) else 'false'}"
        for name in ["de", "hpc", "phd"]
    ]
    profile_flags_block = "\n".join(flag_lines)

    summary_raw = profile.get("summary", "")
    summary_block = (
        f"\\begin{{quote}}\n\\small {summary_raw}\n\\end{{quote}}\n"
        if summary_raw else ""
    )

    template = TEMPLATE.read_text()
    result = (
        template
        .replace("%%PROFILE_FLAGS%%", profile_flags_block)
        .replace("%%TAGLINE%%", tagline)
        .replace("%%SUMMARY%%", summary_block)
        .replace("%%EXPERIENCES%%", experiences)
        .replace("%%PROJECTS%%", projects)
        .replace("%%COURSES%%", courses)
        .replace("%%SKILLS_PROGRAMMING%%", skills_prog)
        .replace("%%SKILLS_TOOLS%%", skills_tools)
    )
    return result


def compile_tex() -> Path:
    subprocess.run(
        ["latexmk", "-pdf", "-xelatex", "-interaction=nonstopmode", "-f", "resume.tex"],
        cwd=ROOT,
    )
    pdf = ROOT / "resume.pdf"
    if not pdf.exists():
        sys.exit("LaTeX compilation failed — no resume.pdf produced")
    (ROOT / "creationdate.lua").unlink(missing_ok=True)
    return pdf


def main():
    parser = argparse.ArgumentParser(description="Assemble resume.tex from a profile")
    parser.add_argument("--profile", help="Profile name (filename without .yaml). If omitted, builds all profiles.")
    parser.add_argument("--no-compile", action="store_true", help="Write resume.tex but skip LaTeX compilation")
    args = parser.parse_args()

    profiles = (
        [args.profile] if args.profile
        else sorted(p.stem for p in PROFILES.glob("*.yaml"))
    )
    multi = len(profiles) > 1

    if multi and not args.no_compile:
        builds_dir = ROOT / "builds"
        builds_dir.mkdir(exist_ok=True)

    for profile_name in profiles:
        tex = assemble(profile_name)
        OUTPUT.write_text(tex)
        print(f"Written {OUTPUT} [{profile_name}]")

        if not args.no_compile:
            # -f forces completion despite the pre-existing pdfx CreationDate warning
            pdf = compile_tex()
            if multi:
                dest = builds_dir / f"resume_{profile_name}.pdf"
                shutil.copy2(pdf, dest)
                print(f"Compiled {dest}")
            else:
                print(f"Compiled {pdf}")


if __name__ == "__main__":
    main()
