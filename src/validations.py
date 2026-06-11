from datetime import datetime


# ============================================================
# FONCTION 1 — Valider le CODE
# Règle : 3 lettres majuscules + 3 chiffres, longueur 6
def validationcode(CODE):
    if CODE[:3].isalpha() and len(CODE) == 6 and CODE[3:].isdigit() and CODE[:3].isupper():
        return True
    else:
        return False


# ============================================================
# FONCTION 2 — Valider le NUMERO
# Règle : 7 caractères, lettres MAJUSCULES et chiffres
#         doit contenir au moins une lettre et un chiffre
def validationnumero(Numero):
    if len(Numero) != 7:
        return False
    if not Numero.isalnum():
        return False
    if Numero.isdigit():
        return False
    if Numero.isalpha():
        return False
    if not Numero.isupper():
        return False
    return True


# ============================================================
# FONCTION 3 — Valider le PRÉNOM
def validationprenom(Prenom):
    if len(Prenom) == 0:
        return False
    if not Prenom[0].isalpha() or len(Prenom) < 3:
        return False

    for i in Prenom:
        if i.isdigit():
            return False
    return True


# ============================================================
# FONCTION 4 — Valider le NOM
# Règle : commence par une lettre, au moins 2 lettres
def validationnom(Nom):
    if Nom.isalpha() and len(Nom) >= 2:
        return True
    else:
        return False


# ============================================================
# FONCTION 5 — Valider la DATE DE NAISSANCE
def validationdate(date):
    # 1. Transformer en texte
    date = str(date).lower()

    # 2. Remplacer les séparateurs
    date = date.replace("-", "/")
    date = date.replace("_", "/")

    # 3. Gérer les mois en lettres (juste les principaux)
    date = date.replace("janvier", "01")
    date = date.replace("fevrier", "02")
    date = date.replace("mars", "03")
    date = date.replace("avril", "04")
    date = date.replace("mai", "05")
    date = date.replace("juin", "06")
    date = date.replace("juillet", "07")
    date = date.replace("aout", "08")
    date = date.replace("septembre", "09")
    date = date.replace("octobre", "10")
    date = date.replace("novembre", "11")
    date = date.replace("decembre", "12")

    try:
        # 4. Tester format JJ/MM/AAAA
        datetime.strptime(date, "%d/%m/%Y")
        return True
    except:
        try:
            # 5. Tester format MM/JJ/AAAA
            datetime.strptime(date, "%m/%d/%Y")
            return True
        except:
            return False


# ============================================================
# FONCTION 6 — Valider et convertir la CLASSE
def validationclasse(classe):
    x = ["3", "4", "5", "6"]
    y = ["A", "B", "C", "D"]

    if len(classe) == 0:
        return False, "Classe vide"
    classe = classe.replace(" ", "")

    chiffre = classe[0]
    lettre = classe[-1]

    if chiffre in x and lettre in y:
        return True, chiffre + "eme" + lettre   # ex: "4emeA"
    else:
        return False, "Classe invalide"


# ============================================================
# FONCTION 7 — Valider les NOTES
# Règle : format Math[11|13:06]#Francais[08|17:12]...
#         on parse, on calcule la moyenne
def validationnote(note):
    try:
        # 1. Séparer les matières
        matieres = note.split("#")

        for matiere in matieres:
            matiere = matiere.strip()  # enlever espaces

            # 2. Séparer nom et contenu
            nom, contenu = matiere.split("[")

            # 3. Enlever ]
            contenu = contenu.replace("]", "")

            # 4. Séparer devoirs et examen
            devoirs_str, examen_str = contenu.split(":")

            # 5. Séparer les devoirs
            liste_devoirs = devoirs_str.split("|")

            # 6. Convertir en float
            devoirs = []
            for d in liste_devoirs:
                d = d.replace(",", ".")
                devoirs.append(float(d))

            # 7. Convertir examen
            examen = float(examen_str.replace(",", "."))

        return True

    except:
        return False


# ============================================================
# LISTES DE STOCKAGE
valide = []
invalide = []


def validationligne(ligne):
    # Dictionnaire vide qui va collecter les erreurs trouvées
    erreurs = {}
    # Si la fonction retourne False → on ajoute l'erreur dans le dictionnaire

    if validationcode(ligne["CODE"]) is False:
        erreurs["CODE"] = "code invalide"

    if validationnumero(ligne["Numero"]) is False:
        erreurs["Numero"] = "numero invalide"

    if validationprenom(ligne["Prénom"]) is False:
        erreurs["Prénom"] = "Prénom invalide"

    if validationnom(ligne["Nom"]) is False:
        erreurs["Nom"] = "Nom invalide"

    if validationdate(ligne["Datedenaissance"]) is False:
        erreurs["Datedenaissance"] = "Date invalide"

    # validationclasse retourne un tuple (True/False, message)
    resultat = validationclasse(ligne["Classe"])
    if resultat[0] is False:
        erreurs["Classe"] = "Classe invalide"
    else:
        # On normalise la classe au format "4emeA"
        ligne["Classe"] = resultat[1]

    if validationnote(ligne["Note"]) is False:
        erreurs["Note"] = "Note invalide"

    if erreurs == {}:
        # Aucune erreur → ligne valide
        valide.append(ligne)
        print(f"{ligne['Nom']} {ligne['Prénom']}")
        return True
    else:
        ligne["erreurs"] = erreurs
        invalide.append(ligne)
        print(f"{ligne['Nom']} {ligne['Prénom']} -> {erreurs}")
        return False