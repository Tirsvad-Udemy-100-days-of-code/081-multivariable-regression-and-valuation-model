# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version<br>Reviewed in RC-001: Go | [0e1081d] |

---

## Executive Summary

Day 81 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" is the capstone project "Predict House Prices". The participant plays an analyst at a real estate development company in Boston in the 1970s and builds a multivariable regression model that values a property from its characteristics (rooms, distance to employment centres, poverty of the area, students per teacher and more). This project turns the two lectures of Day 81 (lecture 597, "Day 81 Goals", and lecture 598, "Solution & Learning Points") into a documented, tested and runnable Python 3.13+ repository with a Jupyter notebook, a `src/` package, pytest tests and a wiki in English, Danish and Bahasa Malaysia. The result is a portfolio piece that fellow course participants and GitHub visitors can read, run and compare against their own solution.

## Methodological and Standards Foundation

The work follows the software quality assurance (SQA) and quality control (QC) framework mounted at `framework/` (Business Case, Stakeholder Analysis, Project Plan, milestones, then code), reviewed against the framework's QC checklists. Quality criteria are tagged with ISO/IEC 25010:2023 characteristics. Code follows the `coding-conventions` skill for Python and the `clean-architecture` layering; source comments are written for Doxygen.

## Problem Statement

- The course gives the exercise as a Google Colab notebook with empty cells; there is no tested, structured, reusable version of the solution.
- A course participant who wants to compare solutions has to copy cells by hand, with no instructions to run them locally and no tests to prove the numbers (r-squared, skew, the estimated property value).
- A GitHub visitor looking for ideas finds no explanation of what each step of the regression workflow teaches.

## Business Opportunity

A clear, runnable repository with the assignment's names, a picture for each step made from the project's own output, and a three-language wiki makes the exercise easy to study, compare and reuse. It also builds the participant's habits of working with a virtual environment, pytest, a pyproject file and a plan-first workflow.

## Objectives

1. Deliver the workflow of Day 81 as Python code in `src/`: data exploration and cleaning, descriptive statistics, feature distributions, pair plots and joint plots, the 80/20 train and test split with `random_state=10`, the multivariable regression, coefficient and residual analysis, the log transformation of the price, the out-of-sample comparison and the valuation of a property.
2. Provide pytest tests in `tests/` that verify every number the notebook and lecture 598 rely on (506 rows and 14 columns, no missing values or duplicates, an 80/20 split of 404 and 102 rows, the training r-squared of the linear and the log model, the extra-room premium, the skew and mean of the residuals, the test r-squared and the estimated price of the average and of the described property).
3. Provide a Jupyter notebook that runs the same steps.
4. Document how to create and use a local `.venv`, how to upgrade `pip`, and how to run the project and its tests, on Linux and Windows.
5. Provide a README and a wiki in English, Danish and Bahasa Malaysia, with a picture for each step made from the project's own output, and an explanation of what each step taught.
6. Publish the repository with a description and topics, one reviewed pull request per milestone.

## Scope

### In Scope

- Python 3.13 or newer, `venv`, `pyproject.toml`, Python `.gitignore`, `constants.py`, Doxygen comments and a `Doxyfile`.
- The comma-separated values (CSV) data file and the notebooks from the lecture resources (used as provided by the course, for personal study).
- Code for the Day 81 workflow, pytest tests, a Jupyter notebook.
- README from the framework template; wiki pages (en, da, ms) including a Getting Started page with Linux and Windows guides, modelled on the Getting Started page of project 074.
- Static analysis with opengrep before each push.
- Repository description and topics on the Gitea host.

### Out of Scope

- Any other course day.
- A graphical or web user interface.
- Runtime dependencies beyond what the analysis needs (pandas, NumPy, Matplotlib, Seaborn, Plotly, scikit-learn).
- Publishing to PyPI.
- Screenshots of the Udemy lectures: README and wiki only summarise the lectures; their pictures are made from this project's own output.
- Judging the dataset: the Boston house price data contains the column `B`, which encodes a racial proportion. It is kept because the assignment uses it, and the documents say so.

