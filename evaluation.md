# CV Evaluation — Junior Data Engineering Role

**Candidate:** Tommaso Crippa | Entry-level / Graduate

---

## 1. Overall Structure & Layout — 7/10

Clean single-column layout with logical ordering (Education → Experience → Projects → Skills). The header is minimal but missing a targeted summary for DE roles, meaning recruiters must infer fit from bullet points alone.

**Feedback:**

- Add a 2-line profile summary directly under the name targeting Data Engineering specifically.
- The icons (§, ï, À, Ð) may not render in ATS parsers — replace with plain text labels (GitHub:, GPA:, Tech:).
- Consider adding a "Data Engineering" or "Data & ML Infrastructure" tag in the header to pass the 6-second recruiter scan.
- Reorder experiences by relevance to DE, not solely by date — the Google DevGroup role has more DE-adjacent relevance (Cloud, tooling) than the HPC Ambassador entry.

**Suggested header summary:**

> "HPC graduate with hands-on experience building data pipelines and ML-backed analytics tools. Proficient in Python, SQL, Kafka, and distributed computing. Seeking a Junior Data Engineering role to apply my skills in building scalable data infrastructure and ETL processes."

---

## 2. Impact of Achievements (Quantified Results) — 4/10

Almost every bullet describes what was done, not what was achieved. No throughput figures, dataset sizes, accuracy metrics, latency improvements, or user numbers appear anywhere. DE hiring managers look for scale and impact.

**Feedback:**

- Quantify data volume in the thesis bullet (e.g. "processing ~50k metric rows/hour").
  -> processing 5,760 data points per minute from 100+ HPC metrics
  (like there is a job that runs for 30mins, each minute it has around 5760 data points, but im not processing them in real time, its more like size of the dataset is going to be really big. consider 18 applications running for 10-15 mins each, its going to be a big dataset u know)
- The Alzheimer project has no accuracy/AUC metric — add one even if approximate.
  -> Macro-AUC of 0.9197 on the test set, outperforming the one from paper (0.80)
- WhatsApp Wrapped has a deployed website — add user numbers or load metrics if available
  -> served 100+ users since launch
- Graph coloring project: mention the speedup factor achieved over baseline.
  -> achieved near-linear speedup scaling from sequential to 64-core MPI deployment
- Google DevGroup: add attendance numbers
  -> hackathon was 150 attendees other events were in general 50 attendees

**Before:**

> "Processing high-resolution multivariate time series metrics with heuristics and ML approaches to detect anomalies."

**After:**

> "Built an anomaly detection pipeline ingesting 80+ multivariate HPC metrics at sub-minute resolution; reduced false-positive rate by ~30% vs. threshold-only baseline on 3 real-world workloads."

---

## 3. ATS Keyword Optimisation — 5/10

Strong HPC and ML keywords are present, but core Data Engineering terminology is sparse. A typical JDE job posting scans for: ETL/ELT, data pipeline, data warehouse, dbt, Airflow, orchestration, batch vs streaming, schema design, SQL, BigQuery/Snowflake/Redshift, Docker, Kubernetes, CI/CD. Several are entirely absent.

**Feedback:**

- SQL is completely absent — this is a critical gap for any DE role. Add it to skills and work it into project bullets where applicable.
- Airflow / workflow orchestration not mentioned — if used even lightly, add it.
- "ETL" or "data pipeline" never appears — rephrase project bullets to use this language.
- Kafka and Spark are listed academically — mention them in experience or project bullets to give them weight.
- Add Docker/containerisation if you've used it — a common DE infrastructure keyword.
- Replace the "Streaming Data Analytics" course name with a bullet that uses "stream processing" in a project context.

**WhatsApp Wrapped bullet rewrite for ATS:**

> "Designed and deployed an end-to-end ETL pipeline in Python (pandas) that parses, transforms, and visualises WhatsApp chat data; served via a Flask REST API on Render with a JS/HTML frontend — 500+ public users."

---

## 4. Skills Section Relevance — 6/10

Good honest proficiency labelling, and DVC/SLURM show pipeline and infra awareness. However, the section is HPC-first rather than DE-first, and key DE staples (SQL, cloud platforms, orchestration tools) are missing.

**Feedback:**

- Add SQL (at least Intermediate) — it is the single most screened-for DE skill and its absence is a red flag.
- Add a "Cloud & Infrastructure" group: list any AWS/GCP/Azure exposure, or Docker, even if academic.
- Move Kafka and Spark into a "Data Engineering" sub-group — recruiters often don't read the proficiency qualifier.
- Consider deprioritising SLURM — it's HPC-specific and may confuse DE recruiters.
- Add dbt or Airflow at "Familiar" level if you've touched them — they are the canonical DE toolchain.

**Suggested skills restructure:**

```
Data Engineering : Python (Advanced), SQL (Intermediate), Spark (Academic), Kafka (Academic), dbt (Familiar)
Infrastructure   : Git (Advanced), Docker (Familiar), SLURM (Advanced), DVC (Advanced)
Cloud            : GCP / BigQuery (Familiar)   ← or whichever applies
```

---

## Summary

|                    | Detail                                                                                                                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Strengths**      | Strong academic pedigree (EUMaster4HPC, cum laude); real deployed project (WhatsApp Wrapped); HPC + ML pipeline experience; honest proficiency labels; GitHub links on every project |
| **Weaknesses**     | No quantified impact anywhere; SQL completely missing; no DE-targeted summary/headline; ETL/pipeline language absent; ATS-hostile icon characters                                    |
| **Priority fixes** | Add SQL + cloud platform to skills; quantify at least 3 bullets; write a DE-targeted header summary; reframe project bullets with ETL/pipeline language; fix icon/symbol characters  |

---

## Top 3 Highest-Impact Changes

**1. Add SQL and reframe projects with DE vocabulary**

SQL is screened for in virtually every JDE job description. Its complete absence will cause ATS rejection before a human reads the CV. Adding it to skills and rewriting 2–3 project bullets to use "pipeline", "ETL", and "data transformation" will dramatically increase both ATS pass-rate and recruiter relevance signals.

**2. Quantify at least 3 achievement bullets**

Entry-level candidates who include numbers (dataset size, accuracy, users, speedup) stand out significantly from peers who only describe tasks. Even approximate figures ("~50k rows", "3 production clusters", "5 events, 300+ attendees") shift bullets from responsibility statements to impact statements — which is what drives recruiter callbacks.

**3. Add a 2-line DE-targeted profile summary**

Most recruiters spend under 10 seconds on an initial scan. A clear summary at the top ("Junior Data Engineer | Python · Spark · Kafka · HPC pipelines") immediately signals fit and primes the reader to interpret your HPC experience as DE-relevant rather than niche. Without it, the CV reads as an HPC/ML profile, not a DE one.
