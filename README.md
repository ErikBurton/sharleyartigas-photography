# Sharley Artigas Photography — Website (MVP)

A single-page portfolio site: static HTML/CSS/JS, no build step, no database — built to host free on GitHub Pages.

## What's in here

```
index.html          → all page content
css/styles.css       → all styling
js/main.js           → mobile nav, lightbox, scroll reveal
images/              → photos (currently placeholders — see below)
scripts/             → optional Python helpers (not needed to run the site)
.nojekyll            → tells GitHub Pages not to run Jekyll on this
```

## 1. Replace the placeholder images

Right now `images/` contains 11 generated placeholder photos so you can preview the
layout. Drop in Sharley's real photos using these **exact filenames** so nothing
else needs to change:

| Filename            | Used for                          |
|----------------------|------------------------------------|
| `hero.jpg`           | Big top-of-page image (wide, e.g. 1920×1080 or wider) |
| `about.jpg`          | Photo of Sharley in the About section (portrait orientation works best) |
| `01-lifestyle.jpg`   | Portfolio grid, frame 1 |
| `02-lifestyle.jpg`   | Portfolio grid, frame 2 |
| `03-lifestyle.jpg`   | Portfolio grid, frame 3 |
| `04-family.jpg`      | Portfolio grid, frame 4 |
| `05-family.jpg`      | Portfolio grid, frame 5 |
| `06-family.jpg`      | Portfolio grid, frame 6 |
| `07-portrait.jpg`    | Portfolio grid, frame 7 |
| `08-portrait.jpg`    | Portfolio grid, frame 8 |
| `09-portrait.jpg`    | Portfolio grid, frame 9 |

Just overwrite the placeholder file with the real one, same name. Any image roughly
900px+ on the short edge will look sharp; don't upload huge multi-MB camera originals
directly — see the optional optimizer script below.

**Want a different photo order or category split?** Open `index.html`, find the
`<section class="contact-sheet">` block, and reorder/edit the `<figure>` blocks —
each one is self-contained (image + number + category label).

### Optional: auto-resize/compress real photos first

If Sharley's camera exports are large (multi-MB), you can shrink them for the
web without losing visible quality:

```bash
pip install Pillow --break-system-packages
python3 scripts/optimize_images.py /path/to/folder/of/raw/photos
```

This saves web-sized copies into `images/optimized/`. Rename/move those into
`images/` using the filenames from the table above.

## 2. Edit text content

Everything else (tagline, bio, categories, email) lives directly in `index.html` —
just open it in any text editor and edit the text between tags. Nothing needs
to be rebuilt or compiled.

A couple of spots worth personalizing further:
- **Tagline** — in the `<section class="hero">` block, `<p class="hero__tagline">`
- **Bio** — in the `<section id="about">` block, `<p class="about__text">`
- **Email** — search for `artigassharley@gmail.com` (appears once, in the Contact section's `mailto:` link)

## 3. Deploy to GitHub Pages

GitHub repo names can't contain spaces, so use a kebab-case name like
`sharleyartigas-photography` for the repo — you can still set the *display title*
(shown in the browser tab) to whatever you like in `index.html`'s `<title>` tag,
which is already set to "Sharley Artigas Photography."

Steps:

1. Create a new GitHub repo, e.g. `sharleyartigas-photography` (public).
2. Upload all files in this folder to the repo (drag-and-drop on github.com works,
   or via git — see below).
3. In the repo, go to **Settings → Pages**.
4. Under "Build and deployment," set **Source: Deploy from a branch**, branch
   `main`, folder `/ (root)`. Save.
5. GitHub gives you a live URL within a minute or two, like:
   `https://<your-username>.github.io/sharleyartigas-photography/`

### Using git from the command line instead

```bash
cd sharleyartigas-photography   # the folder you downloaded
git init
git add .
git commit -m "Initial site"
git branch -M main
git remote add origin https://github.com/<your-username>/sharleyartigas-photography.git
git push -u origin main
```

Then follow step 3–5 above.

## 4. Custom domain (later, once purchased)

In **Settings → Pages → Custom domain**, enter the domain and save — GitHub will
create a `CNAME` file in the repo automatically. Then add the DNS records your
domain registrar's instructions specify (usually a CNAME or A records pointing
at GitHub's servers). GitHub's own docs walk through this once you're at that step:
https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

## Notes on what's intentionally NOT in the MVP

- **No contact form / database** — the Contact section is a `mailto:` link, since
  GitHub Pages only serves static files (no backend to receive form submissions
  without a third-party service). If you want a real form later, Formspree
  (free tier, no backend needed) is the easiest add.
- **No Instagram/social links yet** — add them in the Contact section
  (`<section id="contact">`) whenever Sharley has handles to share.
- **No blog/pricing pages yet** — intentionally scoped out of the MVP; easy to
  add as new sections or pages once the site's live and Sharley wants to expand it.
