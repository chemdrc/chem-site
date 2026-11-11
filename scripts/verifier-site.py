#!/usr/bin/env python3
"""Vérifie le site généré (_site/) : liens internes, ancres, pages FR/EN appariées.
Usage : python3 scripts/verifier-site.py _site      (code de sortie 1 en cas d'erreur)"""
import sys
from pathlib import Path
import bs4

SITE = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
DOMAIN = "https://chemdrc.github.io/chem-site"
pages = {p: bs4.BeautifulSoup(p.read_text(encoding="utf-8"), "html5lib") for p in SITE.rglob("*.html")}

def resolve(path):
    path = path.split("#")[0].split("?")[0]
    if path in ("", "/"):
        return SITE / "index.html"
    rel = path.lstrip("/")
    for c in (SITE / rel, SITE / (rel.rstrip("/") + ".html"), SITE / rel / "index.html"):
        if c.is_file():
            return c
    return None

erreurs = []
for page, soup in pages.items():
    nom = page.relative_to(SITE)
    for tag in soup.find_all(["a", "link"], href=True) + soup.find_all(["script", "img"], src=True):
        url = tag.get("href") or tag.get("src")
        if url.startswith(DOMAIN):
            url = url[len(DOMAIN):] or "/"
        if url.startswith(("http:", "https:", "mailto:", "tel:", "data:")):
            continue
        if url.startswith("#"):
            cible = page
        elif url.startswith("/"):
            cible = resolve(url)
        else:
            cible = resolve("/" + str((page.parent / url).relative_to(SITE)))
        if cible is None:
            erreurs.append(f"{nom} : lien cassé → {url}")
            continue
        if "#" in url and cible.suffix == ".html":
            ancre = url.split("#", 1)[1]
            if ancre and not pages[cible].find(id=ancre):
                erreurs.append(f"{nom} : ancre absente → {url}")
    lang = soup.html.get("lang")
    alts = {l["hreflang"] for l in soup.find_all("link", rel="alternate", hreflang=True)}
    if lang == "en" and "fr" not in alts:
        erreurs.append(f"{nom} : page anglaise sans équivalent français (translationKey ?)")

print(f"{len(pages)} pages vérifiées")
for e in erreurs:
    print("  ✗", e)
sys.exit(1 if erreurs else 0)
