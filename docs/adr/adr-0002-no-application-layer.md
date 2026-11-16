# No application layer; analysis libraries in the domain

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [BC-001], [ADR-0001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version<br>Reviewed in RC-013: Go | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The `clean-architecture` skill lays source out in the packages `domain`, `application`, `infrastructure` and `presentation`, and its checklist (`QC-PY-001`, criteria 15 and 17) accepts a merged layer only when an ADR says why. This project has no use cases ([ADR-0001]): it is a set of pure functions that read one table, fit scikit-learn models and draw charts. The forces are the one-week deadline of [BC-001], one actor, and the wish of S02 to read functions that carry the names of the assignment. The analysis itself is pandas, NumPy and scikit-learn code, so the business rules cannot be written without them. Options considered: (a) add an `application` package of thin use-case functions that call the domain; (b) leave the `application` layer out, keep the functions of the workflow in `domain`, and let the notebook and the picture generator orchestrate the steps; (c) forbid pandas and scikit-learn in `domain` and wrap them in `infrastructure`.

## Decision

The package has the layers `domain`, `infrastructure` and `presentation`, and no `application` layer; the workflow functions live in `domain`. `domain` may import pandas, NumPy and scikit-learn, because they are the language of the analysis, but never Matplotlib, Seaborn, Plotly or file access; those belong to `presentation` and `infrastructure`.

## Consequences

**Positive:**

- Every step is one readable module of functions with the assignment's names; no layer that only forwards calls.
- The rule that decides where code goes is simple and testable: plotting libraries and file access never appear in `domain`.

**Negative:**

- If a user interface or an API is added later, an `application` layer must be introduced and this decision revisited.
- `domain` depends on third-party analysis libraries, so a change of library touches the business rules.

## Affected Artifacts

- [BC-001] — success criterion 8 (only the analysis libraries as runtime dependencies) is kept.
- [ADR-0001] — the decision to skip use cases is the reason an application layer would be empty.

---

[BC-001]: ../business-case.md
[ADR-0001]: ./adr-0001-skip-use-case-artifacts.md
