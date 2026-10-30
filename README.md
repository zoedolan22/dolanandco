# Dolan & Co

The website for Zoë Dolan, Digital Marketing Strategist, Western Cape, South Africa.

Live site: https://zoedolan22.github.io/dolanandco/

Plain HTML, CSS and a little JavaScript. There is no build step and nothing to install. Open `index.html` in a browser, or serve the folder with any static host.

## What is in here

| Path | What it is |
| --- | --- |
| `index.html` | Home |
| `capabilities.html` | The six capabilities |
| `work.html` | All six projects |
| `herotel-business.html`, `hid-global.html` | Case studies |
| `about.html` | About Zoë |
| `blog.html` | Blog archive (empty for now) |
| `contact.html` | Contact form and details |
| `404.html` | Page not found |
| `tokens.css` | The Dolan & Co design system: colours, type, spacing, radius |
| `site.css` | Layout and components |
| `site.js` | Theme toggle, mobile menu, contact form, blog filters |
| `fonts/`, `images/` | Fonts and campaign images |
| `tools/build.py` | Optional page generator (see below) |

## Adding a blog post

1. Add the cover image to `images/blog/`.
2. Create the post page, for example `blog/my-first-post.html`, by copying `about.html` and replacing the content.
3. Open `blog.html`, find the commented card template inside `<div class="posts" data-posts>`, copy it out of the comment and fill it in.

The "explore all" filters build themselves from each card's `data-category`, and the empty state hides as soon as there is one post. Add the new page to `sitemap.xml` too.

## Changing the header, footer or navigation

Every page shares the same header, footer and badge. They are written once in `tools/build.py`. Edit it, then run:

```
python3 tools/build.py
```

This rewrites all nine pages plus `sitemap.xml`, `robots.txt` and `favicon.svg`. If you would rather edit the HTML files by hand, that works too, but then do not run the script afterwards or it will overwrite your changes.

## Things to know

- **Contact form.** It posts to FormSubmit. The first time anyone submits it, FormSubmit emails zoedolan22@gmail.com an activation link. Click it once and the form works from then on.
- **Moving to a custom domain or Vercel.** The site uses relative links, so it works at any address. Three places mention the GitHub Pages address and should be updated to the new one:
  - `SITE` at the top of `tools/build.py` (canonical links, social preview images, sitemap, the "see what AI has to say" prompt), then rerun the script.
  - `<base href="/dolanandco/">` in `404.html` (set it to `/` on a domain root).
  - `robots.txt` and `sitemap.xml`, which the script regenerates.
- **Vercel.** Import this repository, choose "Other" as the framework, leave the build command empty and the output directory as the repository root.
- **Light and dark.** The site follows the visitor's system setting and has a toggle in the header. The choice is remembered in the browser.
- **Images.** All work shown is the property of Cheymaxim Brand & Digital.
