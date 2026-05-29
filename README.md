# CV – Tommaso Crippa

Profile-driven CV system. All content lives in a bank; a YAML profile selects what goes in. Run one command to get a tailored `resume.tex` (and optionally compile it).

## Structure

```
content/
  projects/       # one .tex file per project (e.g. alzheimer.tex)
  experiences/    # one .tex file per experience (e.g. megware.tex)
  courses.yaml    # id → display name for all courses
  skills.yaml     # id → {display, level} for all skills
profiles/
  hpc.yaml             # HPC engineering archetype
  data-engineer.yaml   # Data engineering archetype
  phd-ml.yaml          # PhD / academic archetype
build.py               # assembler script
resume_template.tex    # static scaffold (do not edit resume.tex directly)
resume.tex             # generated output — edit via profiles, not by hand
```

## Usage

```bash
# Build a profile (assembles resume.tex and compiles to resume.pdf)
python3 build.py --profile hpc

# Just write resume.tex without compiling (e.g. for Overleaf)
python3 build.py --profile hpc --no-compile
```

## Switching profiles

Each profile YAML specifies the tagline, and the IDs of experiences, projects, courses, and skills to include — in display order:

```yaml
tagline: "High Performance Computing Engineering Student"

experiences: [megware, eurohpc, gdg]
projects: [alzheimer, graph-coloring, whatsapp]
courses: [parallel-computing, advanced-arch, ann-dl]
skills:
  programming: [python, c, cpp]
  tools: [git, slurm, dvc]
```

## Per-application customization

Copy an archetype and tweak it for the specific job:

```bash
cp profiles/data-engineer.yaml profiles/de-kafka-company-x.yaml
# edit: adjust tagline, swap a project, add docker to tools
python3 build.py --profile de-kafka-company-x
```

## Adding new content

- **New project**: create `content/projects/<id>.tex` with the full `\cvproject{...}` block.
- **New experience**: create `content/experiences/<id>.tex` with the full `\cvexperience{...}` block.
- **New course**: add `id: "Display Name"` to `content/courses.yaml`.
- **New skill**: add an entry under `programming` or `tools` in `content/skills.yaml`.

Then reference the new ID in any profile.

## Overleaf workflow

1. Run `python3 build.py --profile <name> --no-compile` locally.
2. Commit and push `resume.tex`.
3. Overleaf syncs via git and recompiles.
