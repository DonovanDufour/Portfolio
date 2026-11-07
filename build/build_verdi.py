"""Builds the Verdi Markt weekly-offers email in French and Dutch from one
template, so both language versions always share the same markup."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "emails")

COPY = {
    "fr": {
        "file": "verdi-promos-fr.html",
        "title": "Verdi Markt · Promos de la semaine",
        "preheader": "Pommes Jonagold à 1,99 €, café, fromage et pain : vos offres du 12 au 18 novembre.",
        "view_online": "Voir dans le navigateur",
        "other_lang": "Nederlandstalige versie",
        "other_href": "verdi-promos-nl.html",
        "eyebrow": "Du 12 au 18 novembre",
        "issue": "Folder · semaine 46",
        "h1": "La fraîcheur de saison, à petit prix",
        "intro": "Cette semaine, nos producteurs belges remplissent les étals. Profitez de nos meilleures offres en magasin et en ligne.",
        "hero_alt": "Une caisse en bois remplie de pommes et d’oranges, à côté d’un panier de légumes verts",
        "cta": "Voir toutes les promos",
        "products": [
            ("verdi-apples.jpg", "Pommes Jonagold, sachet de 1,5 kg posé sur une nappe", "Pommes Jonagold", "Belgique · 1,5 kg", "1,99 €", "2,79 €", "−28 %"),
            ("verdi-coffee.jpg", "Paquet de café en grains brun foncé", "Café en grains bio", "Pérou · 500 g", "5,49 €", "6,99 €", "−21 %"),
            ("verdi-cheese.jpg", "Part de fromage jaune à trous", "Fromage d’abbaye", "Wallonie · 350 g", "3,89 €", "4,59 €", "−15 %"),
            ("verdi-bread.jpg", "Pain au levain doré avec des entailles", "Pain au levain", "Cuit sur place · 800 g", "2,49 €", "2,99 €", "−17 %"),
        ],
        "was": "au lieu de",
        "add": "Ajouter",
        "card_title": "Votre carte Verdi+",
        "card_body": "Vous avez <strong>1 240 points</strong>. Encore 260 points et vous recevez un bon de 5 € à valoir en magasin.",
        "card_cta": "Mes avantages",
        "store_title": "Votre magasin : Verdi Markt Ixelles",
        "store_body": "Ouvert du lundi au samedi, 8 h – 20 h · Dimanche 9 h – 13 h",
        "store_cta": "Changer de magasin",
        "footer_why": "Vous recevez cet e-mail car vous êtes inscrit·e à la newsletter Verdi Markt.",
        "unsub": "Se désinscrire",
        "prefs": "Gérer mes préférences",
        "legal": "Projet de démonstration · Verdi Markt est une marque fictive. Offres valables dans la limite des stocks disponibles.",
        "footnote": "Prix TVA comprise.",
    },
    "nl": {
        "file": "verdi-promos-nl.html",
        "title": "Verdi Markt · Promoties van de week",
        "preheader": "Jonagold appels aan € 1,99, koffie, kaas en brood: jouw aanbiedingen van 12 tot 18 november.",
        "view_online": "Bekijk in je browser",
        "other_lang": "Version française",
        "other_href": "verdi-promos-fr.html",
        "eyebrow": "Van 12 tot 18 november",
        "issue": "Folder · week 46",
        "h1": "Vers van het seizoen, voor een kleine prijs",
        "intro": "Deze week vullen onze Belgische producenten de rekken. Profiteer van onze beste aanbiedingen in de winkel en online.",
        "hero_alt": "Een houten kist vol appels en sinaasappels, naast een mand met groene groenten",
        "cta": "Bekijk alle promoties",
        "products": [
            ("verdi-apples.jpg", "Zak Jonagold appels van 1,5 kg op een tafelkleed", "Jonagold appels", "België · 1,5 kg", "€ 1,99", "€ 2,79", "−28%"),
            ("verdi-coffee.jpg", "Donkerbruin pak koffiebonen", "Bio koffiebonen", "Peru · 500 g", "€ 5,49", "€ 6,99", "−21%"),
            ("verdi-cheese.jpg", "Stuk gele kaas met gaten", "Abdijkaas", "Wallonië · 350 g", "€ 3,89", "€ 4,59", "−15%"),
            ("verdi-bread.jpg", "Goudbruin zuurdesembrood met insnijdingen", "Zuurdesembrood", "Vers gebakken · 800 g", "€ 2,49", "€ 2,99", "−17%"),
        ],
        "was": "in plaats van",
        "add": "Toevoegen",
        "card_title": "Jouw Verdi+ kaart",
        "card_body": "Je hebt <strong>1 240 punten</strong>. Nog 260 punten en je krijgt een bon van € 5 voor in de winkel.",
        "card_cta": "Mijn voordelen",
        "store_title": "Jouw winkel: Verdi Markt Elsene",
        "store_body": "Open van maandag tot zaterdag, 8 – 20 u · Zondag 9 – 13 u",
        "store_cta": "Andere winkel kiezen",
        "footer_why": "Je ontvangt deze e-mail omdat je ingeschreven bent op de nieuwsbrief van Verdi Markt.",
        "unsub": "Uitschrijven",
        "prefs": "Voorkeuren beheren",
        "legal": "Demoproject · Verdi Markt is een fictief merk. Aanbiedingen geldig zolang de voorraad strekt.",
        "footnote": "Prijzen inclusief btw.",
    },
}

# Brand colours
PAGE = "#EEF3EE"
CARD = "#FFFFFF"
INK = "#14281D"
MUTED = "#4C6155"
GREEN = "#165C3E"
GREEN_D = "#0F4A31"
PRICE = "#C2372B"  # 5.2:1 on white
TINT = "#E6F0E8"
LINE = "#D5E2D8"

FONT = "'Nunito Sans', 'Segoe UI', Helvetica, Arial, sans-serif"


def button(href, label, width=240, bg=GREEN, fg="#FFFFFF"):
    """Bulletproof button: VML roundrect for Outlook desktop, padded link elsewhere."""
    return f"""<!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{href}" style="height:48px;v-text-anchor:middle;width:{width}px;" arcsize="50%" stroke="f" fillcolor="{bg}">
