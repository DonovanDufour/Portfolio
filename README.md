# Portfolio e-mail FR·NL

Portfolio d’intégration HTML e-mail : cinq gabarits responsive, accessibles et bilingues (français / néerlandais), codés pour Outlook, Gmail et Apple Mail.

*HTML email developer portfolio: five responsive, accessible, bilingual (French / Dutch) email templates.*

## Contenu

| Fichier | Projet | Points techniques |
|---|---|---|
| `emails/verdi-promos-fr.html` · `emails/verdi-promos-nl.html` | Folder promo hebdomadaire d’un supermarché | Colonnes hybrides, bouton VML, versions FR/NL générées depuis un seul gabarit |
| `emails/atelier-nord-commande.html` | Confirmation de commande | E-mail transactionnel, polices système, totaux TVA |
| `emails/lumen-lancement.html` | Lancement produit | Image de fond VML, polices web avec repli |
| `emails/kit-composants.html` | Bibliothèque de 8 modules | Modules réutilisables, inversion de colonnes `dir="rtl"` |

`index.html` présente les e-mails dans une interface de messagerie : bureau / mobile, clair / sombre, et code source. Les styles de la page sont dans `css/style.css`.

`build/build_verdi.py` génère les versions française et néerlandaise de l’e-mail Verdi Markt à partir d’un seul fichier de textes.

## Notes

- Toutes les marques (Verdi Markt, Atelier Nord, Lumen) sont fictives et ont été créées pour ce portfolio.
- Dans un vrai envoi, les chemins d’images (`img/…`) seraient remplacés par des URL absolues hébergées.
