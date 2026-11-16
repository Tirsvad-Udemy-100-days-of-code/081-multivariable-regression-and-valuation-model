# MIL-003 Step 2 Feature Distributions

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version<br>Reviewed in RC-005: Go | pending |

---

## Purpose

Decide whether the visualisation of the features (price, distance to employment centres, rooms, highway access and the river dummy) is implemented, tested and documented.

## Deliverable

Chart functions for the four distribution challenges (Seaborn `displot` with a Kernel Density Estimate (KDE) for `PRICE`, `DIS` and `RM`, a Matplotlib histogram for `RAD`) and the Plotly bar chart for `CHAS`, tests of the figure structure, the notebook section, a picture, and the wiki page in en, da and ms.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Distribution functions use `aspect=2`, a KDE and 50 bins for the price, and the titles carry the averages | Pass | Any missing |
| 2 | The river bar chart returns a Plotly figure with the two categories `No` and `Yes` and 471 and 35 homes | Pass | Mismatch |
| 3 | A picture made from the project's output is in README and wiki | Present | Missing |
| 4 | Wiki page exists in en, da and ms | Present | Missing |
| 5 | opengrep clean and pytest green | Pass | Fail |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The loader and the data helpers |

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

2026-11-18 — within the one-week schedule.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the price distribution chart | Histogram with a KDE of `PRICE` (50 bins, `aspect=2`, colour `#2196f3`) with the average in the title. | No | |
| 2 | Implement the distance and rooms distribution charts | Charts for `DIS` (dark blue) and `RM` (teal) with the averages in the titles. | No | |
| 3 | Implement the highway access histogram | Matplotlib histogram of `RAD` with 24 bins, black edges, purple bars and a bar width of 0.5. | No | |
| 4 | Implement the river bar chart | Plotly bar chart of `CHAS` counts with the labels `No` and `Yes`, the haline colour scale and no colour axis. | No | |
| 5 | Write tests for step 2 | Pytest tests for the structure of the figures using the Agg backend and the counts behind the river chart. | No | |
| 6 | Add notebook section and Doxygen comments | Mirror step 2 in the Jupyter notebook and comment every function for Doxygen. | No | |
| 7 | Render the step 2 picture and update README | Render a picture of the price distribution from the project's own output and show it in the README. | No | |
| 8 | Write the step 2 wiki page in en, da and ms | Explain what was gained: reading distributions, skew, outliers and categorical bars. | No | |

---

[BC-001]: ../business-case.md
