# MIL-007 Step 6 Valuation Model

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-007 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version<br>Reviewed in RC-009: Go | [0e1081d] |

---

## Purpose

Decide whether the use of the log model to estimate the value of a property (the average property and the described property) is implemented, tested and documented.

## Deliverable

Functions that build the average property, estimate its log price and dollar value, set the characteristics of the described property (river, 8 rooms, 20 students per teacher, distance 5, high pollution, low poverty) and estimate its value, tests asserting the figures, the notebook section, a picture, and the wiki page in en, da and ms.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The average property has a log estimate of about 3.03 and a dollar estimate of about 20,703 | Pass | Mismatch |
| 2 | The described property has a log estimate of about 3.25 and a dollar estimate of about 25,792 | Pass | Mismatch |
| 3 | The valuation function takes the characteristics as parameters and keeps the averages for all other features | Pass | Any missing |
| 4 | A picture made from the project's output is in README and wiki; wiki page exists in en, da and ms | Present | Missing |
| 5 | opengrep clean and pytest green | Pass | Fail |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-006 | The log model |

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

2026-11-22 — within the one-week schedule.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the average property | Function building a one-row DataFrame of the mean of every feature. | No | |
| 2 | Implement the estimate | Function turning a property row into a log estimate and a dollar value with `exp`, in thousands converted to dollars. | No | |
| 3 | Implement the described property | Function `value_property` with the characteristics as parameters (river, rooms, students per classroom, distance to town, pollution, poverty), keeping the averages for the other features. | No | |
| 4 | Write tests for step 6 | Pytest tests with the figures of the criteria, with tolerances. | No | |
| 5 | Add notebook section and Doxygen comments | Mirror step 6 in the Jupyter notebook and comment every function for Doxygen. | No | |
| 6 | Render the step 6 picture and update README | Render a picture comparing the average and the described property value from the project's own output and show it in the README. | No | |
| 7 | Write the step 6 wiki page in en, da and ms | Explain what was gained: using a model to answer a business question and reversing a log transformation. | No | |

---

[BC-001]: ../business-case.md
[0e1081d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/commit/0e1081ddb340d222e4fb986725d5a7feef19e5f8
