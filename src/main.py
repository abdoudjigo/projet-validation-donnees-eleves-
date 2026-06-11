import csv
from pathlib import Path

from validations import valide, invalide, validationligne
from menu import menu


# ============================================================
# CHEMIN DU FICHIER CSV
# Chemin relatif : data/Donnees_Projet_Python_Dev_Data_bis.csv
BASE_DIR = Path(__file__).resolve().parent.parent
FICHIER_CSV = BASE_DIR / "data" / "Donnees_Projet_Python_Dev_Data_bis.csv"


# ============================================================
# LECTURE ET VALIDATION DES DONNÉES
def charger_donnees():
    with open(FICHIER_CSV, encoding="utf-8") as ficherouvert:
        classeur = csv.DictReader(ficherouvert)
        infoetudiant = []
        for ligne in classeur:
            infoetudiant.append(ligne)

    for ligne in infoetudiant:
        validationligne(ligne)

    print(f"\nEtudiants valides   : {len(valide)}")
    print(f"Etudiants invalides : {len(invalide)}\n")


# ============================================================
# POINT D'ENTRÉE
if __name__ == "__main__":
    charger_donnees()
    menu()