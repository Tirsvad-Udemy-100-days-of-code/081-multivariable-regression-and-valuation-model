# MIL-001 Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version<br>Reviewed in RC-003: Go | [0e1081d] |

---

## Purpose

Decide whether the project skeleton, tooling, data and documentation base are good enough to build the workflow steps on (lecture 597, "Day 81 Goals").

## Deliverable

A repository with `pyproject.toml`, Python `.gitignore`, `.editorconfig`, `src/` and `tests/` skeleton with `constants.py`, the lecture data and notebooks, a `Doxyfile`, a README from the framework template, a Getting Started wiki page (Linux and Windows) in en, da and ms, repository description and topics on the host, and the picture generator that renders README and wiki pictures from the project's own output.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m venv .venv`, `python -m pip install --upgrade pip`, `pip install -e ".[dev]"` and `pytest` work from a clean clone | Pass | Any step fails |
| 2 | `pyproject.toml` requires Python 3.13 or newer; runtime dependencies are only pandas, NumPy, Matplotlib, Seaborn, Plotly and scikit-learn | Pass | Other runtime dependency |
| 3 | The CSV data file and the start and complete notebooks are in the repository | Present | Missing |
| 4 | The repository on the host has a description and at least five topics | Set | Missing |
| 5 | Getting Started exists in en, da and ms with Linux and Windows sections | Present | Page or section missing |
| 6 | opengrep run shows no unaddressed finding | 0 open | Open finding |
| 7 | README follows the framework template and `check-readme.sh` passes; `check-editorconfig.sh` passes | Pass | Fail |

## Dependencies

| Depends on | Reason |
| --- | --- |
| BC-001, SA-001, PP-001 accepted | Baseline of the plan-first gate |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 3, 4, 5 and 6; success criteria 6, 7 and 8 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-17 — within the one-week schedule of the Project Plan.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Record the ADR for skipped use-case artifacts | The project is a set of pure analysis functions with one actor, so use cases, user stories and a presentation pattern add nothing. Record the skip in an architecture decision record (ADR-0001) as the create-project skill requires. | No | |
| 2 | Set repository description and topics | Use the Gitea API with the repository token read from the parent `.env` (never stored, imported or tested by the project) to set a one-line description and topics such as python, pandas, scikit-learn, seaborn, plotly, jupyter, linear-regression, data-analysis, udemy and 100-days-of-code. Serves S03. | No | |
| 3 | Add pyproject.toml | Configure Python 3.13 or newer, runtime dependencies pandas, numpy, matplotlib, seaborn, plotly and scikit-learn only, a `dev` extra with pytest and ruff, a `notebook` extra with jupyterlab and ipykernel, pytest settings and the src layout. | No | |
| 4 | Add Python .gitignore | Standard Python ignores plus `.venv/`, `.env`, notebook checkpoints, Doxygen output and `docs/ai-prompts/`. | No | |
| 5 | Add .editorconfig | Create the root `.editorconfig` from `framework/templates/editorconfig/baseline.editorconfig` and check it with `check-editorconfig.sh`. | No | |
| 6 | Create src and tests skeleton with constants.py | Create the package `boston_valuation` under `src/` with domain, infrastructure and presentation layers, an empty `tests/` with a conftest that selects the Agg backend, and `constants.py` holding file names, column names, the random state and the other figures of the workflow. | No | |
| 7 | Add the lecture data and notebooks | Take the CSV file and the start and complete notebooks from the two zips downloaded through the user's Chrome session (lectures 597 and 598), put the CSV in the package data folder and the notebooks in a notebooks folder. | No | |
| 8 | Add Doxyfile | Add a Doxyfile configured for the Python sources so the Doxygen comments render. | No | |
| 9 | Add the picture generator | Create `presentation/screenshots.py` that renders the README and wiki pictures of each step from the project's own output with the Agg backend, so no lecture screenshot is ever used. | No | |
| 10 | Write README from the framework template | Use `framework/templates/README-template.md`, include run and test instructions, the venv steps, a summary of the two lectures (text only) and the first picture. | No | |
| 11 | Document the local venv and pip upgrade | Describe creating and using `.venv` and `python -m pip install --upgrade pip` in README and wiki. | No | |
| 12 | Write the Getting Started wiki in en, da and ms | Model it on the Getting Started page of project 074 with separate Linux and Windows guides, plus Home and sidebar, in English, Danish and Bahasa Malaysia. | No | |
| 13 | Add opengrep local check | Document and run opengrep from `~/.opengrep/cli/latest/opengrep.exe` before every push and fix the findings. | No | |
| 14 | Enable the git hooks and the plan gate | Run `framework/scripts/install-git-hooks.sh --enable-plan-gate` so no commit lands on `main` and each change under `src/` or `tests/` carries a `Task:` trailer. | No | |

---

[BC-001]: ../business-case.md
[0e1081d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/commit/0e1081ddb340d222e4fb986725d5a7feef19e5f8
