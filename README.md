# 🎓 Validation et Gestion de Données Élèves

Projet Python développé dans le cadre de la formation **Dev Data** (Orange Digital Center).

Ce programme lit un fichier CSV contenant des informations sur des élèves, valide chaque ligne selon des règles précises, sépare les données valides des invalides, puis propose un menu interactif pour gérer ces données.

---

## ✨ Fonctionnalités

- **Validation automatique** de 7 champs : CODE, Numéro, Nom, Prénom, Date de naissance, Classe, Notes
- **Séparation** des élèves en deux listes : valides et invalides (avec détail des erreurs)
- **Menu interactif** :
  - Affichage paginé des données (valides / invalides)
  - Ajout d'un nouvel élève avec validation
  - Modification d'un élève invalide (correction champ par champ)
  - Recherche par numéro d'élève
  - Recherche par CODE avec calcul du pourcentage de lignes valides/invalides
- **Pagination** configurable (5 lignes par page par défaut)
- **Calcul de moyennes** par matière selon la formule : `(moyenne_devoirs + 2 × examen) / 3`

---

## 🛠️ Technologies

- Python 3
- Modules standards uniquement (`csv`, `datetime`, `pathlib`)

---

## 📂 Structure du projet

```
Validation_donnees_eleves/
├── data/
│   └── Donnees_Projet_Python_Dev_Data_bis.csv
├── docs/
│   └── Projet_Python_Dev_Data.pdf
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── menu.py
│   ├── pagination.py
│   └── validations.py
├── README.md
└── requirements.txt
```

---

## 🚀 Utilisation

```bash
git clone https://github.com/VOTRE_USERNAME/Validation_donnees_eleves.git
cd Validation_donnees_eleves/src
python main.py
```

Le programme charge automatiquement le fichier CSV, affiche le nombre d'élèves valides/invalides, puis ouvre le menu interactif.

---

## 📋 Règles de validation

| Champ | Règle |
|---|---|
| **CODE** | 3 lettres majuscules + 3 chiffres (ex: `AAD004`) |
| **Numéro** | 7 caractères alphanumériques majuscules, lettres + chiffres obligatoires |
| **Prénom** | Commence par une lettre, minimum 3 caractères, sans chiffre |
| **Nom** | Commence par une lettre, minimum 2 lettres |
| **Date de naissance** | Date valide, formats acceptés : `JJ/MM/AAAA`, `MM/JJ/AAAA`, mois en lettres |
| **Classe** | Niveau (3 à 6) + section (A, B, C, D), normalisé en `XemeY` |
| **Notes** | Format `Matiere[devoir1\|devoir2:examen]#...` |

---

## 👤 Auteur

**Abdoulaye** — Formation Dev Data, Orange Digital Center   