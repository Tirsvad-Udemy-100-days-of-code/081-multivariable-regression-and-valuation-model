# MIL-008 Step 7 Summary and Release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-008 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version<br>Reviewed in RC-010: Go | [0e1081d] |

---

## Purpose

Decide whether lecture 598 ("Solution & Learning Points") is summarised, the wiki is complete and published, and the repository is ready to release.

## Deliverable

The summary page of the learning points of lecture 598 in README and wiki (en, da, ms), the completed notebook, a summary picture, the published wiki on the host, the release `v1.0.0` and a final check of the repository.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The seven learning points of lecture 598 are each tied to the step that taught them | Present | Missing |
| 2 | The wiki has the same page set in en, da and ms and is published to the host wiki | Present | Missing |
| 3 | `check-readme.sh`, `check-languages.sh`, `check-qc-tags.sh` and `check-editorconfig.sh` exit with code 0 | Pass | Fail |
| 4 | `pytest` passes on Python 3.13 and opengrep shows no unaddressed finding | Pass | Fail |
| 5 | The release `v1.0.0` exists on the host | Present | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-007 | All steps implemented |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 5 and 6; success criteria 1 to 8 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-23 — the Business Case deadline.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the lecture 598 summary | Summarise the seven learning points in the README and in a wiki page, each pointing at the step and the function that shows it. | No | |
| 2 | Complete the notebook | Run the notebook end to end so its stored outputs match the tests. | No | |
| 3 | Render the summary picture and update README | Render the picture comparing both models on the test set from the project's own output. | No | |
| 4 | Write the summary wiki page in en, da and ms | Explain what was gained over the whole day and how to continue. | No | |
| 5 | Publish the wiki to the host | Push the pages of `docs/wiki` to the wiki repository of the host with the wiki token from the parent `.env`. | No | |
| 6 | Run the final checks | Run the framework check scripts, pytest and opengrep, and record the code reviews. | No | |
| 7 | Create the release v1.0.0 | Tag and publish the release on the host with the release token from the parent `.env`. | No | |

---

[BC-001]: ../business-case.md
[0e1081d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/commit/0e1081ddb340d222e4fb986725d5a7feef19e5f8