<w:anchorlock/>
<center style="color:{fg};font-family:Arial,sans-serif;font-size:16px;font-weight:bold;">{label}</center>
</v:roundrect>
<![endif]-->
<!--[if !mso]><!-->
<a href="{href}" class="btn dm-btn" style="display:inline-block;background-color:{bg};color:{fg};font-family:{FONT};font-size:16px;font-weight:700;line-height:48px;text-align:center;text-decoration:none;border-radius:24px;padding:0 28px;-webkit-text-size-adjust:none;mso-hide:all;">{label}</a>
<!--<![endif]-->"""


def product(p, c):
    img, alt, name, origin, price, old, badge = p
    return f"""<div class="col" style="display:inline-block;width:100%;max-width:290px;vertical-align:top;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
<tr><td style="padding:10px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="dm-card" style="background-color:{CARD};border:1px solid {LINE};border-radius:12px;">
<tr><td style="padding:0;">
<img src="img/{img}" width="268" alt="{alt}" style="width:100%;max-width:268px;height:auto;border-radius:11px 11px 0 0;background-color:{TINT};font-family:{FONT};font-size:14px;color:{MUTED};">
</td></tr>
<tr><td style="padding:16px 18px 18px 18px;font-family:{FONT};text-align:left;">
<span class="dm-badge" style="display:inline-block;background-color:{PRICE};color:#FFFFFF;font-size:12px;font-weight:800;line-height:22px;padding:0 8px;border-radius:4px;">{badge}</span>
<h3 class="dm-text" style="margin:10px 0 2px 0;font-size:18px;line-height:24px;font-weight:800;color:{INK};">{name}</h3>
<p class="dm-muted" style="margin:0 0 12px 0;font-size:14px;line-height:20px;color:{MUTED};">{origin}</p>
<p style="margin:0;font-size:14px;line-height:20px;color:{MUTED};" class="dm-muted"><span class="dm-price" style="font-size:24px;line-height:28px;font-weight:800;color:{PRICE};">{price}</span>&nbsp; {c["was"]} <s>{old}</s></p>
</td></tr>
</table>
</td></tr>
</table>
</div>"""


def row(a, b, c):
    return f"""<tr><td class="cols-wrap" style="padding:0 10px;font-size:0;text-align:center;">
