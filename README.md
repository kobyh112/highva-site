# highva.app

The public website for Highva: home page, Privacy Policy, Terms of Use and Support.
Plain HTML and CSS (no framework), hosted on GitHub Pages.

This repository holds **only the website**. The app's code lives in a separate private
repository, and nothing secret belongs here.

## Editing

- Home and Support: `content/home.html`, `content/support.html`
- Privacy Policy and Terms of Use: `content/privacy.md`, `content/terms.md`
  (text in `[square brackets]` is a placeholder to fill in)
- Look: `assets/style.css`

Then rebuild the pages and commit:

```bash
python3 build.py
```
