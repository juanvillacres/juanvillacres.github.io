# Juan Villacrés · Research portfolio

An original Hugo website with a neutral grey/blue visual system, a compact academic profile sidebar, editorial research lists, grouped publications, and progressive enhancement. No theme submodule, package manager, external JavaScript or third-party font download is required. Existing teaching resources remain available at their original paths.

## Quick start (macOS)

Install Hugo Extended and confirm the version:

```sh
brew install hugo
hugo version
```

The project targets Hugo Extended 0.125+; the deployment workflow pins 0.147.2, the version in the uploaded project's previous workflow. Use that version if you want exact parity with deployment. Compatibility with every intervening release has not been verified.

From this repository root:

```sh
hugo server --disableFastRender
```

Open `http://localhost:1313/`. The server reloads whenever source files change. Use `hugo server -D` only when you intentionally want to preview drafts.

## Production build and validation

```sh
hugo --gc --minify --cleanDestinationDir
python3 scripts/legacy_routes.py public
python3 scripts/check_site.py public
```

`public/` is disposable output, not the source. If you are upgrading an existing checkout, remove its old generated `public/` directory before building to ensure retired pages are not left behind. The checker verifies generated internal links (including fragments and static assets), key routes, basic HTML metadata and teaching PDF bytes. The uppercase legacy redirects are generated only on a case-sensitive filesystem (as in GitHub Actions); on default macOS filesystems the equivalent paths resolve without duplicates.

## Edit your website

| File | What to update |
|---|---|
| `data/profile.yaml` | Name, headline, affiliation, location, email and social links |
| `data/research.yaml` | Research themes and their corresponding publication topics |
| `data/experience.yaml` | Academic/professional appointments |
| `data/skills.yaml` | Research methods and technical expertise |
| `data/publications.yaml` | Publications, authors, venue, year, topic and featured flag |
| `data/projects.yaml` | Project entries, tags, paper links and optional GitHub/demo URLs |
| `content/projects/` | Detailed case studies |
| `content/posts/` | News and research writing |
| `content/courses/` | Academic periods and course descriptions |
| `static/courses/` | Teaching PDFs (match their course directory) |
| `assets/images/portrait.webp` | Optimized profile portrait |
| `static/picture.jpeg` | Original portrait and social sharing image |
| `assets/css/tokens.css` | Light and dark palette, typography and design tokens |
| `hugo.yaml` | Site metadata, menu and Hugo configuration |

The archive section and unused template routes have been removed. Older course PDFs and their historical links are deliberately preserved.

The site uses the operating-system font stack with Inter and JetBrains Mono as preferred locally installed fonts. This avoids external font requests. The portrait is served in WebP on the homepage; the original JPEG is retained for old links and sharing metadata.

### Add publications

Copy an existing entry in `data/publications.yaml`. The expected fields are `title`, `authors`, `year` (integer), `venue`, `type` (`Journal`, `Conference`, or `Book chapter`), `topic` (`Control`, `Perception`, `Agriculture`, or `Sensing`), `url` and `featured` (boolean). Publications are automatically sorted and grouped by year. Set `featured: false` for items not shown on the homepage. The publication filter and count are generated from this data, not hard-coded. Year, type and topic filter options are derived from the data automatically. Add a research theme if appropriate. The copy button copies a plain-text citation; verify incomplete author lists and bibliographic details before citing formally.

### Add a case study

```sh
hugo new content projects/new-case-study.md
```

Write the case study in Markdown and change `draft: true` to `draft: false` when ready. Add a corresponding item to `data/projects.yaml` with `slug: new-case-study`, title, summary, year, tags, kind, diagram (`yield`, `control`, or `vision`), and optional verified `paper`, `github`, or `demo` URLs. The template links to the actual Markdown page via Hugo's page lookup. Keep the entry's title and the Markdown title aligned. The diagrams are conceptual illustrations, not experimental plots.

### Add news or blog writing

```sh
hugo new content posts/new-article.md
```

Edit the title, date, description, body and optional `dateLabel`; publish by removing `draft: true` or setting it to false. The newest three posts automatically appear on the homepage. Use `dateLabel` when only a month or date range is known.

For an optional thumbnail on `/posts/`, place a photo in `static/images/news/` and add these fields to the post's existing YAML front matter:

```yaml
image: images/news/my-photo.jpg
imageAlt: Descriptive alternative text for the photograph.
```

Use paths relative to `static/` (do not include `static/` in the URL). A 3:2 landscape image, ideally around 960 × 640 pixels, works best; other aspect ratios are cropped to fit the thumbnail. Use compressed WebP or JPEG for photographs. If `image` is omitted or empty, no image or reserved image space is rendered. `imageAlt` may be empty for a purely decorative image. Thumbnails appear on the news index only; use Markdown image syntax inside the article body to display a full-size photo there. The semiconductor manufacturing training post includes a red SVG explicitly labeled “Sample image” for demonstration; replace its `image` and `imageAlt` when a real photograph is ready.


### Add a course

Create `content/courses/<period>/_index.md` and `content/courses/<period>/<course>/_index.md`. Each needs a title in YAML front matter. Use a smaller `weight` on the newest period to show it first. Place PDFs in `static/courses/<period>/<course>/` and link to them using relative Markdown links. Keep existing PDF names and paths to avoid breaking student bookmarks. When a course is primarily Spanish, use `languageCode: es` in front matter.

## Replace your existing GitHub repository safely

Read `MIGRATION.md` before merging. Extract this ZIP outside the current checkout. In the existing repository, first back up any local changes and commit the current source (if needed); then create a branch:

```sh
git status
git switch -c redesign
```

From the existing repository root, set `NEW` to the extracted replacement directory. Dry-run the synchronization first. The trailing slash copies the new repository's contents, not its enclosing directory. It excludes the existing `.git` so commit history survives. `--delete` intentionally removes obsolete PaperMod files, old configuration and old workflows; review the dry-run output carefully before proceeding.

```sh
NEW="$HOME/Downloads/juanvillacres-portfolio-blue"
rsync -avn --delete --exclude='.git' --exclude='public/' --exclude='resources/' "$NEW/" ./
# Only after reviewing the dry run:
rsync -av --delete --exclude='.git' --exclude='public/' --exclude='resources/' "$NEW/" ./
```

Build and review locally, then run:

```sh
git add -A
git commit -m "Refine academic portfolio with grey and blue editorial layout"
git push -u origin redesign
```

Open a pull request into `main`; the workflow builds and validates it. In GitHub **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source. Merge only after the build check succeeds. A push to `main` builds, validates, uploads and deploys the site. No generated files or new Git submodules need to be committed. The existing Pages environment may require approval if you configured deployment protection rules.

## Checks and limitations

See `VALIDATION.md`. This revision was source-checked and its templates, design and JavaScript tested in a Chromium fixture, but a real Hugo build and Lighthouse audit must still be run. No Lighthouse score is claimed. The included CI job gates deployment on the real build and internal-link checks. External publisher links were not exhaustively tested.