<!--[if mso]><table role="presentation" width="580" cellpadding="0" cellspacing="0" border="0"><tr><td width="290" valign="top"><![endif]-->
{product(a, c)}
<!--[if mso]></td><td width="290" valign="top"><![endif]-->
{product(b, c)}
<!--[if mso]></td></tr></table><![endif]-->
</td></tr>"""


DARK = {
    ".dm-page": "background-color:#0E1712!important;",
    ".dm-shell": "background-color:#14211A!important;",
    ".dm-card": "background-color:#1B2A22!important;border-color:#2C4136!important;",
    ".dm-tint": "background-color:#1D3328!important;",
    ".dm-text": "color:#EAF2EC!important;",
    ".dm-muted": "color:#AFC3B6!important;",
    ".dm-price": "color:#FF8A7A!important;",
    ".dm-link": "color:#8FD6AE!important;",
    ".dm-logo": "color:#EAF2EC!important;",
    ".dm-btn": "background-color:#2E8A5E!important;",
}


def dark_css():
    media = "\n".join(f"  {k}{{{v}}}" for k, v in DARK.items())
    # Outlook.com / Outlook apps rewrite dark mode with [data-ogsc]/[data-ogsb]
    ogs = "\n".join(
        f"[data-ogs{'b' if 'background' in v else 'c'}] {k}{{{v}}}" for k, v in DARK.items()
    )
    return f"@media (prefers-color-scheme: dark) {{\n{media}\n}}\n{ogs}"


def build(lang):
    c = COPY[lang]
    p = c["products"]
    html = f"""<!DOCTYPE html>
<html lang="{lang}-BE" dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="x-apple-disable-message-reformatting">
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no, url=no">
<meta name="color-scheme" content="light dark">
<meta name="supported-color-schemes" content="light dark">
<title>{c["title"]}</title>
<!--[if mso]>
<noscript><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript>
<style>td,th,div,p,a,h1,h2,h3,span{{font-family:Arial,sans-serif;mso-line-height-rule:exactly;}}</style>
<![endif]-->
<!--[if !mso]><!-->
<link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;700;800&display=swap" rel="stylesheet">
<!--<![endif]-->
<style>
:root{{color-scheme:light dark;supported-color-schemes:light dark;}}
body{{margin:0;padding:0;width:100%;word-spacing:normal;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;}}
table,td{{mso-table-lspace:0pt;mso-table-rspace:0pt;}}
img{{border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;display:block;}}
a[x-apple-data-detectors]{{color:inherit!important;text-decoration:none!important;font-size:inherit!important;font-family:inherit!important;font-weight:inherit!important;line-height:inherit!important;}}
u + #body a{{color:inherit;text-decoration:none;font-size:inherit;font-family:inherit;font-weight:inherit;line-height:inherit;}}
#MessageViewBody a{{color:inherit;text-decoration:none;font-size:inherit;font-family:inherit;font-weight:inherit;line-height:inherit;}}
.btn:hover{{background-color:{GREEN_D}!important;}}
@media screen and (max-width:620px){{
  .px{{padding-left:20px!important;padding-right:20px!important;}}
  .h1{{font-size:30px!important;line-height:36px!important;}}
  .col{{max-width:100%!important;}}
  .stack{{display:block!important;width:100%!important;text-align:left!important;}}
  .stack-gap{{padding-top:16px!important;}}
  .hide-sm{{display:none!important;}}
}}
{dark_css()}
</style>
</head>
<body id="body" class="dm-page" style="margin:0;padding:0;word-spacing:normal;background-color:{PAGE};">
<div role="article" aria-roledescription="email" aria-label="{c["title"]}" lang="{lang}-BE" dir="ltr" class="dm-page" style="font-size:16px;font-size:1rem;background-color:{PAGE};">
<!-- Preheader: shown in the inbox list, hidden in the body -->
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:{PAGE};opacity:0;">{c["preheader"]}{"&#8199;&#65279;&#847; " * 30}</div>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="dm-page" style="background-color:{PAGE};">
<tr><td align="center" style="padding:0;">

<!--[if mso]><table role="presentation" width="600" align="center" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->
<div style="max-width:600px;margin:0 auto;">

<!-- Top links -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
<tr><td class="px" style="padding:16px 30px;font-family:{FONT};font-size:13px;line-height:18px;color:{MUTED};text-align:center;" >
<a href="#" class="dm-muted" style="color:{MUTED};text-decoration:underline;">{c["view_online"]}</a> &nbsp;·&nbsp; <a href="{c["other_href"]}" class="dm-muted" lang="{"nl" if lang == "fr" else "fr"}" style="color:{MUTED};text-decoration:underline;">{c["other_lang"]}</a>
</td></tr>
</table>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="dm-shell" style="background-color:{CARD};border-radius:16px;">

