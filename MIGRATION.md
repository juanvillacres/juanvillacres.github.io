# Migration notes

The uploaded source archive, rather than its generated `public/` or `docs/` output, was the primary content source. The reference website was used for high-level research-first information architecture only; its code and layout were not copied.

## Preserved

- 21 bibliographic records from `content/papers/_index.md`, structured in `data/publications.yaml`.
- Six substantive news entries from 2024–2026, migrated to individual Markdown pages (the two related AGRICONTROL updates on August 27 were combined into one post).
- All three academic periods and four course entries, including bilingual Intelligent Control content and the Spanish exam/solution notes and student attributions.
- All 14 source teaching PDFs, byte-for-byte unchanged, at their lowercase source paths; the original portrait; favicon assets were rebuilt for the new palette.
- Existing `/papers/`, `/courses/` paths and original course PDF URLs. Hugo aliases cover `/publications/`, `/teaching/`, `/news/` and `/blog/`. The workflow also restores historical uppercase 2025B/ACE routes and copies the PDFs into those legacy paths on Linux.
- Original license notice.

## Updated

- Three papers mentioned in the existing 2026 news were added to the bibliography, giving 24 listed records. Part II was published online in 2026 and assigned to the January 2027 issue; the venue field explicitly distinguishes these dates. The two yield-mapping author lists are abbreviated with “et al.”; confirm complete citation metadata if desired.
- Verified the incorrect multi-camera publication link (previously duplicated the 2023 tracking paper): https://doi.org/10.1016/j.compag.2024.109164.
- Replaced the `example.com` link for the IECON 2024 plant-phenotyping paper with https://doi.org/10.1109/IECON55916.2024.10905108. Kept the conference year in the source bibliography.
- New publication metadata checked against https://doi.org/10.1016/j.biosystemseng.2026.104591, https://doi.org/10.1016/j.biosystemseng.2026.104605 and https://doi.org/10.1109/CoDIT70676.2026.11630768. Remaining publisher links and bibliographic metadata have not been exhaustively verified.
- Corrected the 2026B course period text, which previously read 2025B; sorted periods newest first.
- Wrote a concise research positioning statement and organized research into three themes inferred from the supplied publications. Three case studies summarize published research and use conceptual diagrams, not experimental data or claims of unpublished results. Research labels and expertise are editorial classifications, not verified personal preferences.
- Removed the template's office/location pages referring to a fictional professor at Regensburg; the unused old routes have been retired. No office schedule was invented. The December 2024 “ABC Conference” entry was not republished because it appears to be an unsubstantiated template remnant. The 2026 news no longer makes the unverified journal-quartile claim. Generic sample books, datasets, courses and fictional publication pages found only in generated output were not migrated.
- The profile uses the original April 2025 appointment news and supplied email and social links. It does not infer other positions, degrees, citation metrics, ORCID, GitHub project repositories or demos. No CV was included in the source; no CV page or download link has been fabricated.
- English remains the primary interface language; course content is retained in its original language. Date precision is shown in `dateLabel`; month-only dates use the first day for ordering, not as a claimed publication date.
- System font fallbacks were chosen instead of bundling or requesting external fonts. Blue is reserved for emphasis, links, actionable elements and research graphics. Dark mode follows the OS initially and persists a manual choice using localStorage where available.

## Before merging

Check the profile wording, appointment date and affiliation, abbreviated author lists and the selected research classification. Add a current CV, more experience, or verified project links when ready. Check whether any retired generated-only URLs were real content you want to restore. The local repository's Git history is not included in this replacement ZIP; follow README instructions to preserve your existing history.

## Second design revision

The homepage now uses a compact profile rail with experience, a text-led introduction, research interests and selected publications, followed by recent updates, projects and teaching. Nicole Paul’s academic content hierarchy inspired this revision; no external HTML, CSS or layout code was copied. Grey and blue replace the previous green palette. Publications are grouped by year, and empty groups hide when filters are applied. The archive, obsolete location/office-hours aliases, unreferenced favicon variants, commented-out course links, unused numbered research labels and generated taxonomy pages were removed. All published teaching resources and the compatibility script for historical course PDF URLs remain intentionally preserved.
