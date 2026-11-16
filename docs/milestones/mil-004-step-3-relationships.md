# MIL-004 Step 3 Relationships in the Data

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version<br>Reviewed in RC-006: Go | [0e1081d] |

---

## Purpose

Decide whether the exploration of relationships between features (pair plot and the five joint plots) is implemented, tested and documented.

## Deliverable

Functions for the Seaborn pair plot and the joint plots (`DIS` versus `NOX`, `NOX` versus `INDUS`, `LSTAT` versus `RM`, `LSTAT` versus `PRICE`, `RM` versus `PRICE`) with `alpha=0.5`, correlation helpers that back each stated observation, tests, the notebook section, a picture, and the wiki page in en, da and ms.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The five joint plots exist with the colours and the `alpha=0.5` of the assignment | Pass | Any missing |
| 2 | Tests assert the sign of the correlation of each observation (`NOX`/`DIS` negative, `NOX`/`INDUS` positive, `LSTAT`/`RM` negative, `LSTAT`/`PRICE` negative, `RM`/`PRICE` positive) | Pass | Mismatch |
| 3 | The pair plot function is tested on a subset of columns so the test suite stays fast | Pass | Test slower than 30 seconds |
| 4 | A picture made from the project's output is in README and wiki | Present | Missing |
| 5 | Wiki page exists in en, da and ms | Present | Missing |
| 6 | opengrep clean and pytest green | Pass | Fail |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Chart helpers and the loader |

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

2026-11-19 — within the one-week schedule.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the pair plot | Function that draws the Seaborn `pairplot` of a DataFrame, with an option for the regression line and for a column subset. | No | |
| 2 | Implement the joint plot helper and the five joint plots | One helper with colour, style and the `alpha` keyword, used for the five relationships of the assignment. | No | |
| 3 | Implement the correlation helpers | Functions returning the correlation of two features, so each observation of the assignment is testable. | No | |
| 4 | Write tests for step 3 | Pytest tests for the plot functions (Agg backend) and the correlation signs. | No | |
| 5 | Add notebook section and Doxygen comments | Mirror step 3 in the Jupyter notebook and comment every function for Doxygen. | No | |
| 6 | Render the step 3 picture and update README | Render a joint plot of `RM` versus `PRICE` from the project's own output and show it in the README. | No | |
| 7 | Write the step 3 wiki page in en, da and ms | Explain what was gained: spotting relationships, multicollinearity and why we look before we model. | No | |

---

[BC-001]: ../business-case.md
[0e1081d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/commit/0e1081ddb340d222e4fb986725d5a7feef19e5f8
