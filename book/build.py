#!/usr/bin/env python3
"""Generate the Verus Request QR Creator book."""
import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "site" / "chapters"
OUT.mkdir(parents=True, exist_ok=True)

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --paper: #f5f5f5; --paper-2: #ececec; --ink: #2d3142; --muted: #4f5d75;
      --accent: #bf4520; --rule: rgba(45,49,66,0.12);
      --sans: 'Geist', system-ui, sans-serif; --serif: 'Instrument Serif', serif;
      --mono: 'Geist Mono', ui-monospace, monospace;
    }}
    html[data-theme="dark"] {{
      --paper: #12141a; --paper-2: #1b1f27; --ink: #e8e6e0; --muted: #98a0ae;
      --accent: #e2663c; --rule: rgba(232,230,224,0.13);
    }}
    .theme-toggle {{
      position: fixed; top: 1rem; right: 1rem; z-index: 30;
      font-family: var(--mono); font-size: 0.62rem; letter-spacing: 0.14em;
      text-transform: uppercase; color: var(--muted);
      background: var(--paper-2); border: 1px solid var(--rule);
      border-radius: 999px; padding: 0.42rem 0.85rem; cursor: pointer;
      transition: color 120ms ease, border-color 120ms ease;
    }}
    .theme-toggle:hover {{ color: var(--ink); border-color: var(--muted); }}
    html[data-theme="dark"] .scroll [fill="#f5f5f5"] {{ fill: #12141a; }}
    html[data-theme="dark"] .scroll [fill="#ffffff"] {{ fill: #1b1f27; }}
    html[data-theme="dark"] .scroll [fill="#2d3142"] {{ fill: #e8e6e0; }}
    html[data-theme="dark"] .scroll [fill="#4f5d75"] {{ fill: #98a0ae; }}
    html[data-theme="dark"] .scroll [fill="#5a6580"] {{ fill: #aab2c0; }}
    html[data-theme="dark"] .scroll [fill="#bf4520"] {{ fill: #e2663c; }}
    html[data-theme="dark"] .scroll [fill="rgba(45,49,66,0.10)"] {{ fill: rgba(232,230,224,0.10); }}
    html[data-theme="dark"] .scroll [fill="rgba(79,93,117,0.03)"] {{ fill: rgba(232,230,224,0.045); }}
    html[data-theme="dark"] .scroll [fill="rgba(191,69,32,0.08)"] {{ fill: rgba(226,102,60,0.16); }}
    html[data-theme="dark"] .scroll [fill="rgba(191,69,32,0.06)"] {{ fill: rgba(226,102,60,0.12); }}
    html[data-theme="dark"] .scroll [stroke="#2d3142"] {{ stroke: #e8e6e0; }}
    html[data-theme="dark"] .scroll [stroke="#4f5d75"] {{ stroke: #98a0ae; }}
    html[data-theme="dark"] .scroll [stroke="#bf4520"] {{ stroke: #e2663c; }}
    html[data-theme="dark"] .scroll [stroke="rgba(45,49,66,0.20)"] {{ stroke: rgba(232,230,224,0.26); }}
    html[data-theme="dark"] .scroll [stroke="rgba(45,49,66,0.18)"] {{ stroke: rgba(232,230,224,0.24); }}
    html[data-theme="dark"] .scroll [stroke="rgba(45,49,66,0.12)"] {{ stroke: rgba(232,230,224,0.17); }}
    html[data-theme="dark"] .scroll svg {{ background: transparent; }}
    body {{ font-family: var(--sans); background: var(--paper); color: var(--ink);
            padding: 4rem 2rem 8rem; line-height: 1.6; }}
    .frame {{ max-width: 1080px; margin: 0 auto; }}
    .eyebrow {{ font-family: var(--mono); font-size: 0.66rem; font-weight: 500;
               letter-spacing: 0.18em; text-transform: uppercase; color: var(--muted);
               margin-bottom: 0.75rem; }}
    h1 {{ font-family: var(--serif); font-size: clamp(2rem, 4vw + 0.5rem, 3.1rem);
          font-weight: 400; letter-spacing: -0.02em; line-height: 1.1; margin-bottom: 1.25rem; }}
    .standfirst {{ font-size: 1.05rem; color: var(--muted); max-width: 62ch; margin-bottom: 3rem; }}
    h2 {{ font-family: var(--serif); font-size: 1.55rem; font-weight: 400;
          letter-spacing: -0.01em; margin: 3.25rem 0 0.9rem; }}
    h2 + p, p + p {{ margin-top: 0.9rem; }}
    p {{ max-width: 68ch; }}
    ul {{ max-width: 68ch; margin: 1rem 0 0 1.1rem; }}
    li {{ margin: 0.35rem 0; }}
    code {{ font-family: var(--mono); font-size: 0.86em; background: var(--paper-2);
            padding: 0.1em 0.35em; border-radius: 3px; }}
    pre {{ font-family: var(--mono); font-size: 0.78rem; line-height: 1.65; background: var(--paper-2);
           border: 1px solid var(--rule); border-radius: 6px; padding: 1.1rem 1.25rem;
           overflow-x: auto; margin: 1.25rem 0; color: var(--ink); }}
    table {{ border-collapse: collapse; width: 100%; margin: 1.25rem 0; font-size: 0.88rem; }}
    th, td {{ text-align: left; padding: 0.55rem 0.75rem; border-bottom: 1px solid var(--rule); vertical-align: top; }}
    th {{ font-family: var(--mono); font-size: 0.66rem; letter-spacing: 0.12em;
          text-transform: uppercase; color: var(--muted); font-weight: 500; }}
    td code {{ font-size: 0.82em; }}
    .scroll {{ overflow-x: auto; }}
    svg {{ width: 100%; min-width: 960px; display: block; }}
    .caption {{ font-family: var(--mono); font-size: 0.68rem; letter-spacing: 0.06em;
                color: var(--muted); margin-top: 1rem; }}
    .callout {{ border-left: 2px solid var(--accent); padding: 0.35rem 0 0.35rem 1.1rem;
                margin: 1.75rem 0; font-family: var(--serif); font-style: italic;
                font-size: 1.05rem; color: var(--ink); max-width: 66ch; }}
    .backlink {{ font-family: var(--mono); font-size: 0.72rem; letter-spacing: 0.1em;
                 text-transform: uppercase; color: var(--muted); text-decoration: none; }}
    .footer {{ margin-top: 4rem; padding-top: 1.5rem; border-top: 1px solid var(--rule); }}
    .next {{ font-size: 0.9rem; color: var(--muted); margin-top: 0.5rem; }}
    .next a {{ color: var(--ink); }}
  </style>
</head>
<body>
  <div class="frame">
    <a class="backlink" href="../">&larr; Book map</a>
    <div style="height:1.75rem"></div>
    <p class="eyebrow">{eyebrow}</p>
    <h1>{heading}</h1>
    <p class="standfirst">{standfirst}</p>
"""

THEME_SNIPPET = "<script>\n(function () {\n  var root = document.documentElement, KEY = 'qrcodes-theme', saved = null;\n  try { saved = localStorage.getItem(KEY); } catch (e) {}\n  root.dataset.theme = saved || 'dark';\n  function paint(btn) {\n    var next = root.dataset.theme === 'dark' ? 'light' : 'dark';\n    btn.textContent = next === 'light' ? 'Light' : 'Dark';\n    btn.setAttribute('aria-label', 'Switch to ' + next + ' mode');\n    btn.setAttribute('title', 'Switch to ' + next + ' mode');\n  }\n  document.addEventListener('DOMContentLoaded', function () {\n    var btn = document.getElementById('theme-toggle');\n    if (!btn) {\n      btn = document.createElement('button');\n      btn.id = 'theme-toggle';\n      btn.className = 'theme-toggle';\n      btn.type = 'button';\n      document.body.appendChild(btn);\n    }\n    paint(btn);\n    btn.addEventListener('click', function () {\n      root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';\n      try { localStorage.setItem(KEY, root.dataset.theme); } catch (e) {}\n      paint(btn);\n    });\n  });\n})();\n</script>\n"

TAIL = """
    <div class="footer">
      <a class="backlink" href="../">&larr; Book map</a>
      <p class="next">{next}</p>
    </div>
  </div>
</body>
</html>
"""


def chapter(slug, title, eyebrow, heading, standfirst, body, next_text):
    html = HEAD.format(title=title, eyebrow=eyebrow, heading=heading, standfirst=standfirst)
    html = html.replace("</head>", THEME_SNIPPET + "</head>")
    html += body + TAIL.format(next=next_text)
    (OUT / slug).write_text(html, encoding="utf-8")
    print("wrote", slug, len(html))


def chips_svg(slug, title_text, desc, rows, note="", cols=3):
    """A card grid of field/flag chips — no connectors, so geometry is trivially safe."""
    w, chip_w, chip_h, gap = 1000, 290, 44, 26
    top = 66
    row_h = chip_h + 18
    height = top + len(rows) * row_h + 54
    xs = [40, 40 + chip_w + gap, 40 + 2 * (chip_w + gap)]
    parts = [f'''    <div class="scroll">
    <svg viewBox="0 0 1000 {height}" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="{slug}-title {slug}-desc">
      <title id="{slug}-title">{title_text}</title>
      <desc id="{slug}-desc">{desc}</desc>
      <defs>
        <pattern id="{slug}-dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="0.9" fill="rgba(45,49,66,0.10)"/></pattern>
      </defs>
      <rect width="100%" height="100%" fill="#f5f5f5"/>
      <rect width="100%" height="100%" fill="url(#{slug}-dots)" opacity="0.55"/>
''']
    for r, row in enumerate(rows):
        y = top + r * row_h
        for c, label in enumerate(row):
            if label is None:
                continue
            x = xs[c]
            parts.append(f'''      <rect x="{x}" y="{y}" width="{chip_w}" height="{chip_h}" rx="6" fill="#ffffff" stroke="#2d3142"/>
      <text x="{x + chip_w/2}" y="{y + 27}" fill="#2d3142" font-size="11" font-family="'Geist',sans-serif" text-anchor="middle">{label}</text>
''')
    if note:
        parts.append(f'''      <text x="40" y="{height - 20}" fill="#4f5d75" font-size="8.5" font-family="'Geist',sans-serif" font-style="italic">{note}</text>
''')
    parts.append("    </svg>\n    </div>\n")
    return "".join(parts)


# ---------------------------------------------------------------- 01
B1 = """
    <div class="scroll">
    <svg viewBox="0 0 1000 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="repo-title repo-desc">
      <title id="repo-title">Repository map</title>
      <desc id="repo-desc">The app splits into a server, an Express route layer with one file per request tab, shared route utilities, EJS views, and tests.</desc>
      <defs>
        <pattern id="repo-dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="0.9" fill="rgba(45,49,66,0.10)"/></pattern>
      </defs>
      <rect width="100%" height="100%" fill="#f5f5f5"/>
      <rect width="100%" height="100%" fill="url(#repo-dots)" opacity="0.55"/>
      <text x="40" y="54" fill="#4f5d75" font-size="8" font-family="'Geist Mono',monospace" letter-spacing="0.14em">ONE ROUTE FILE PER TAB — THAT IS THE WHOLE ARCHITECTURE</text>

      <rect x="60" y="76" width="250" height="56" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="185" y="102" fill="#2d3142" font-size="12" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">src/server.ts</text>
      <text x="185" y="120" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">Express app, RPC helpers</text>

      <rect x="350" y="76" width="250" height="56" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="475" y="102" fill="#2d3142" font-size="12" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">src/routes/utils.ts</text>
      <text x="475" y="120" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">build + sign + encode</text>

      <rect x="640" y="76" width="300" height="56" rx="8" fill="rgba(191,69,32,0.08)" stroke="#bf4520"/>
      <text x="790" y="102" fill="#2d3142" font-size="12" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">src/routes/requests/*.ts</text>
      <text x="790" y="120" fill="#bf4520" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">one file per tab</text>

      <rect x="60" y="176" width="250" height="56" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="185" y="202" fill="#2d3142" font-size="12" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">views/tabs/*.ejs</text>
      <text x="185" y="220" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">forms that POST JSON</text>

      <rect x="350" y="176" width="250" height="56" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="475" y="202" fill="#2d3142" font-size="12" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">config.js</text>
      <text x="475" y="220" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">RPC + service signer</text>

      <rect x="640" y="176" width="300" height="56" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="790" y="202" fill="#2d3142" font-size="12" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">__tests__/*.test.js</text>
      <text x="790" y="220" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">concrete expected outputs</text>

      <rect x="60" y="276" width="880" height="46" rx="6" fill="#ffffff" stroke="rgba(45,49,66,0.18)"/>
      <text x="80" y="304" fill="#4f5d75" font-size="10.5" font-family="'Geist Mono',monospace">verus-typescript-primitives  ·  verusid-ts-client  ·  express  ·  ejs  ·  qrcode</text>
    </svg>
    </div>
    <p class="caption">FIGURE 1.1 · The shape of the codebase.</p>
"""

BODY1 = B1 + """
    <h2>What the app is</h2>
    <p>
      A small Express server with a form per request type. Each form posts JSON to an endpoint; the
      endpoint builds a VDXF request with <code>verus-typescript-primitives</code>, signs it through a
      Verus daemon over RPC using <code>verusid-ts-client</code>, encodes it as a wallet deeplink, renders
      a QR code, and returns both as JSON for the page to display.
    </p>
    <p>
      It is the reference implementation of "how do I actually produce one of these things", which makes it
      the right second book after the primitives: everything here is application code built on that
      library.
    </p>

    <h2>The tab set</h2>
    <table>
      <thead><tr><th>Tab</th><th>Route file</th><th>Endpoint</th></tr></thead>
      <tbody>
        <tr><td>Update Identity</td><td><code>requests/updateIdentity.ts</code></td><td><code>POST /api/generate-qr</code></td></tr>
        <tr><td>Service signer</td><td><code>requests/serviceSigner.ts</code></td><td><code>POST /api/generate-service-signer-qr</code> + callback/status</td></tr>
        <tr><td>Authentication</td><td><code>requests/authentication.ts</code></td><td><code>POST /api/generate-auth-qr</code></td></tr>
        <tr><td>Invoice</td><td><code>requests/invoice.ts</code></td><td><code>POST /api/generate-invoice-qr</code></td></tr>
        <tr><td>App Encryption</td><td><code>requests/encryption.ts</code></td><td><code>POST /api/generate-app-encryption-qr</code></td></tr>
        <tr><td>Data Packet</td><td><code>requests/dataPacket.ts</code></td><td><code>POST /api/generate-data-packet-qr</code></td></tr>
        <tr><td>User Data</td><td><code>requests/userData.ts</code></td><td><code>POST /api/generate-user-data-qr</code></td></tr>
        <tr><td>Attestation</td><td><code>requests/createAttestationTab.ts</code></td><td><code>POST /api/create-attestation-tab</code> + sign + QR</td></tr>
        <tr><td>TX Signing</td><td><code>requests/txSigning.ts</code></td><td><code>POST /api/generate-tx-signing-qr</code></td></tr>
      </tbody>
    </table>

    <h2>Run it</h2>
    <pre>yarn install
# config.js: RPC_HOST, RPC_PORT (18843 = testnet), RPC_USER, RPC_PASSWORD,
#            SERVICE_SIGNER_IADDRESS / SERVICE_SIGNER_WIF for the service signer tab
yarn ui          # Express + EJS UI on :3000
yarn main        # CLI mode: identity update only, prints a terminal QR</pre>
    <p>
      <code>RPC_PORT === 18843</code> is the switch that decides testnet everywhere in the app — not a
      separate flag. That single comparison picks the system id, the identity chain, and the
      <code>FLAG_IS_TESTNET</code> bit.
    </p>

    <h2>How to read this book</h2>
    <p>
      Chapter 2 is the shared half that all nine tabs use. Every later chapter is then short: the tab's
      form fields, the details object it builds, the flags it sets, and the one thing that makes that
      request type different. Chapter 12 puts the whole thing back together.
    </p>
"""

# ---------------------------------------------------------------- 02
B2 = """
    <div class="scroll">
    <svg viewBox="0 0 1000 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="pipe-title pipe-desc">
      <title id="pipe-title">The shared request pipeline</title>
      <desc id="pipe-desc">Form fields are validated, a details object is built and wrapped in a generic request, signed through the daemon, encoded as a deeplink and rendered as a QR code.</desc>
      <defs>
        <pattern id="pipe-dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="0.9" fill="rgba(45,49,66,0.10)"/></pattern>
        <marker id="pipe-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#4f5d75"/></marker>
      </defs>
      <rect width="100%" height="100%" fill="#f5f5f5"/>
      <rect width="100%" height="100%" fill="url(#pipe-dots)" opacity="0.55"/>

      <line x1="228" y1="130" x2="256" y2="130" stroke="#4f5d75" stroke-width="1.2" marker-end="url(#pipe-arrow)"/>
      <line x1="436" y1="130" x2="464" y2="130" stroke="#4f5d75" stroke-width="1.2" marker-end="url(#pipe-arrow)"/>
      <line x1="644" y1="130" x2="672" y2="130" stroke="#4f5d75" stroke-width="1.2" marker-end="url(#pipe-arrow)"/>
      <line x1="852" y1="130" x2="880" y2="130" stroke="#bf4520" stroke-width="1.4" marker-end="url(#pipe-arrow)"/>

      <rect x="40" y="98" width="188" height="64" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="134" y="126" fill="#2d3142" font-size="11.5" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">form JSON</text>
      <text x="134" y="144" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">validated per tab</text>

      <rect x="256" y="98" width="180" height="64" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="346" y="126" fill="#2d3142" font-size="11.5" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">details object</text>
      <text x="346" y="144" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">wrapped in an ordinal</text>

      <rect x="464" y="98" width="180" height="64" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="554" y="126" fill="#2d3142" font-size="11.5" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">GenericRequest</text>
      <text x="554" y="144" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">flags + URIs + stub sig</text>

      <rect x="672" y="98" width="180" height="64" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="762" y="126" fill="#2d3142" font-size="11.5" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">RPC signData</text>
      <text x="762" y="144" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">over the raw hash</text>

      <rect x="880" y="98" width="80" height="64" rx="8" fill="rgba(191,69,32,0.08)" stroke="#bf4520"/>
      <text x="920" y="126" fill="#2d3142" font-size="11" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">QR</text>
      <text x="920" y="144" fill="#bf4520" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">deeplink</text>

      <text x="40" y="212" fill="#4f5d75" font-size="8.5" font-family="'Geist',sans-serif" font-style="italic">buildGenericRequestFromDetails() and signRequest() are the two functions every tab shares.</text>
      <text x="40" y="236" fill="#4f5d75" font-size="8.5" font-family="'Geist',sans-serif" font-style="italic">Everything before step 2 and after step 5 is tab-specific.</text>
    </svg>
    </div>
    <p class="caption">FIGURE 2.1 · The six steps, with the shared ones highlighted.</p>
"""

BODY2 = B2 + """
    <h2>The two functions that matter</h2>
    <p>
      <code>src/routes/utils.ts</code> is 251 lines and contains the entire shared protocol. If you read
      only two functions in this repo, read these.
    </p>

    <h2>buildGenericRequestFromDetails</h2>
    <pre>const req = new primitives.GenericRequest({
  details,                                        // ordinal-wrapped request objects
  createdAt: new BN((Date.now() / 1000).toFixed(0)), // seconds, not ms
  responseURIs,                                   // built from the redirects field
  flags: isTestnet ? FLAG_IS_TESTNET : BASE_FLAGS,
  requestID
});

if (signed) {
  req.signature = new VerifiableSignatureData({ systemID, identityID });
  req.setSigned();
}</pre>
    <p>
      Three details carry weight. <code>createdAt</code> must be seconds — the library serialises it as a
      uint32 and a millisecond value silently truncates. <code>FLAG_IS_TESTNET</code> is passed as the
      <em>initial</em> flags value, not OR'd in later; <code>setIsTestnet()</code> does the OR for you.
      And the signature object is created here but empty — the actual bytes are filled in by
      <code>signRequest</code>.
    </p>

    <h2>buildResponseUris</h2>
    <table>
      <thead><tr><th>Form value</th><th>ResponseURI type</th><th>Wallet behaviour</th></tr></thead>
      <tbody>
        <tr><td><code>"1"</code></td><td><code>TYPE_REDIRECT</code></td><td>Redirect the user back to the URI (browser/deeplink)</td></tr>
        <tr><td><code>"2"</code></td><td><code>TYPE_POST</code></td><td>POST the signed response to the URI</td></tr>
        <tr><td>anything else</td><td>—</td><td>Silently dropped; no URI is added</td></tr>
      </tbody>
    </table>
    <p>
      The silent drop is worth knowing: a typo in the redirect type produces a request with no callback and
      no error, and the UI will happily show a QR that cannot answer.
    </p>

    <h2>signRequest</h2>
    <pre>const rawHash = request.getRawDataSha256(false);        // no signature field
const sigRes  = await verusId.interface.signData({
  address: signingId,
  datahash: rawHash.toString("hex")
});
request.signature.signatureAsVch = Buffer.from(sigRes.result.signature, "base64");</pre>
    <p>
      The daemon signs the hash, not the bytes — the app never sees a private key for this path. The
      <code>false</code> argument to <code>getRawDataSha256</code> is the "exclude signature" switch; passing
      <code>true</code> here produces a signature over a message nobody receives. If signing fails, the error
      message is unusually explicit about the likely cause (the signing identity is not in the wallet), and
      that message is worth preserving rather than replacing with a generic 500.
    </p>

    <h2>Validation helpers</h2>
    <table>
      <thead><tr><th>Helper</th><th>Rule worth remembering</th></tr></thead>
      <tbody>
        <tr><td><code>parseAddress</code></td><td>A string ending in <code>@</code> becomes <code>TYPE_FQN</code>; anything else must pass <code>fromBase58Check</code> and becomes <code>TYPE_I_ADDRESS</code></td></tr>
        <tr><td><code>requireString</code></td><td>Trimmed, non-empty, or <code>ValidationError</code></td></tr>
        <tr><td><code>parseNumber</code> / <code>parseOptionalPositiveNumber</code></td><td>Positive and finite; the optional form floors to an integer (used for heights and expiry)</td></tr>
        <tr><td><code>parseJsonField</code></td><td>Accepts either a JSON string or an object; parse errors surface as validation errors</td></tr>
      </tbody>
    </table>
    <p>
      <code>ValidationError</code> maps to HTTP 400; anything else is a 500 and gets logged. That split is the
      reason the UI can show useful messages without leaking stack traces.
    </p>

    <h2>Where the chain id comes from</h2>
    <pre>RPC_PORT === 18843  →  VRSCTEST
  system id  iJhCezBExJHvtyH3fGhNnt2NhU4Ztkf2yq
otherwise           →  VRSC
  system id  i5w5MuNik5NtLcYmNzcvaoixooEebB6MGV</pre>
    <p>
      <code>getRpcConfig()</code> derives <code>isTestnet</code> from the port, and the signing path repeats
      that comparison rather than passing a flag. It is consistent, but it means a malformed
      <code>RPC_PORT</code> silently lands you on mainnet semantics — check the port first when debugging.
    </p>

    <div class="callout">
      One pipeline, nine callers. If two tabs behave differently in production, the difference is almost
      always in what they pass to these two functions, not in how the functions behave.
    </div>

    <h2>Reading the code</h2>
    <pre>src/routes/utils.ts
├── parseAddress / requireString / parseNumber / parseJsonField
├── parseRedirectsField / buildResponseUris
├── buildGenericRequestFromDetails
├── signRequest
└── getRpcConfig / getServiceSignerConfig</pre>
"""

# ---------------------------------------------------------------- 03
B3 = chips_svg(
    "uid", "Update Identity — what the request carries",
    "The identity update details object carries a partial identity, an optional request id, an expiry height, a system, an optional txid, and sign data.",
    [
        ["requestID", "expiryHeight", "systemID"],
        ["identity (PartialIdentity)", "txid", "signDataMap"],
        ["flags derived from present fields", None, None],
    ],
    "Flags: 1 signData · 2 expires · 4 requestID · 8 system · 16 txid",
) + """
    <p class="caption">FIGURE 3.1 · IdentityUpdateRequestDetails, as used by the simplest tab.</p>
"""

BODY3 = B3 + """
    <h2>The simplest route, and the template for the rest</h2>
    <p>
      <code>updateIdentity.ts</code> is 111 lines: parse three fields, build details, build the request, sign,
      encode, return. It is the one tab with a CLI equivalent (<code>src/index.ts</code>), which makes it the
      best place to see the minimum viable path.
    </p>

    <h2>The details object is built from CLI-shaped JSON</h2>
    <pre>const details = IdentityUpdateRequestDetails.fromCLIJson(
  params.identityChanges,                     // { name, parent, contentmultimap, … }
  params.requestId                            // { requestid: "i…" }
    ? { requestid: CompactIAddressObject.fromAddress(params.requestId).toJson() }
    : undefined
);</pre>
    <p>
      <code>fromCLIJson</code> is the bridge between "the JSON a Verus CLI prints" and the typed details
      object. It accepts snake_case fields, parses the partial identity, and derives the detail flags from
      the fields present. That is why this tab's form takes a JSON blob rather than eight separate inputs —
      it is intentionally a thin skin over the CLI shape.
    </p>
    <pre>{ "name": "mylo",
  "parent": "i…",
  "contentmultimap": { "i…key": ["hex…"] } }</pre>

    <h2>What the wallet does with it</h2>
    <ul>
      <li>Resolves the target identity from <code>name</code> + <code>parent</code>.</li>
      <li>Applies only the fields present in the partial identity — everything else is untouched.</li>
      <li>Checks <code>expiryHeight</code> if the flag is set, and refuses after that height.</li>
      <li>If <code>txid</code> is present, the update must spend that transaction.</li>
      <li>Builds an identity-update transaction and broadcasts it; the QR is only the instruction sheet.</li>
    </ul>

    <div class="callout">
      An identity update request cannot include a content map entry it does not name. "Leave the rest
      alone" is the absence of fields, not a boolean you set.
    </div>

    <h2>Where it goes wrong</h2>
    <table>
      <thead><tr><th>Symptom</th><th>Cause</th></tr></thead>
      <tbody>
        <tr><td>QR scans, wallet says "invalid request"</td><td><code>identityChanges</code> is not an object, or the JSON has snake_case keys the parser rejects</td></tr>
        <tr><td>Update applies but nothing changes</td><td>Partial identity field missing — the bitmask has no bit for it</td></tr>
        <tr><td>Signature error at generation time</td><td>Signing identity not in the daemon's wallet, or wrong chain for the port</td></tr>
      </tbody>
    </table>

    <h2>Reading the code</h2>
    <pre>src/routes/requests/updateIdentity.ts
src/index.ts                        # CLI version of the same flow
src/routes/utils.ts                 # buildGenericRequestFromDetails + signRequest</pre>
"""

# ---------------------------------------------------------------- 04
B4 = chips_svg(
    "svc", "Service signer — the moving parts",
    "A service identity signs an update for a target identity, with a generated request id, an automatic callback redirect, and a status endpoint the browser polls.",
    [
        ["generateRequestId()", "ensureCallbackRedirect()", "getidentity (target)"],
        ["merge name + parent + contentmultimap", "sign with service signer", "callback → txid"],
        ["status polling", "QR of the signed request", None],
    ],
    "The wallet signs nothing here: it only authorises. The service holds the key.",
) + """
    <p class="caption">FIGURE 4.1 · Who does what in the service-signer flow.</p>
"""

BODY4 = B4 + """
    <h2>The inversion</h2>
    <p>
      Every other tab signs with a user identity that lives in the daemon's wallet. The service-signer tab
      signs with a <em>service</em> identity configured on the server
      (<code>SERVICE_SIGNER_IADDRESS</code> / <code>SERVICE_SIGNER_WIF</code>), targets someone else's
      identity, and uses the QR only to get the user's authorisation.
    </p>
    <p>
      That is the model used by provisioning and conversion services: the user authorises by scanning, the
      service performs the update. The request is still a normal
      <code>IdentityUpdateRequestOrdinalVDXFObject</code> — what differs is who signed it and how the answer
      comes back.
    </p>

    <h2>Assembly, step by step</h2>
    <pre>1. requestId = generateRequestId()                       // new i-address-ish id per request
2. redirects = ensureCallbackRedirect(redirects, uri)    // adds type "1" -> /api/service-signer/callback
3. { name, parent } = getidentity(targetIdentity)        // RPC, must resolve
4. merged = { ...identityChanges, name, parent, contentmultimap }
5. details = IdentityUpdateRequestDetails.fromCLIJson(merged, { requestid })
6. request = buildGenericRequestFromDetails({ details, signed: true,
              signingId: SERVICE_SIGNER_IADDRESS, redirects })
7. signRequest(...)  with the service signing id
8. QR / deeplink</pre>
    <p>
      Note step 3: the tab refuses to build a request if the target identity's name and parent cannot be
      resolved. A partial identity that names an identity by something the chain cannot resolve is a request
      the wallet would reject anyway.
    </p>

    <h2>The callback loop</h2>
    <table>
      <thead><tr><th>Endpoint</th><th>Purpose</th></tr></thead>
      <tbody>
        <tr><td><code>GET /api/service-signer/callback?requestId=…</code></td><td>Wallet redirect target; renders a page that then polls status</td></tr>
        <tr><td><code>POST /api/service-signer/callback?requestId=…</code></td><td>Programmatic callback carrying the wallet's response</td></tr>
        <tr><td><code>GET /api/service-signer/status?requestId=…</code></td><td>Poll request state (pending / complete / error)</td></tr>
      </tbody>
    </table>
    <p>
      <code>parseIdentityUpdateResponse</code> extracts the <code>txid</code> from the wallet's response and
      stores it against the request id. The UI polls status until it sees one. This is the only tab with a
      server-side lifecycle — everything else is request/response in a single HTTP call.
    </p>

    <div class="callout">
      If the service-signer QR works but the page never updates, the callback redirect is missing — and
      because <code>buildResponseUris</code> drops unknown types silently, the failure looks like a wallet
      problem rather than a form problem.
    </div>

    <h2>keydefiner.ts</h2>
    <p>
      A 22-line CLI helper: given a VDXF key URI, it constructs a <code>DefinedKey</code>, prints its
      i-address, and emits the identity-update JSON fragment that registers it under
      <code>DATA_TYPE_DEFINEDKEY</code>. It is how you create the key you will then write into a content
      multimap in the update tab.
    </p>

    <h2>Reading the code</h2>
    <pre>src/routes/requests/serviceSigner.ts
├── generateServiceSignerQr     # assembly + QR
├── serviceSignerCallback       # POST from wallet
├── serviceSignerCallbackRedirect # GET redirect + page
├── serviceSignerStatus         # polling
└── fetchTargetIdentityInfo     # getidentity, name + parent
src/keydefiner.ts               # VDXF key → i-address + update JSON</pre>
"""

# ---------------------------------------------------------------- 05
B5 = chips_svg(
    "auth", "Authentication — the constraint menu",
    "An authentication request carries a request id, an optional expiry, and recipient constraints that narrow who may answer.",
    [
        ["requestID", "expiryTime (unix)", "recipientConstraintType"],
        ["REQUIRED_ID = 1", "REQUIRED_SYSTEM = 2", "REQUIRED_PARENT = 3"],
        ["signing identity", "response URIs", None],
    ],
    "Constraint type 2 (system) is what the encryption tab uses to pin the answering chain.",
) + """
    <p class="caption">FIGURE 5.1 · AuthenticationRequestDetails and its three constraint types.</p>
"""

BODY5 = B5 + """
    <h2>What the request asks</h2>
    <p>
      "Prove you control this identity, by signing my challenge." The request itself is small: a request id
      so you can match the answer, an optional expiry so a leaked QR stops working, and optional recipient
      constraints so only a particular identity, system, or parent may answer.
    </p>

    <h2>The route</h2>
    <pre>const details = new AuthenticationRequestDetails({
  requestID: CompactIAddressObject.fromAddress(params.requestId),
  recipientConstraints,                                  // optional, one constraint
  expiryTime: params.expiryTime != null ? new BN(params.expiryTime) : undefined
});
return buildGenericRequestFromDetails({
  details: [new AuthenticationRequestOrdinalVDXFObject({ data: details })],
  signed: true, signingId, redirects
}, isTestnet);</pre>
    <p>
      Constraints are validated against exactly three values — <code>REQUIRED_ID</code> (1),
      <code>REQUIRED_SYSTEM</code> (2), <code>REQUIRED_PARENT</code> (3). Anything else is a 400 with an
      explicit message. The app supports one constraint per request; the primitive supports an array.
    </p>

    <h2>Where the answer goes</h2>
    <p>
      The wallet signs and returns a <code>Response</code> to the configured response URI. There is no
      server-side verification in this tab — the redirect/POST URI is yours to handle, and the app returns it
      in the request exactly as configured.
    </p>

    <h2>Reading the code</h2>
    <pre>src/routes/requests/authentication.ts
  parseRecipientConstraints()   # validates 1/2/3
  buildAuthRequest()
  generateAuthQr()</pre>
"""

# ---------------------------------------------------------------- 06
B6 = chips_svg(
    "inv", "Invoice — the flags decide what the wallet may do",
    "An invoice carries amount, destination, currency, expiry, slippage, accepted systems and a tag, with flags that relax or constrain the payment.",
    [
        ["amount (BN base10)", "destination (PKH or ID)", "requestedCurrencyId"],
        ["expiryHeight", "maxEstimatedSlippage", "acceptedSystems[]"],
        ["acceptsAnyAmount", "acceptsAnyDestination", "acceptsConversion"],
        ["acceptsNonVerusSystems", "expires", "isPreconvert / isTagged"],
    ],
    "Destination is omitted entirely when acceptsAnyDestination is on.",
) + """
    <p class="caption">FIGURE 6.1 · VerusPayInvoiceDetails, as wired by the form.</p>
"""

BODY6 = B6 + """
    <h2>Signed or not — a real choice</h2>
    <p>
      Invoice is the only tab where <code>signed</code> is optional. An unsigned invoice is a payment
      request anyone can read; a signed one proves which identity asked. The route branches on it and only
      calls <code>requireString(payload.signingId)</code> when signing.
    </p>

    <h2>Building the details</h2>
    <pre>destination = acceptsAnyDestination ? undefined :
  new TransferDestination({
    type: destinationType === "id" ? DEST_ID : DEST_PKH,
    destinationBytes: fromBase58Check(address).hash
  });

amount = acceptsAnyAmount ? undefined : new BN(amountString, 10);   // must be > 0

details.setFlags({
  acceptsAnyAmount, acceptsAnyDestination, acceptsConversion,
  expires, acceptsNonVerusSystems, isTestnet, isPreconvert, isTagged
});</pre>
    <p>
      <code>setFlags()</code> is where most invoice bugs live: the field is set from the flags, not the
      other way round. If you pass <code>amount</code> but forget <code>acceptsAnyAmount: false</code> (or the
      reverse), the serialised invoice will disagree with the form.
    </p>

    <h2>Flag meanings worth internalising</h2>
    <table>
      <thead><tr><th>Flag</th><th>What it permits</th></tr></thead>
      <tbody>
        <tr><td><code>acceptsAnyAmount</code></td><td>Payer chooses the amount — no amount field serialised</td></tr>
        <tr><td><code>acceptsAnyDestination</code></td><td>Payer chooses where to send — no destination serialised</td></tr>
        <tr><td><code>acceptsConversion</code></td><td>Payment may be converted through another currency, bounded by slippage</td></tr>
        <tr><td><code>acceptsNonVerusSystems</code></td><td>Payment may route through listed PBaaS systems</td></tr>
        <tr><td><code>expires</code></td><td><code>expiryHeight</code> is enforced</td></tr>
        <tr><td><code>isPreconvert</code></td><td>Pre-conversion semantics</td></tr>
        <tr><td><code>isTagged</code></td><td>An invoice tag identifies the payment</td></tr>
      </tbody>
    </table>

    <div class="callout">
      Two flags are effectively permissions: "any amount" and "any destination". A wallet UI that shows them
      is telling the user they are handing over choice, not just convenience.
    </div>

    <h2>Reading the code</h2>
    <pre>src/routes/requests/invoice.ts
  buildInvoiceRequest()   # destination, amount, flags, accepted systems
  generateInvoiceQr()     # signed branch + QR</pre>
"""

# ---------------------------------------------------------------- 07
B7 = """
    <div class="scroll">
    <svg viewBox="0 0 1000 280" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="enc-title enc-desc">
      <title id="enc-title">Two details, in order</title>
      <desc id="enc-desc">The app encryption request carries an authentication detail first, constrained to the chain, followed by the app encryption detail.</desc>
      <defs>
        <pattern id="enc-dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="0.9" fill="rgba(45,49,66,0.10)"/></pattern>
        <marker id="enc-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#4f5d75"/></marker>
      </defs>
      <rect width="100%" height="100%" fill="#f5f5f5"/>
      <rect width="100%" height="100%" fill="url(#enc-dots)" opacity="0.55"/>
      <text x="40" y="58" fill="#4f5d75" font-size="8" font-family="'Geist Mono',monospace" letter-spacing="0.14em">DETAILS[0] MUST PRECEDE DETAILS[1]</text>

      <line x1="300" y1="136" x2="400" y2="136" stroke="#4f5d75" stroke-width="1.2" marker-end="url(#enc-arrow)"/>
      <line x1="700" y1="136" x2="780" y2="136" stroke="#bf4520" stroke-width="1.4" marker-end="url(#enc-arrow)"/>

      <rect x="100" y="104" width="200" height="64" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="200" y="132" fill="#2d3142" font-size="11.5" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">auth detail</text>
      <text x="200" y="150" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">REQUIRED_SYSTEM</text>

      <rect x="400" y="104" width="300" height="64" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="550" y="132" fill="#2d3142" font-size="11.5" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">app encryption detail</text>
      <text x="550" y="150" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">derivation · z-address · return ESK</text>

      <rect x="780" y="104" width="150" height="64" rx="8" fill="rgba(191,69,32,0.08)" stroke="#bf4520"/>
      <text x="855" y="132" fill="#2d3142" font-size="11.5" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">QR</text>
      <text x="855" y="150" fill="#bf4520" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">verified first</text>

      <text x="40" y="222" fill="#4f5d75" font-size="8.5" font-family="'Geist',sans-serif" font-style="italic">The wallet enforces recipient constraints in the auth detail before it shows the encryption request.</text>
    </svg>
    </div>
    <p class="caption">FIGURE 7.1 · Ordering is semantic, not cosmetic.</p>
"""

BODY7 = B7 + """
    <h2>The only tab that composes two details</h2>
    <p>
      App encryption asks an identity to encrypt data back to a viewing key. The primitive requires an
      authentication detail alongside it, and the code comments say exactly why: the wallet processes the
      auth first, so it can enforce a recipient constraint before presenting the encryption request.
    </p>
    <pre>details: [
  new AuthenticationRequestOrdinalVDXFObject({ data: authDetails }),   // REQUIRED_SYSTEM
  new AppEncryptionRequestOrdinalVDXFObject({ data: appEncryptDetails })
]</pre>
    <p>
      The auth detail's <code>requestID</code> defaults to the signing identity if no request id was given,
      and its constraint is <code>REQUIRED_SYSTEM</code> pinned to VRSC/VRSCTEST. Reordering the array
      produces a request that parses but loses the guard.
    </p>

    <h2>What the encryption detail carries</h2>
    <table>
      <thead><tr><th>Field</th><th>Rule in this app</th></tr></thead>
      <tbody>
        <tr><td><code>encryptResponseToAddress</code></td><td>Must start with <code>zs1</code>; parsed with <code>SaplingPaymentAddress.fromAddressString</code></td></tr>
        <tr><td><code>derivationNumber</code></td><td>Non-negative integer, default 0</td></tr>
        <tr><td><code>derivationID</code></td><td>Optional, i-address or FQN</td></tr>
        <tr><td><code>requestID</code></td><td>Optional; defaults to the signing identity</td></tr>
        <tr><td><code>returnEsk</code></td><td>Boolean; asks the wallet to return the extended spending key</td></tr>
        <tr><td><code>redirects</code></td><td><strong>Required and non-empty</strong> for this tab</td></tr>
      </tbody>
    </table>
    <p>
      The redirect requirement is deliberate: an encryption response with nowhere to go is a dead request.
      The route rejects an empty array rather than emitting one.
    </p>

    <h2>Round-trip verification</h2>
    <pre>const deeplink = reqToSign.toWalletDeeplinkUri();
const back = primitives.GenericRequest.fromWalletDeeplinkUri(deeplink);
const ok = await verusId.verifyGenericRequest(back);
if (!ok) throw new Error("Failed to verify the generated GenericRequest.");</pre>
    <p>
      This is the only tab that verifies its own output before returning it — parse the deeplink back, check
      the signature against the chain, and fail loudly. It is a pattern worth copying: the QR is only useful
      if the round trip preserves the signed bytes.
    </p>

    <div class="callout">
      <code>returnEsk</code> is a capability upgrade, not a checkbox. A returned extended spending key can
      derive every message in that derivation chain; decrypting one response cannot.
    </div>

    <h2>Reading the code</h2>
    <pre>src/routes/requests/encryption.ts
  parseOptionalZAddress / parseDerivationNumber / parseOptionalIAddress
  buildAppEncryptionRequest()   # auth detail + encryption detail
  generateAppEncryptionQr()     # sign → round-trip → verify → QR</pre>
"""

# ---------------------------------------------------------------- 08
B8 = chips_svg(
    "dp", "Data packet — six flags, one payload",
    "Data packet flags decide which optional fields exist: request id, statements, a signature, whether the user signs, whether it is transmitted to the user, and whether a URL is downloaded.",
    [
        ["1 requestID", "2 statements", "4 signature"],
        ["8 for user's signature", "16 transmittal to user", "32 URL download"],
        ["signableObjects: DataDescriptor[]", "recipient auth (optional)", None],
    ],
    "Only one of these flags is not obvious from its name: 16 means 'hand this to the user', not 'send it now'.",
) + """
    <p class="caption">FIGURE 8.1 · DataPacketRequestDetails flags used by this tab.</p>
"""

BODY8 = B8 + """
    <h2>The most general request in the app</h2>
    <p>
      A data packet asks an identity to sign an arbitrary data blob — often a hash of a URL-fetched
      resource. At 748 lines it is the biggest route file, and most of that is validation and descriptor
      assembly rather than request construction.
    </p>

    <h2>Flags are computed, then partially overridden</h2>
    <pre>buildFlags():  requestID | statements | signature
             | forUsersSignature | transmittalToUser | hasUrlForDownload

applyUserControlledFlags(details, flags):
  // calcFlags() in the primitive ignores three of them, so the route re-applies
  forUsersSignature · transmittalToUser · hasUrlForDownload</pre>
    <p>
      That workaround is a real piece of institutional knowledge: the primitive's own flag calculation does
      not derive those three, so a request built only from the constructor can silently lose them. If a data
      packet arrives at the wallet missing flags the form clearly set, this is the line to check.
    </p>

    <h2>URL download mode</h2>
    <p>
      When <code>FLAG_HAS_URL_FOR_DOWNLOAD</code> is set, <code>signableObjects</code> becomes exactly one
      descriptor: a <code>DataDescriptor</code> whose object data is a <code>URLRef</code>, optionally
      carrying a hash (<code>URLRef.FLAG_HAS_HASH</code>). <code>fetchAndHashUrl</code> exists so the UI can
      fill that hash by downloading the resource first — the signature then commits to those exact bytes.
    </p>
    <pre>DataDescriptor.fromJson({
  version: 1,
  flags: …,
  objectdata: new VdxfUniValue({ values: [{ [URLRef.vdxfid]: urlRef }] }).toBuffer()
})</pre>

    <h2>Recipient constraints via a preceding auth detail</h2>
    <p>
      When transmitting to a specific user, the route prepends an
      <code>AuthenticationRequestOrdinalVDXFObject</code> with a recipient constraint — the same ordering
      trick the encryption tab uses. The comment in the code is explicit that the auth must come first so the
      wallet can enforce it before showing the data.
    </p>

    <h2>Required-field rules</h2>
    <table>
      <thead><tr><th>If the flag is set…</th><th>…this field becomes required</th></tr></thead>
      <tbody>
        <tr><td><code>FLAG_HAS_STATEMENTS</code></td><td><code>statements</code> non-empty</td></tr>
        <tr><td><code>FLAG_HAS_REQUEST_ID</code></td><td>A request id</td></tr>
        <tr><td><code>FLAG_HAS_SIGNATURE</code></td><td>A <code>VerifiableSignatureData</code> blob</td></tr>
        <tr><td><code>FLAG_FOR_TRANSMITTAL_TO_USER</code></td><td>A recipient identity</td></tr>
        <tr><td><code>FLAG_HAS_URL_FOR_DOWNLOAD</code></td><td>A download URL (and only the URL descriptor is signed)</td></tr>
      </tbody>
    </table>

    <div class="callout">
      Eight of the nine tabs build one detail. This one builds a variable-length array whose shape depends
      on the flags — which is why its validation is longer than every other route combined.
    </div>

    <h2>Reading the code</h2>
    <pre>src/routes/requests/dataPacket.ts
  buildFlags / applyUserControlledFlags
  parseSignableObjects / buildUrlDataDescriptor
  buildRecipientAuthDetails / buildDataPacketRequest
  generateDataPacketQr / signDataPacket / fetchAndHashUrl</pre>
"""

# ---------------------------------------------------------------- 09
B9 = chips_svg(
    "ud", "User data — ask for named fields",
    "A user data request carries a request id, an optional signer, and requested keys, asking an identity to return specific VDXF-keyed data.",
    [
        ["requestID", "signer", "requestedKeys[]"],
        ["FULL_DATA = 1", "PARTIAL_DATA = 2", "searchDataKey"],
        ["recipient auth (optional)", None, None],
    ],
    "Flags: 1 requestID · 2 signer · 4 requested keys.",
) + """
    <p class="caption">FIGURE 9.1 · UserDataRequestDetails as wired by the form.</p>
"""

BODY9 = B9 + """
    <h2>The request is a query</h2>
    <p>
      Where the data packet asks for a signature on data the requester already has, user data asks the
      identity to <em>return</em> data it holds. The distinction is the flags and the payload: here the
      payload is a list of VDXF keys, not a blob.
    </p>

    <h2>Requested keys and search</h2>
    <pre>const details = new UserDataRequestDetails({
  requestID, signer, requestedKeys, searchDataKey, …
});
// the constructor's setFlags() derives 1/2/4 from the fields present</pre>
    <p>
      <code>buildSearchDataKey(keyAddress, keyValue)</code> produces the
      <code>Array&lt;{[key: string]: string}&gt;</code> form the details object expects, so a request can target
      a specific key/value pair rather than a whole namespace. The form exposes a single key, but the
      primitive takes an array.
    </p>

    <h2>Full or partial</h2>
    <table>
      <thead><tr><th>Mode</th><th>Meaning</th></tr></thead>
      <tbody>
        <tr><td><code>FULL_DATA</code> (1)</td><td>Return complete objects for the requested keys</td></tr>
        <tr><td><code>PARTIAL_DATA</code> (2)</td><td>Return only the named fields</td></tr>
      </tbody>
    </table>
    <p>
      The route builds the details and wraps it with an optional recipient auth detail, exactly like the data
      packet. Response handling is the caller's problem: the request asks, the wallet answers to the
      configured response URI.
    </p>

    <h2>Reading the code</h2>
    <pre>src/routes/requests/userData.ts
  parseRequestedKeys / buildSearchDataKey
  buildRecipientAuthDetails / buildUserDataRequest
  generateUserDataQr
__tests__/userData.test.js        # concrete expected output</pre>
"""

# ---------------------------------------------------------------- 10
B10 = """
    <div class="scroll">
    <svg viewBox="0 0 1000 340" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="att-title att-desc">
      <title id="att-title">How an attestation is assembled</title>
      <desc id="att-desc">signdata with createmmr returns an MMR descriptor and signature data, which are packed into a VdxfUniValue, wrapped in a labelled DataDescriptor, hashed, and then sent as a data packet request.</desc>
      <defs>
        <pattern id="att-dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="0.9" fill="rgba(45,49,66,0.10)"/></pattern>
        <marker id="att-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#4f5d75"/></marker>
      </defs>
      <rect width="100%" height="100%" fill="#f5f5f5"/>
      <rect width="100%" height="100%" fill="url(#att-dots)" opacity="0.55"/>
      <text x="40" y="56" fill="#4f5d75" font-size="8" font-family="'Geist Mono',monospace" letter-spacing="0.14em">TWO RPC CALLS, THREE WRAPPERS</text>

      <line x1="258" y1="118" x2="296" y2="118" stroke="#4f5d75" stroke-width="1.2" marker-end="url(#att-arrow)"/>
      <line x1="518" y1="118" x2="556" y2="118" stroke="#4f5d75" stroke-width="1.2" marker-end="url(#att-arrow)"/>
      <line x1="778" y1="118" x2="816" y2="118" stroke="#4f5d75" stroke-width="1.2" marker-end="url(#att-arrow)"/>
      <line x1="640" y1="152" x2="640" y2="196" stroke="#4f5d75" stroke-width="1.2" marker-end="url(#att-arrow)"/>
      <line x1="640" y1="252" x2="640" y2="286" stroke="#bf4520" stroke-width="1.4" marker-end="url(#att-arrow)"/>

      <rect x="60" y="86" width="198" height="64" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="159" y="114" fill="#2d3142" font-size="11" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">mmrdata[]</text>
      <text x="159" y="132" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">label · mimetype · message</text>

      <rect x="296" y="86" width="222" height="64" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="407" y="114" fill="#2d3142" font-size="11" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">signdata (createmmr)</text>
      <text x="407" y="132" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">RPC, encrypttoaddress</text>

      <rect x="556" y="86" width="222" height="64" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="667" y="114" fill="#2d3142" font-size="11" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">MMRDescriptor + SignatureData</text>
      <text x="667" y="132" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">inside a VdxfUniValue</text>

      <rect x="816" y="86" width="140" height="64" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="886" y="114" fill="#2d3142" font-size="11" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">DataDescriptor</text>
      <text x="886" y="132" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">label + objectdata</text>

      <rect x="420" y="196" width="280" height="56" rx="8" fill="#ffffff" stroke="#2d3142"/>
      <text x="560" y="220" fill="#2d3142" font-size="11" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">hex + sha256</text>
      <text x="560" y="238" fill="#5a6580" font-size="8" font-family="'Geist Mono',monospace" text-anchor="middle">pastebin payload</text>

      <rect x="420" y="286" width="280" height="34" rx="8" fill="rgba(191,69,32,0.08)" stroke="#bf4520"/>
      <text x="560" y="308" fill="#2d3142" font-size="11" font-weight="600" font-family="'Geist',sans-serif" text-anchor="middle">data packet request → QR</text>
    </svg>
    </div>
    <p class="caption">FIGURE 10.1 · Attestation is a data packet with a two-call prologue.</p>
"""

BODY10 = B10 + """
    <h2>Attestation is not a request type</h2>
    <p>
      There is no <code>AttestationRequestOrdinalVDXFObject</code>. An attestation tab produces a
      <strong>data packet</strong> whose signable object is a <code>DataDescriptor</code> containing a
      signed MMR payload. Once you see that, the 493 lines become approachable: half is building the
      descriptor, half is reusing the data-packet flow.
    </p>

    <h2>Step 1 — ask the daemon to sign the data</h2>
    <pre>const sigRes = await verusId.interface.request({
  cmd: "signdata",
  getParams: () => [{
    address: signingId,
    createmmr: true,
    encrypttoaddress: encryptToAddress,
    mmrdata: mmrdata.map(e => ({ flags: e.flags ?? 0, label: e.label,
                                 mimetype: e.mimetype || "text/plain",
                                 message: e.message }))
  }]
});</pre>
    <p>
      The response contains <code>mmrdescriptor</code> and <code>signaturedata</code>. Those are parsed back
      into typed objects (<code>MMRDescriptor.fromJson</code>, <code>SignatureData.fromJson</code>) rather
      than passed through as opaque JSON — that is what lets them be re-serialised deterministically.
    </p>

    <h2>Step 2 — pack them into a VdxfUniValue</h2>
    <pre>const innerUniValue = new VdxfUniValue({ values: [
  { [MMRDescriptorKey.vdxfid]: mmr },
  { [SignatureDataKey.vdxfid]: signaturedataObj }
]});</pre>
    <p>
      A VdxfUniValue is the library's "tagged union" container: each entry is keyed by its VDXF id so a
      reader knows what the payload is without being told. This is the same structure a content multimap
      value uses.
    </p>

    <h2>Step 3 — wrap in a labelled DataDescriptor</h2>
    <pre>const containingDataDescriptor = new DataDescriptor({
  version: new BN(1), flags: new BN(0),
  label: attestationLabel,          // what the attestation is about
  objectdata: innerUniValue.toBuffer()
});
const pastebinHex  = containingDataDescriptor.toBuffer().toString("hex");
const pastebinHash = sha256(Buffer.from(pastebinHex, "hex")).toString("hex");</pre>
    <p>
      The label is the attestation's subject; the hash is what the eventual data packet should commit to.
      The tab returns <code>pastebinHex</code>, <code>pastebinHash</code>, <code>pastebinJson</code> and the
      raw signdata result, because the UI may need to upload the hex somewhere the URL descriptor can point
      at.
    </p>

    <h2>Step 4 — send it as a data packet</h2>
    <p>
      <code>signAttestationPacket</code> and <code>generateAttestationQr</code> build a
      <code>DataPacketRequestDetails</code> with the attestation flags:
    </p>
    <pre>FLAG_HAS_REQUEST_ID | FLAG_FOR_TRANSMITTAL_TO_USER | FLAG_HAS_URL_FOR_DOWNLOAD</pre>
    <p>
      Note <code>FLAG_HAS_URL_FOR_DOWNLOAD</code>: the attestation payload is expected to be reachable at a
      URL whose hash matches the descriptor. The request commits to both the URL and the hash, which is what
      makes the attestation verifiable later.
    </p>

    <div class="callout">
      The interesting failure mode is a hash mismatch: if the pastebin hex changes after the descriptor is
      built, the data packet still points at the old hash and the attestation silently fails to verify.
      Rebuild the descriptor, not just the upload.
    </div>

    <h2>Reading the code</h2>
    <pre>src/routes/requests/createAttestationTab.ts
  buildUrlDataDescriptor / parseSignableObjects / parseSignature
  getAttestationFlags / applyUserControlledFlags
  createAttestationForTab      # signdata → MMRDescriptor + SignatureData
  signAttestationPacket        # sign the packet
  generateAttestationQr        # final request
__tests__/dataPacket.test.js   # descriptor shapes</pre>
"""

# ---------------------------------------------------------------- 11
B11 = chips_svg(
    "txs", "Transaction signing — one general-purpose detail",
    "Instead of a typed details class, the transaction signing request carries a JSON payload in a general-purpose VDXF object keyed by a text key.",
    [
        ["type: tx-signing-template", "chain: VRSCTEST / VRSC", "hextx"],
        ["outputtotalsSats", "feeSats", "createdAt aligned to chain time"],
        ["optional signature", "verify before return", "QR"],
    ],
    "No dedicated Details class — the payload is JSON inside a GeneralTypeOrdinalVDXFObject.",
) + """
    <p class="caption">FIGURE 11.1 · The newest tab takes a different approach.</p>
"""

BODY11 = B11 + """
    <h2>Why this tab is different</h2>
    <p>
      Every other tab has a purpose-built details class in the primitives library. Transaction signing does
      not: it sends a JSON payload describing a pre-built transaction, inside a general-purpose VDXF object
      keyed by a text key. That is the escape hatch the library provides for request types it does not model
      yet.
    </p>
    <pre>new GeneralTypeOrdinalVDXFObject({
  type: VDXF_OBJECT_RESERVED_BYTE_VDXF_ID_STRING,
  key: TX_SIGNING_TEMPLATE_VDXF_TEXT_KEY,
  data: Buffer.from(JSON.stringify({
    type: "tx-signing-template",
    chain: isTestnet ? "VRSCTEST" : "VRSC",
    signed, signingId,
    hextx,
    outputtotalsSats, feeSats
  }), "utf-8")
})</pre>

    <h2>The details that show real care</h2>
    <ul>
      <li><strong>Amounts never touch floats.</strong> <code>parseFixedPointToSats</code> rejects scientific
        notation, requires at most eight decimals, and does the arithmetic in <code>bigint</code>.</li>
      <li><strong>The hex is validated before it is embedded.</strong> Even length, hex characters only —
        a malformed transaction is a 400, not a QR that fails at the wallet.</li>
      <li><strong>createdAt is aligned to chain time.</strong> <code>alignCreatedAtToChainTime</code> asks for
        the current height, fetches the block, and uses the block's timestamp — so a request generated on a
        machine with a drifting clock is still inside the wallet's validity window.</li>
      <li><strong>The signature is applied conditionally.</strong> <code>applyOptionalSignature</code> and
        <code>verifySignedRequestSignature</code> let the tab return either an unsigned template or a
        verified signed request.</li>
    </ul>

    <h2>What the payload promises</h2>
    <table>
      <thead><tr><th>Field</th><th>Meaning</th></tr></thead>
      <tbody>
        <tr><td><code>hextx</code></td><td>The exact transaction to sign</td></tr>
        <tr><td><code>outputtotalsSats</code></td><td>Per-destination totals the wallet should verify against the transaction</td></tr>
        <tr><td><code>feeSats</code></td><td>Declared fee, so the wallet can refuse a mismatch</td></tr>
        <tr><td><code>chain</code></td><td>Which network the transaction belongs to</td></tr>
      </tbody>
    </table>

    <div class="callout">
      General-purpose objects are how you ship a request type before the library models it. The cost is that
      nothing validates your JSON but your own code — which is why this file is 329 lines for one payload.
    </div>

    <h2>Reading the code</h2>
    <pre>src/routes/requests/txSigning.ts
  parseFixedPointToSats / parseHexTransaction / parseOutputTotals
  buildTxSigningRequest / alignCreatedAtToChainTime
  verifySignedRequestSignature / applyOptionalSignature
  generateTxSigningQr</pre>
"""

# ---------------------------------------------------------------- 12
B12 = chips_svg(
    "syn", "The nine tabs at a glance",
    "Each tab is a details class plus a set of flags; the pipeline underneath is identical.",
    [
        ["Update Identity → IdentityUpdate", "Service Signer → IdentityUpdate", "Authentication → Auth"],
        ["Invoice → VerusPayInvoice", "App Encryption → Auth + AppEncryption", "Data Packet → DataPacket"],
        ["User Data → UserData", "Attestation → DataPacket + MMR", "TX Signing → GeneralType"],
    ],
    "Nine tabs, five distinct request primitives, one pipeline.",
) + """
    <p class="caption">FIGURE 12.1 · The whole app in one grid.</p>
"""

BODY12 = B12 + """
    <h2>The mental model</h2>
    <p>
      Every tab does the same four things: validate input, build a details object, wrap it in a
      <code>GenericRequest</code>, sign and encode. What differs is only <em>which</em> details object and
      <em>which</em> flags — and, in two cases, that more than one detail is needed.
    </p>

    <h2>A working sketch for a new tab</h2>
    <pre>// routes/requests/myThing.ts
import { MyThingRequestDetails, MyThingRequestOrdinalVDXFObject } from "verus-typescript-primitives";
import { buildGenericRequestFromDetails, signRequest, getRpcConfig,
         requireString, parseRedirectsField } from "../utils";

export async function generateMyThingQr(req, res) {
  try {
    const signingId = requireString(req.body.signingId, "signingId");
    const redirects = parseRedirectsField(req.body.redirects);
    const { rpcHost, rpcPort, rpcUser, rpcPassword, isTestnet } = getRpcConfig();

    const details = new MyThingRequestDetails({ /* form fields */ });

    const request = buildGenericRequestFromDetails({
      details: [new MyThingRequestOrdinalVDXFObject({ data: details })],
      signed: true, signingId, redirects
    }, isTestnet);

    await signRequest({ request, rpcHost, rpcPort, rpcUser, rpcPassword, signingId });

    const deeplink = request.toWalletDeeplinkUri();
    res.json({ deeplink, qrDataUrl: await QRCode.toDataURL(deeplink) });
  } catch (e) {
    res.status(e.name === "ValidationError" ? 400 : 500).json({ error: e.message });
  }
}</pre>
    <p>
      Then mount it in <code>server.ts</code> and add a form view. That is genuinely the whole recipe; the
      rest of each route file is validation and the odd workaround.
    </p>

    <h2>The five lessons worth carrying</h2>
    <ul>
      <li><strong>Sign the bytes you send.</strong> <code>getRawDataSha256(false)</code> before
        <code>signatureAsVch</code> is set, every time.</li>
      <li><strong>Ordering is semantic.</strong> Auth details go first when a constraint must be enforced.</li>
      <li><strong>Flags are the API.</strong> A request's meaning lives in its flag bits; set them from the
        fields, never the other way round.</li>
      <li><strong>Silent drops are the enemy.</strong> Unknown redirect types and ignored flags produce
        requests that look fine and fail later — validate in the route.</li>
      <li><strong>Round-trip when it matters.</strong> The encryption tab parses its own deeplink back and
        verifies the signature; nothing else does, and that is why it is the one that never ships a broken QR.</li>
    </ul>

    <div class="callout">
      If you can describe a tab as "a details class plus flags, fed through two shared functions", you can
      build it in an afternoon.
    </div>

    <h2>Where to go next</h2>
    <pre>the primitives book   → for the byte-level meaning of each details class
src/routes/utils.ts   → the shared pipeline, read end to end
__tests__/            → concrete expected outputs per tab
docs/                 → per-tab manual test notes and design plans</pre>
"""

chapter("01-orientation.html", "Chapter 01 · Orientation · A QR factory for Verus requests",
        "Chapter 01 · Foundations", "A QR factory for Verus requests",
        "Nine tabs, one pipeline: validate a form, build a VDXF request, sign it through the daemon, encode "
        "it as a deeplink, render a QR.",
        BODY1, "Next — <a href=\"02-shared-pipeline.html\">Chapter 02 · The shared pipeline</a>")

chapter("02-shared-pipeline.html", "Chapter 02 · The shared pipeline · Two functions, nine callers",
        "Chapter 02 · Foundations", "Two functions, nine callers",
        "<code>buildGenericRequestFromDetails</code> and <code>signRequest</code> do all the work that is not "
        "tab-specific. Everything else in the app is validation and flag-setting.",
        BODY2, "Next — <a href=\"03-update-identity.html\">Chapter 03 · Update Identity</a>")

chapter("03-update-identity.html", "Chapter 03 · Update Identity · The minimal path",
        "Chapter 03 · Tabs", "The minimal path",
        "One details object built from CLI-shaped JSON, one signature, one QR. Read this tab first; it is the "
        "template the other eight follow.",
        BODY3, "Next — <a href=\"04-service-signer.html\">Chapter 04 · Service signer</a>")

chapter("04-service-signer.html", "Chapter 04 · Service signer · When the service signs, not the user",
        "Chapter 04 · Tabs", "When the service signs, not the user",
        "The only tab with a server-side lifecycle: a generated request id, an automatic callback, a status "
        "endpoint, and a service identity holding the key.",
        BODY4, "Next — <a href=\"05-authentication.html\">Chapter 05 · Authentication</a>")

chapter("05-authentication.html", "Chapter 05 · Authentication · Prove control, constrain the answer",
        "Chapter 05 · Tabs", "Prove control, constrain the answer",
        "The smallest request in the app, and the one that introduces constraints: who may answer, and until when.",
        BODY5, "Next — <a href=\"06-invoice.html\">Chapter 06 · Invoice</a>")

chapter("06-invoice.html", "Chapter 06 · Invoice · Flags are the payment policy",
        "Chapter 06 · Tabs", "Flags are the payment policy",
        "An invoice is not just an amount. It is a set of permissions — any amount, any destination, "
        "conversion, routing — encoded as flags.",
        BODY6, "Next — <a href=\"07-app-encryption.html\">Chapter 07 · App Encryption</a>")

chapter("07-app-encryption.html", "Chapter 07 · App Encryption · Two details, in order",
        "Chapter 07 · Tabs", "Two details, in order",
        "The only tab that composes an auth detail with its request, and the only one that verifies its own QR "
        "by round-tripping the deeplink.",
        BODY7, "Next — <a href=\"08-data-packet.html\">Chapter 08 · Data Packet</a>")

chapter("08-data-packet.html", "Chapter 08 · Data Packet · Six flags, one payload",
        "Chapter 08 · Tabs", "Six flags, one payload",
        "The most general request type, and the one where the flags genuinely change the shape of the details "
        "object — six optional fields, plus a known workaround.",
        BODY8, "Next — <a href=\"09-user-data.html\">Chapter 09 · User Data</a>")

chapter("09-user-data.html", "Chapter 09 · User Data · Ask for named fields",
        "Chapter 09 · Tabs", "Ask for named fields",
        "A query rather than a signature request: a list of VDXF keys, an optional signer, and a full/partial "
        "data mode.",
        BODY9, "Next — <a href=\"10-attestation.html\">Chapter 10 · Attestation</a>")

chapter("10-attestation.html", "Chapter 10 · Attestation · A data packet with a prologue",
        "Chapter 10 · Tabs", "A data packet with a prologue",
        "Two RPC calls, three wrappers: signdata produces an MMR descriptor and a signature, which become a "
        "VdxfUniValue inside a labelled DataDescriptor, then a data packet.",
        BODY10, "Next — <a href=\"11-tx-signing.html\">Chapter 11 · Transaction signing</a>")

chapter("11-tx-signing.html", "Chapter 11 · Transaction signing · The escape hatch",
        "Chapter 11 · Tabs", "The escape hatch",
        "No typed details class — a JSON payload in a general-purpose VDXF object, with chain-time alignment "
        "and bigint arithmetic instead of floats.",
        BODY11, "Next — <a href=\"12-synthesis.html\">Chapter 12 · Synthesis</a>")

chapter("12-synthesis.html", "Chapter 12 · Synthesis · Nine tabs, one recipe",
        "Chapter 12 · Synthesis", "Nine tabs, one recipe",
        "Validate, build a details object, wrap, sign, encode. If you can say that sentence with the right "
        "details class and flags, you can add a tab.",
        BODY12, "End of book. Back to the <a href=\"../\">book map</a>.")
