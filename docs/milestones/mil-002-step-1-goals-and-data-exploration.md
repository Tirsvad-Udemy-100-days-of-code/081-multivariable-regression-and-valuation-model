# MIL-002 Step 1 Goals and Data Exploration

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version<br>Reviewed in RC-004: Go | pending |

---

## Purpose

Decide whether lecture 597 ("Day 81 Goals") and the first part of the notebook (set-up, loading the data, preliminary exploration, data cleaning and descriptive statistics) are implemented, tested and documented.

## Deliverable

Code that loads `boston.csv` with the first column as index, answers the exploration challenges (shape, column names, NaN values, duplicates) and the descriptive statistics challenges (students per teacher, average price, the `CHAS` feature, rooms per dwelling), tests asserting the figures, the notebook section, a picture made from project output in README and wiki, and the wiki page in en, da and ms.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Tests assert the shape (506, 14), the 14 column names, no NaN values and no duplicates | Pass | Mismatch |
| 2 | Tests assert the descriptive figures: `CHAS` is 0 or 1, the mean price is about 22.53 (thousand dollars), the mean pupil-teacher ratio is about 18.46 and the room range is stated | Pass | Mismatch |
| 3 | A picture made from the project's output is in README and wiki; no lecture screenshot is used | Present | Missing or a lecture screenshot |
| 4 | Wiki page exists in en, da and ms and summarises lecture 597 in words | Present | Missing |
| 5 | opengrep clean and pytest green | Pass | Fail |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Skeleton, data and tooling |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2, 3 and 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-17 — within the one-week schedule.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Load the Boston data | Provide a loader function that reads `boston.csv` into a pandas DataFrame with `index_col=0`, using names from `constants.py`. | No | |
| 2 | Implement the preliminary exploration helpers | Functions for the shape, the column names, the missing-value check and the duplicate check, so the answers are testable. | No | |
| 3 | Implement the descriptive statistics helpers | Functions answering the descriptive challenges: average students per teacher, average price, the minimum and maximum of `CHAS`, and the minimum and maximum rooms per dwelling. | No | |
| 4 | Write tests for step 1 | Pytest tests for the loader, the exploration and the descriptive functions with the figures above. | No | |
| 5 | Add notebook section and Doxygen comments | Mirror step 1 in the Jupyter notebook and comment every function for Doxygen. | No | |
| 6 | Render the step 1 picture and update README | Render a picture of the descriptive statistics table from the project's own output, save it under `docs/images`, show it in the README together with a text summary of lecture 597. | No | |
| 7 | Write the step 1 wiki page in en, da and ms | Explain what was gained: reading the problem as an analyst, checking data quality and reading descriptive statistics. | No | |

---

[BC-001]: ../business-case.md
