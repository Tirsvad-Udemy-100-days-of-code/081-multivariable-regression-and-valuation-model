# SQA Review Record RC-019

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-019 |
| CrossReference | [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: source code of MIL-006 on its branch (log transformation helpers, log model, model comparison and the step 5 panel picture)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | ruff (pycodestyle naming rules N) passes; names are snake_case, UPPER_SNAKE and PascalCase. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names come from the assignment and the data columns (price, rooms, residuals, log price). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` pass; the only suppressions are the documented ones, if any. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every signature is annotated, `-> None` included. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare or swallowed exceptions; specific exceptions are raised. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no builtin shadowed (ruff B rules pass). |
| 7 | Files, locks and connections are managed with context managers | Pass | Files are read through `pathlib` paths and pandas, never left open, figures are closed after saving. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Doxygen docstrings (@brief, @param, @return) on every public module and function. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `logging` is used, never `print`; no secrets or personal data are logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | N-A by ADR-0001: no Design Class Diagram exists; functions implement the milestone tasks directly. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | pytest tests named for the behaviour; no network, no order dependence, Agg backend. 300 tests pass; they assert the skew of price 1.11 and log price -0.33, training r-squared 0.75 and 0.79, test r-squared 0.67 and 0.74, the log coefficient signs (CHAS positive, PTRATIO negative) and the residual mean and skew of both models. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | mypy strict is not configured; only ruff is. Optional. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Dependencies are declared in pyproject.toml with minimum versions; none unused. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Names, colours, limits and scenario values live in constants.py only. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain imports no plotting or file-access code (ADR-0002); infrastructure and presentation import domain and constants; no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Small pure functions; one reason to change per module; the picture registry is extended by one line per picture. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | src/boston_valuation/{domain,infrastructure,presentation}, tests/unit; no application layer by ADR-0002 (a merged layer is accepted when an ADR says why); imports point inward. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | English names with letters, digits, `_` and `.` only. |

## Overall Verdict

Go — every criterion of QC-PY-001 is Pass or N-A; there is no blocking finding. The review is by the author's stand-in and is not independent; S01 can challenge it in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |

---
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
