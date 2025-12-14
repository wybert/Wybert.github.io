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

## Deployment

Site deploys automatically to GitHub Pages when pushed to master branch.
