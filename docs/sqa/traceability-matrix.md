# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Deprecated | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Added RC-017 for the MIL-004 code | [c164920] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Added RC-018 for the MIL-005 code | [2e0fa37] |

---

## Purpose

Tracks backward and forward links between artifact instances so that traceability from objective to gateway to review is measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001] to [MIL-008] | [RC-012] |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-003] |
| [MIL-002] | MIL | en | it | [BC-001], [MIL-001] | [MIL-003] | [RC-004] |
| [MIL-003] | MIL | en | it | [BC-001], [MIL-002] | [MIL-004] | [RC-005] |
| [MIL-004] | MIL | en | it | [BC-001], [MIL-003] | [MIL-005] | [RC-006] |
| [MIL-005] | MIL | en | it | [BC-001], [MIL-004] | [MIL-006] | [RC-007] |
| [MIL-006] | MIL | en | it | [BC-001], [MIL-005] | [MIL-007] | [RC-008] |
| [MIL-007] | MIL | en | it | [BC-001], [MIL-006] | [MIL-008] | [RC-009] |
| [MIL-008] | MIL | en | it | [BC-001], [MIL-007] | - | [RC-010] |
| [ADR-0001] | ADR | - | - | [BC-001], [PP-001] | - | [RC-011] |
| [ADR-0002] | ADR | - | - | [BC-001], [ADR-0001] | - | [RC-013] |
| Source code (`src/`, `tests/`) | PY | - | - | [MIL-002] to [MIL-007] | - | [RC-014], [RC-015], [RC-016], [RC-017], [RC-018] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | none (no views; see ADR-0001) | [ADR-0001] | pytest tests, MIL-002 to MIL-007 | Planned |
| CN-002 | none | [ADR-0001] | pull request per milestone | Planned |
| CN-003 | none | [ADR-0001] | Getting Started guides, MIL-001 | Covered |
| CN-004 | none | [ADR-0001] | tests call the assignment's function names | Planned |
| CN-005 | none | [ADR-0001] | repository description, topics, README, MIL-001 | Covered |
| CN-006 | none | [ADR-0001] | pyproject review, MIL-001 | Covered |
| CN-007 | none | [ADR-0001] | pictures and wiki, MIL-002 to MIL-008 | Planned |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |

## Coverage Notes

- There are no use cases, user stories, domain model or design artifacts ([ADR-0001]), and no Architecture Description or Test Plan; concerns are answered by code, tests and documentation.
- `-` in Upstream means foundational; `-` in Downstream means nothing is built on it yet.
- The Status of a concern changes from `Planned` to `Covered` when the milestone that answers it is accepted.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-step-1-goals-and-data-exploration.md
[MIL-003]: ../milestones/mil-003-step-2-feature-distributions.md
[MIL-004]: ../milestones/mil-004-step-3-relationships.md
[MIL-005]: ../milestones/mil-005-step-4-split-and-regression.md
[MIL-006]: ../milestones/mil-006-step-5-log-transformation.md
[MIL-007]: ../milestones/mil-007-step-6-valuation.md
[MIL-008]: ../milestones/mil-008-lecture-598-summary-release.md
[ADR-0002]: ../adr/adr-0002-no-application-layer.md
[ADR-0001]: ../adr/adr-0001-skip-use-case-artifacts.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-mil-001.md
[RC-004]: ./reviews/rc-004-mil-002.md
[RC-005]: ./reviews/rc-005-mil-003.md
[RC-006]: ./reviews/rc-006-mil-004.md
[RC-007]: ./reviews/rc-007-mil-005.md
[RC-008]: ./reviews/rc-008-mil-006.md
[RC-009]: ./reviews/rc-009-mil-007.md
[RC-010]: ./reviews/rc-010-mil-008.md
[RC-011]: ./reviews/rc-011-adr-0001.md
[RC-012]: ./reviews/rc-012-project-plan.md
[RC-013]: ./reviews/rc-013-adr-0002.md
[RC-014]: ./reviews/rc-014-code-mil-001.md
[RC-015]: ./reviews/rc-015-code-mil-002.md
[RC-016]: ./reviews/rc-016-code-mil-003.md
[RC-017]: ./reviews/rc-017-code-mil-004.md
[c164920]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/commit/c1649208bd12a1d006e1434ae1359b6eaff934af
[RC-018]: ./reviews/rc-018-code-mil-005.md
[2e0fa37]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/commit/2e0fa379ad92ce85270057bf9ea16d1509135cd8
