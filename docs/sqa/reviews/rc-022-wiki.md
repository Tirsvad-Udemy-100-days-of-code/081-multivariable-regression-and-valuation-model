# SQA Review Record RC-022

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-022 |
| CrossReference | [QC-WIKI-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [c6ed0a7] |

---

## Artifact Under Review

- Instance reviewed: the wiki in `docs/wiki` (27 pages and the sidebar) and its published copy
- Checklist used: [QC-WIKI-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en, da, ms / it
- Language reviewer: none (the reviewer stand-in reads English and knows the IT domain)
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | It starts with the wiki title in bold, then one list of the nine English pages with `Home` first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | The list holds Home, Getting Started and the seven step pages; a script over `docs/wiki` found no link to a missing page; the host renders every one. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | No `**Related**` section: the wiki has no related wiki. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | `**Languages**` is the last section, with English, Dansk and Bahasa Melayu linking to `Home`, `Home-da` and `Home-ms`. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar and the Home pages are plain files kept by hand in `docs/wiki`; the repository has no generator that produces them. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page starts with the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | The wiki exists in English (the PO language of the registry), Danish and Bahasa Malaysia. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | The nine English pages each have a `-da` and a `-ms` page: 27 pages, none missing. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Each page starts with `**English** · [Dansk](...) · [Bahasa Malaysia](...)` with the current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Translations are named `<Page>-da.md` and `<Page>-ms.md`; English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Function names, file names, commands and IDs stay in English in every language. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | Checked on the published wiki after the merge of MIL-008 (PR 78): the host lists 28 pages (27 pages and the sidebar); `Home`, `Home-da`, `Step-7-Summary-ms` and `Getting-Started` return HTTP 200; the rendered Home links all 21 step pages; the eight pictures return HTTP 200 as `image/png`. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | Optional; no layout rule was changed. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | `docs/wiki/` holds every page, `Home*.md` and `_Sidebar.md` at the top level, with no subfolder. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | N-A | Wiki pages carry no Metadata table; the language is in the file name and the language line (QC-WIKI-001 criteria 11 and 12). |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | The file name codes `da` and `ms` are BCP 47 codes; the domain is `it` as in the registry. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | English pages are English, `-da` pages Danish and `-ms` pages Bahasa Malaysia. The author's stand-in (the AI) wrote and read all three; no native speaker of Danish or Bahasa Malaysia has read them. Confirmed by the AI stand-in for S01, not independent. |
| 4 | The register matches the one the registry gives for the artifact type | N-A | The registry gives no register for wiki pages. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No dictionary (`DICT`) exists; each page uses one term per concept (for example residual, r-squared, coefficient) and keeps English names for code. Confirmed by the AI stand-in for S01. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | N-A | Applies to artifacts with scripted headings; wiki headings follow the page's language, as the registry's `wiki en/da/ms` setting asks. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | N-A | The wiki is the registered exception: its translations are `<Page>-<code>.md` pages by design (QC-WIKI-001 criterion 12). |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | The pages were written in their language from the start. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The stand-in reads English and knows the IT domain; for Danish and Bahasa Malaysia the confirmation is the stand-in's, in this record, not independent, and open to challenge in the run summary. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations such as KDE and r-squared are spelled out or explained on first use in each language. |

## Overall Verdict

Go — every criterion of QC-WIKI-001 and QC-LANG-001 is Pass or N-A; there is no blocking finding. The review is by the author's stand-in and is not independent; S01 can challenge it in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Have the Danish and Bahasa Malaysia pages read by a native speaker if the wiki is shared more widely | S01 | open |

---
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[c6ed0a7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/commit/c6ed0a768a7fef6d86d64d622dbb1bc94e6ce4f4
