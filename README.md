# CHEM — Congo Health Emergency

> **Santé pour les nécessiteux**

Site web officiel de **Congo Health Emergency (CHEM)**, organisation humanitaire médicale non gouvernementale, à but non lucratif, basée à Bukavu (Sud-Kivu, République démocratique du Congo).

CHEM est apolitique, sans appartenance confessionnelle ni tribale. Elle **soigne, protège et témoigne** auprès des personnes vulnérables et marginalisées.

---

## À propos de CHEM

| | |
|---|---|
| **Création** | 31 décembre 2021, assemblée générale constituante à Bukavu |
| **Siège** | Avenue Saïo, Quartier Ndendere, Commune d'Ibanda, Bukavu, Sud-Kivu, R.D. Congo |
| **Zone prioritaire** | Sud-Kivu (rayon d'action prévu : toute la R.D.C.) |
| **Principes** | Humanité, impartialité, neutralité, égalité, indépendance |

**Mission :** soigner, protéger, témoigner.

**Domaines d'intervention :** santé, protection, genre et inclusion sociale, environnement et WASH, nutrition, sécurité alimentaire, réhabilitation à base communautaire, éducation, préparation aux désastres, déminage, agropastoral.

---

## Contenu du site

| Page | Français | Anglais |
|---|---|---|
| Accueil | `src/index.html` | `src/en/index.html` |
| L'organisation | `src/organisation.html` | `src/en/organisation.html` |
| Notre action | `src/action.html` | `src/en/action.html` |
| Contact | `src/contact.html` | `src/en/contact.html` |

## Structure du projet

Le site est généré avec [Eleventy](https://www.11ty.dev/) : on modifie les fichiers de `src/`,
Eleventy produit le site final dans `_site/` (jamais modifié à la main, jamais commité).

```
.
├── src/
│   ├── _includes/
│   │   ├── base.njk       # <head> commun, liens hreflang FR/EN
│   │   ├── header.njk     # En-tête et menu (une seule copie pour tout le site)
│   │   └── footer.njk     # Pied de page
│   ├── _data/
│   │   ├── site.json      # Adresse publique du site
│   │   └── t.json         # Textes du menu et du pied de page, en français et en anglais
│   ├── index.html, organisation.html, action.html, contact.html   # Pages françaises
│   ├── en/                # Pages anglaises (mêmes noms de fichiers)
│   ├── sitemap.njk        # → sitemap.xml
│   ├── assets/, css/, js/ # Copiés tels quels
├── scripts/verifier-site.py   # Vérification des liens internes et des pages FR/EN
├── .github/workflows/site.yml # Compilation, vérification et publication sur GitHub Pages
├── eleventy.config.js
└── package.json
```

Chaque page commence par un en-tête (titre, description…) suivi du contenu de la page. Une page
française et sa traduction portent le même nom de fichier : le bouton **EN / FR** du menu passe de
l'une à l'autre.

## Voir le site en local

```bash
npm install     # une seule fois
npm start       # http://localhost:8080
```

## Mise en ligne

Le site est publié sur **GitHub Pages** par GitHub Actions : à chaque `git push` sur `main`, le site est
compilé, les liens sont vérifiés, puis le site est publié. Réglage à faire une seule fois :
*Settings → Pages → Build and deployment → Source : **GitHub Actions***.

---

## Contact

- **Téléphone :** +243 821 505 083 · +243 851 505 083 · +243 998 291 126
- **Courriel :** [congohealthemergency.drc@gmail.com](mailto:congohealthemergency.drc@gmail.com)

© CHEM — Congo Health Emergency. Tous droits réservés.