## Expected Benefits

### Tangible Benefits

- A repository that runs from a clean clone with documented commands.
- Tests that fail if a number of the workflow changes.
- A picture and a wiki page for each step.

### Intangible Benefits

- Understanding of how a regression model is built, checked on residuals, improved by a data transformation and used for a prediction.
- Practice with a structured, reviewed workflow.
- A reusable template for the next course-day repositories.

## Strategic Alignment

The repository is one of the participant's 100 Days of Code projects. It supports the aim of keeping each day's work readable and comparable for other course participants and visible as a portfolio on GitHub.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Workflow steps implemented | 6 of 6 (exploration, distributions, relationships, regression, log model, valuation) | Each step has code, a test and a wiki page |
| 2 | Tests pass | 100 % of tests pass on Python 3.13 | `pytest` exits 0 |
| 3 | Lecture numbers reproduced | All stated figures match | Tests assert them |
| 4 | Wiki languages | 3 (en, da, ms), same page set | Page list per language |
| 5 | Pictures | At least 1 per step in README and wiki, made from project output | Image count |
| 6 | Run from clean clone | Documented commands work on Windows and Linux | Getting Started guides followed |
| 7 | Static analysis | 0 opengrep findings left unaddressed before each push | opengrep report |
| 8 | Runtime dependencies | Only the analysis libraries | `pyproject.toml` review |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Lecture resources cannot be downloaded | Data and notebook missing | Stop and report; the user supplies the files |
| Course data is copyrighted | Redistribution problem | Keep the repository for personal study; state the source and rights in the README |
| Udemy shows a bot check | Lecture or resource unreadable | Stop and ask the user to pass the check; never bypass it |
| Translations drift from English | Inconsistent wiki | English is authoritative; same page set checked before each review |
| Plotting tests are slow or flaky (the pair plot of 14 columns takes minutes) | CI red | Use the non-interactive Agg backend, assert on data and figure structure, not pixels, and test the pair plot on a small subset |
| Regression figures differ between scikit-learn versions | Tests fail | Assert with tolerances and pin only the lower bound of the dependency |
| Token leak | Credential exposure | Tokens stay in the parent `.env`, which is git-ignored and never read by project code |

## Assumptions

- The user is the Product Owner and developer (S01); in autonomous mode the AI acts as reviewer stand-in for S01 and records it.
- The two Udemy lectures stay available in the user's Chrome session.
- The git host accepts the tokens in the parent `.env` for issues, repository, wiki and release work.
- The Product Owner (PO) language is English and the PO domain is IT.

## Constraints

- Python 3.13 or newer; `venv`; pytest; `pyproject.toml`; constants in `constants.py`.
- Folders `src/`, `tests/` and `docs/`.
- Nothing under `src/` or `tests/` before an accepted milestone with a `Go` review.
- Tokens are used only from `.env` for personal use, never imported or tested by the project.
- No GUI test on the host desktop.
- Finished within one week of the plan acceptance, by 2026-11-23.

## Cost–Benefit Assessment

Qualitative; the project is a personal learning exercise with no revenue, so a numeric model would add nothing.

| Costs | Benefits |
| --- | --- |
| The participant's time for the workflow steps, tests and a three-language wiki | A runnable, tested, documented portfolio repository and a reusable workflow |
| Review effort per milestone | Readable code for fellow course participants |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owns the goal, builds and reviews the work |
| S02 | Reads and runs the code and compares solutions |
| S03 | Browses the repository for ideas |

## Recommendation

Proceed — the scope is small, the workflow steps are well defined and the result is useful to all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[PP-001]: ./project-plan.md
[0e1081d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/commit/0e1081ddb340d222e4fb986725d5a7feef19e5f8
