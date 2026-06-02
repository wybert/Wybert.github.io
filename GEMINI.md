# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal academic portfolio website for Xiaokang Fu (https://wybert.github.io/), built with Jekyll using the Moonwalk theme. The site showcases research, publications, teaching, and services.

## Development Commands

```bash
# Install dependencies (run once after cloning)
bundle config set --local path 'vendor/bundle'
bundle install
# On Apple Silicon: arch -arm64 bundle install

# Start development server with live reload
bundle exec jekyll serve --livereload
# Server runs at http://127.0.0.1:4000
# Note: Do NOT use --incremental flag as it may cause caching issues

# Build the site
bundle exec jekyll build
```

If _config.yml changes don't appear, delete the `_site` folder and restart the server.

## Architecture

### Content Structure
- `_config.yml` - Site configuration, theme settings, and metadata
- `_data/home.yml` - Navigation (navbar, footer) and homepage project cards
- `_data/research.yml` - Research project data
- `*.md` (root) - Static pages: about.md, publications.md, teaching.md, services.md, contact.md
- `_posts/` - Blog posts (format: `YYYY-MM-DD-title.md`)

### Theme System (Moonwalk)
- Remote theme from `abhinavs/moonwalk`
- `_layouts/` - Page templates: home.html, post.html, blog.html, card.html
- `_includes/` - Reusable components (navbar, footer, cards, theme toggle)
- `_sass/` - SCSS stylesheets with CSS variables for light/dark mode
- `assets/` - Static files (CSS, JS, images)

### Key Configuration Options in _config.yml
- `theme_config.appearance` - "light", "dark", or "auto"
- `theme_config.show_*` - Toggle visibility of navbar, footer, projects, blog
- Dependencies defined in `moonwalk.gemspec`

## Personal Bio / Research Interests

The personal introduction appears in **5 locations** (NOT auto-generated, must update manually):

| File | Purpose | Notes |
|------|---------|-------|
| `_includes/profile_header.html` | **Main display** (homepage) | ✅ Primary - update this first |
| `about.md` | About page | ⚠️ Hidden - navigation commented out in `_data/home.yml` |
| `_config.yml` | SEO description | Used by search engines |
| `_layouts/home.html` | Meta description | Also for SEO |
| `Clean_Academic_CV/*.tex` | CV | Independent LaTeX file |

**Current status**: About page navigation is disabled:
```yaml
# _data/home.yml
# - title: About
#   url: about
```

When updating bio/research interests, sync across all files manually.

**⚠️ IMPORTANT**: Always check and update ALL 5 files when modifying personal info or research interests. Do NOT assume changes propagate automatically.

### Chinese Version
The Chinese introduction appears in **4 locations**:

| File | Purpose | Notes |
|------|---------|-------|
| `_includes/profile_header_cn.html` | **Main display** (homepage) | ✅ Primary - update this first |
| `cn/index.md` | Chinese homepage meta | For SEO |
| `cn/researches.md` | Research page meta | For SEO |
| `Clean_Academic_CV/XiaokangFu-CV-cn.tex` | Chinese CV | Independent LaTeX file |

**⚠️ IMPORTANT**: When updating personal info, update BOTH English (5 files) AND Chinese (4 files) versions.

## CV and Publications Workflow

### File Structure
- `Clean_Academic_CV/ref.bib` - **Source** bibliography file (for CV)
- `_bibliography/publications.bib` - **Target** bibliography file (for Jekyll website)
- `bin/update_bib.py` - Script to sync and clean bibliography

### Automated Sync (GitHub Actions)
When you push to master, GitHub Actions automatically:
1. Runs `python3 bin/update_bib.py`
2. Cleans LaTeX formatting (removes `\textbf{}`, `\textit{}`, `$`, etc.)
3. Copies `Clean_Academic_CV/ref.bib` → `_bibliography/publications.bib`
4. Builds Jekyll site and deploys to GitHub Pages

### Local Development
After updating `Clean_Academic_CV/ref.bib`, manually sync for local testing:
```bash
python3 bin/update_bib.py
```

### CV Compilation
Compile CV in `Clean_Academic_CV/` directory:
```bash
# English version
latexmk -xelatex XiaokangFu-CV.tex

# Chinese version
latexmk -xelatex XiaokangFu-CV-cn.tex
```

Note: Uses XeLaTeX (not pdfLaTeX) because of fontspec requirement.

## Deployment

Site deploys automatically to GitHub Pages when pushed to master branch.
