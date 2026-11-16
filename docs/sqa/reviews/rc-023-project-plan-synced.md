# SQA Review Record RC-023

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-023 |
| CrossReference | [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [c6ed0a7] |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001]
- Scope: change review: the Milestone column
- Language and domain: en / it
- Language reviewer: none (the reviewer stand-in reads English and knows the IT domain)
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Unchanged since [RC-012]. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Unchanged since [RC-012]. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Unchanged since [RC-012]. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Unchanged since [RC-012]. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Unchanged since [RC-012]. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Unchanged since [RC-012]. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Unchanged since [RC-012]. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Unchanged since [RC-012]. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Unchanged since [RC-012]. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Unchanged since [RC-012]. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Unchanged since [RC-012]. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Unchanged since [RC-012]. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Unchanged since [RC-012]. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | The Milestone column now links the milestone of each gateway on the host (602 to 609), created by the publish workflow after each merge; the eight links were read from the host's milestone list. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | Unchanged since [RC-012]. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has Language `en` and Domain `it`, no placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | Prose and table cells of PP-001 are English. Confirmed by the AI stand-in for S01 (the document author is S01; not independent). |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register per registry for this artifact type is checked against the wording. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No dictionary (`DICT`) exists; the document uses plain IT vocabulary with one term per concept (milestone and gateway are used as the framework does). Confirmed by the AI stand-in for S01. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No `<name>.<language>.md` twin exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | Initial version; no earlier language to compare. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The stand-in reads English and knows the IT domain; confirmed in this record, not independent, open to challenge in the run summary. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out on first use or are established terms of the domain. |

## Overall Verdict

Go — every criterion of QC-PP-001 and QC-LANG-001 is Pass or N-A; there is no blocking finding. The review is by the author's stand-in and is not independent; S01 can challenge it in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |

---
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[c6ed0a7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/commit/c6ed0a768a7fef6d86d64d622dbb1bc94e6ce4f4
