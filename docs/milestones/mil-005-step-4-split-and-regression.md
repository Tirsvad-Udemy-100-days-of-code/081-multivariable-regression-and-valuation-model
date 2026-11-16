# MIL-005 Step 4 Split and Multivariable Regression

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version<br>Reviewed in RC-007: Go | [0e1081d] |

---

## Purpose

Decide whether the training and test split, the first multivariable regression, the coefficient check and the residual analysis are implemented, tested and documented.

## Deliverable

Functions for the 80/20 split with `random_state=10`, the linear regression on the training data, the coefficient table, the room premium, the actual versus predicted and the residual plots, the mean and skew of the residuals, tests asserting the figures, the notebook section, a picture, and the wiki page in en, da and ms.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The split gives 404 training and 102 test rows (79.8 % and 20.2 %) | Pass | Mismatch |
| 2 | The training r-squared of the regression is 0.75 and the extra-room premium is about 3108.5 dollars | Pass | Mismatch |
| 3 | The coefficients have the expected signs (`RM` positive, `LSTAT` and `NOX` negative, `CHAS` positive) | Pass | Mismatch |
| 4 | The residual figures (mean and skew) are computed and asserted, and the plots are produced in the assignment's colours | Pass | Any missing |
| 5 | A picture made from the project's output is in README and wiki; wiki page exists in en, da and ms | Present | Missing |
| 6 | opengrep clean and pytest green | Pass | Fail |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | Understanding of the relationships and the chart helpers |

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

2026-11-20 — within the one-week schedule.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the train and test split | Function using `train_test_split` with `test_size=0.2` and `random_state=10`, plus the helper that reports the percentages. | No | |
| 2 | Implement the linear regression | Function that fits `LinearRegression` on the training data and returns the model with its training r-squared. | No | |
| 3 | Implement the coefficient table and the room premium | Function returning a one-column DataFrame of coefficients and a function returning the dollar premium of one extra room. | No | |
| 4 | Implement the residual analysis | Functions for the predictions, the residuals, their mean and skew. | No | |
| 5 | Implement the regression charts | Actual versus predicted values with the cyan identity line, the residuals versus predicted values, and the residual distribution with a KDE, in indigo. | No | |
| 6 | Write tests for step 4 | Pytest tests with the figures of the criteria, with tolerances. | No | |
| 7 | Add notebook section and Doxygen comments | Mirror step 4 in the Jupyter notebook and comment every function for Doxygen. | No | |
| 8 | Render the step 4 picture and update README | Render the actual versus predicted picture from the project's own output and show it in the README. | No | |
| 9 | Write the step 4 wiki page in en, da and ms | Explain what was gained: out-of-sample thinking, reading coefficients and residuals. | No | |

---

[BC-001]: ../business-case.md
[0e1081d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/commit/0e1081ddb340d222e4fb986725d5a7feef19e5f8
