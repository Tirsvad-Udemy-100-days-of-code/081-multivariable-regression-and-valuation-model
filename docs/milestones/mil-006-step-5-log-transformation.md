# MIL-006 Step 5 Log Transformation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version<br>Reviewed in RC-008: Go | pending |

---

## Purpose

Decide whether the data transformation of the target (log price), the second regression, the side-by-side comparison and the out-of-sample comparison are implemented, tested and documented.

## Deliverable

Functions for the skew of price and log price, the log mapping chart, the log regression with the same split, its coefficients, the side-by-side regression and residual charts (indigo and navy), the residual mean and skew of both models, the test-set r-squared of both models, tests, the notebook section, a picture, and the wiki page in en, da and ms.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The skew of the log price is closer to zero than the skew of the price, and a test asserts it | Pass | Mismatch |
| 2 | The training r-squared of the log model is 0.79 and higher than the linear model | Pass | Mismatch |
| 3 | The test-set r-squared is 0.67 for the linear and 0.74 for the log model, and both are lower than their training values | Pass | Mismatch |
| 4 | The log coefficients are asserted: `CHAS` positive, `PTRATIO` negative (more students per teacher lowers prices) | Pass | Mismatch |
| 5 | A picture made from the project's output is in README and wiki; wiki page exists in en, da and ms | Present | Missing |
| 6 | opengrep clean and pytest green | Pass | Fail |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-005 | The split, the linear model and the residual helpers |

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

2026-11-21 — within the one-week schedule.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the log transformation helpers | Functions for the skew of a Series, the log of the price and the mapping chart of the price to its log. | No | |
| 2 | Implement the log regression | Function that splits with the same random state, fits the model on the log price and returns it with its r-squared, predictions and residuals. | No | |
| 3 | Implement the log coefficient table | Coefficient DataFrame of the log model and the checks of the signs of `CHAS` and `PTRATIO`. | No | |
| 4 | Implement the side-by-side comparison charts | Actual versus predicted and residual plots for both models, indigo for the linear and navy for the log model, and the residual distributions. | No | |
| 5 | Implement the out-of-sample comparison | Function returning the test-set r-squared of both models. | No | |
| 6 | Write tests for step 5 | Pytest tests with the figures of the criteria, with tolerances. | No | |
| 7 | Add notebook section and Doxygen comments | Mirror step 5 in the Jupyter notebook and comment every function for Doxygen. | No | |
| 8 | Render the step 5 picture and update README | Render the log price versus predicted comparison picture from the project's own output and show it in the README. | No | |
| 9 | Write the step 5 wiki page in en, da and ms | Explain what was gained: skew, log transformation, comparing models on unseen data. | No | |

---

[BC-001]: ../business-case.md