<!-- Header / live-text logo (still readable with images off) -->
<tr><td class="px" style="padding:26px 30px 6px 30px;font-family:{FONT};">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td style="font-size:26px;line-height:30px;font-weight:800;color:{GREEN};letter-spacing:-0.5px;" class="dm-logo">verdi<span style="color:{PRICE};" class="dm-price">●</span>markt</td>
<td align="right" class="hide-sm" style="font-size:13px;line-height:18px;color:{MUTED};" ><span class="dm-muted">{c["issue"]}</span></td>
</tr></table>
</td></tr>

<!-- Hero -->
<tr><td class="px" style="padding:22px 30px 0 30px;font-family:{FONT};text-align:left;">
<p class="dm-price" style="margin:0 0 8px 0;font-size:13px;line-height:18px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:{PRICE};">{c["eyebrow"]}</p>
<h1 class="h1 dm-text" style="margin:0 0 12px 0;font-size:36px;line-height:42px;font-weight:800;color:{INK};">{c["h1"]}</h1>
<p class="dm-muted" style="margin:0 0 22px 0;font-size:17px;line-height:26px;color:{MUTED};">{c["intro"]}</p>
{button("#", c["cta"], width=260)}
</td></tr>
<tr><td style="padding:26px 0 8px 0;">
<img src="img/verdi-hero.jpg" width="600" alt="{c["hero_alt"]}" style="width:100%;max-width:600px;height:auto;background-color:{TINT};font-family:{FONT};font-size:14px;color:{MUTED};">
</td></tr>

<!-- Product grid: hybrid columns, stack without media queries -->
<tr><td style="padding:10px 0 0 0;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
{row(p[0], p[1], c)}
{row(p[2], p[3], c)}
</table>
</td></tr>
<tr><td class="px" style="padding:4px 30px 0 30px;font-family:{FONT};font-size:12px;line-height:18px;color:{MUTED};" ><span class="dm-muted">{c["footnote"]}</span></td></tr>

<!-- Loyalty card -->
<tr><td class="px" style="padding:24px 20px 10px 20px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="dm-tint" style="background-color:{TINT};border-radius:12px;">
<tr>
<td class="stack" valign="middle" style="padding:22px 24px;font-family:{FONT};text-align:left;">
<h2 class="dm-text" style="margin:0 0 6px 0;font-size:20px;line-height:26px;font-weight:800;color:{INK};">{c["card_title"]}</h2>
<p class="dm-muted" style="margin:0;font-size:15px;line-height:22px;color:{MUTED};">{c["card_body"]}</p>
</td>
<td class="stack stack-gap" valign="middle" align="right" style="padding:22px 24px 22px 0;font-family:{FONT};white-space:nowrap;">
<a href="#" class="dm-link" style="color:{GREEN};font-size:16px;line-height:22px;font-weight:800;text-decoration:underline;">{c["card_cta"]} &rarr;</a>
</td>
</tr>
</table>
</td></tr>

<!-- Store -->
<tr><td class="px" style="padding:14px 30px 30px 30px;font-family:{FONT};text-align:left;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid {LINE};">
<tr><td style="padding-top:20px;">
<p class="dm-text" style="margin:0 0 4px 0;font-size:16px;line-height:22px;font-weight:800;color:{INK};">{c["store_title"]}</p>
<p class="dm-muted" style="margin:0 0 8px 0;font-size:14px;line-height:20px;color:{MUTED};">{c["store_body"]}</p>
<a href="#" class="dm-link" style="color:{GREEN};font-size:14px;line-height:20px;font-weight:700;text-decoration:underline;">{c["store_cta"]}</a>
</td></tr>
</table>
</td></tr>

</table>

<!-- Footer -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
<tr><td class="px" style="padding:24px 30px 40px 30px;font-family:{FONT};font-size:12px;line-height:18px;color:{MUTED};text-align:center;">
<p class="dm-muted" style="margin:0 0 8px 0;">{c["footer_why"]}</p>
<p style="margin:0 0 8px 0;"><a href="#" class="dm-muted" style="color:{MUTED};text-decoration:underline;">{c["unsub"]}</a> &nbsp;·&nbsp; <a href="#" class="dm-muted" style="color:{MUTED};text-decoration:underline;">{c["prefs"]}</a></p>
<p class="dm-muted" style="margin:0;">{c["legal"]}</p>
</td></tr>
</table>

</div>
<!--[if mso]></td></tr></table><![endif]-->

</td></tr>
</table>
</div>
</body>
</html>
"""
    with open(os.path.join(OUT, c["file"]), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(c["file"], len(html.encode("utf-8")) // 1024, "KB")


for lang in COPY:
    build(lang)
