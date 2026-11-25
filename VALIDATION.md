# Validation status — grey and blue revision

## Completed in the authoring environment

- Parsed all 22 Go HTML templates using the standard Go HTML template parser with a stub function map for Hugo-specific functions. This is not a real Hugo compilation.
- Rendered the homepage and publication partials using the actual templates with a lightweight fixture for Hugo data and page functions. Tested their CSS and JavaScript in Chromium at 320, 390, 520, 680, 768, 900, 1000 and 1440 CSS pixels: no horizontal overflow.
- Tested theme switching, mobile navigation and Escape, year/type/topic/keyword filtering, reset, empty-result messaging and hiding empty publication-year groups. No uncaught JavaScript errors in the fixture tests.
- Parsed YAML configuration/data and all Markdown front matter; verified 24 publication records and the complete removal of the archive source page and archive navigation links.
- Verified all 14 teaching PDFs byte-for-byte against the original uploaded repository, and confirmed all active Markdown PDF links resolve to source static files. Unused commented links were removed.
- Checked JavaScript syntax and compiled the Python validation scripts. Reviewed screenshots of the new design.

## Pending on a real Hugo build

Hugo Extended is not installed in this environment, and external release downloads could not be resolved. The screenshots are from the template-based Chromium fixture, not a production Hugo build. Local HTTP navigation was blocked by the browser environment; localStorage persistence across reloads, URL query filtering, clipboard permissions, Hugo-generated routes and a formal accessibility/Lighthouse audit remain unverified here. No Lighthouse score is claimed. Existing external publication links were not re-audited exhaustively.

Run the actual build and internal-link validation commands in README. The GitHub Actions workflow runs the real Hugo build and link/PDF checks before deployment and rejects an archive route if one is produced. Start with a clean generated `public/` directory to prevent stale output from earlier builds. Use Chrome DevTools Lighthouse on the built/deployed site; 95+ is the target, not a measured result.

## Optional news thumbnails update

- Parsed the modified list template and new news-card partial using Go's HTML template parser with Hugo function stubs. Rendered the six existing news cards with the actual partial.
- Chromium fixture checks passed at 320, 390, 520, 768, 900, 1080 and 1440 CSS pixels in both light and dark modes. Confirmed one loaded demonstration thumbnail, five text-only cards and no horizontal overflow. The fixture used the SVG bytes as a data URI because file navigation is blocked; deployed image URLs and actual Hugo compilation still require local or CI verification.
- The thumbnail is deliberately a red sample, not a photograph of the training event. Only the news listing is modified.
