# qrcodes-book

The **qr-creator book** — how Verus QR / deeplink requests are built, signed and
verified, told tab by tab against the running app.

    live  https://qrcodesbook.vrsctest.buildwithdreams.com
    app   https://qrcodes.vrsctest.buildwithdreams.com   (what the book describes)

Public repo. The book itself (12 chapters + map) is generated; only
`site/index.html` and `book/build.py` are hand-authored.

## Layout

    site/
      index.html          the book map  (hand-written)
      chapters/*.html     GENERATED — do not hand-edit
    book/
      build.py            the generator: all chapter content lives here
    deploy/
      inventory.ini       `bwd` host alias; ansible runs from w3k1
      group_vars/production.yml
      84-site-mount.yml   bind-mount site/ into the shared Caddy container
      85-site-caddy-route.yml  Caddy file_server route(s) + validate + reload

## Regenerating the book

    python3 book/build.py            # writes site/chapters/*.html (12 files)

Edit **`book/build.py`**, never `site/chapters/`. Check a regeneration didn't
change anything unexpected (`git diff --stat site/chapters/`) before publishing.

## Theme

Dark is the default. The pill button top-right toggles light/dark; the choice
persists in `localStorage` under `qrcodes-theme`. An inline pre-paint script sets
`data-theme` on `<html>` before first paint (no flash); with JS off the light
palette in `:root` is the fallback.

    :root                     light palette (fallback)
    html[data-theme="dark"]   dark palette overrides

The book keeps its Instrument Serif display face — only the palette, the toggle
and the figure re-theming are themed. Inline SVG figures are light-authored and
re-coloured in dark mode by CSS attribute selectors over the SVG *presentation*
attributes:

    html[data-theme="dark"] .scroll [fill="#ffffff"] { fill: #1b1f27; }

A new colour in a figure needs a matching entry in `SVG_DARK`
(`book/build.py`) or it renders dark-on-dark.

## Publishing (content change)

`site/` is bind-mounted read-only into the shared Caddy container, so ordinary
content edits need **no** playbook and **no** Caddy reload:

    rsync -az --delete ~/qrcodes-book/site/ bwd:/home/dream-hermes-agent/qrcodesbook-site/site/

## Publishing (infra change)

Only when the mount or the domain list changes. Export the Let's Encrypt contact
first — it is not committed (the playbooks read `CADDY_LE_EMAIL`):

    export CADDY_LE_EMAIL=you@example.com

84 recreates the Caddy container (~3 s downtime for every bwd site), so it is
first-time-only:

    cd ~/qrcodes-book
    ansible-playbook -i deploy/inventory.ini deploy/84-site-mount.yml
    ansible-playbook -i deploy/inventory.ini deploy/85-site-caddy-route.yml

## Going live on a new domain

1. DNS: **A record → the bwd host's public IP** (the SSH alias `bwd` in
   `deploy/inventory.ini`; ask an operator for the address). No apex CNAME —
   Namecheap BasicDNS has no ALIAS/ANAME.
2. Add the name to `site_domains` in `deploy/group_vars/production.yml`.
3. Run `deploy/85-site-caddy-route.yml`; Caddy issues the cert on demand once
   DNS resolves.
4. Verify: `curl -sI https://<domain>/` and
   `echo | openssl s_client -connect <domain>:443 -servername <domain> 2>/dev/null | openssl x509 -noout -subject -dates`

## Source

The book was written from `verus-identity-update-qr-creator-main` and the
`VerusCoin/verus-typescript-primitives` request classes. The generator's chapter
bodies cite file paths and flags as they were at writing time — re-read the
source before trusting a specific line.
