from validations import valide, invalide, validationligne
from pagination import pagination


# ============================================================
# MENU PRINCIPAL
def menu():
    while True:
        print("\nFAITES VOTRE CHOIX")
        print("=========================")
        print("1. Affichage des données ")
        print("2. Ajout des données ")
        print("3. Faites une modification ")
        print("4. Faites une recherche ")
        print("5. Quitter")

        choix = input("Entrer votre choix : ")

        if choix == "1":
            afficher_donnees()
        elif choix == "2":
            ajouter_eleve()
        elif choix == "3":
            modifier_eleve()
        elif choix == "4":
            recherche()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("=========================")
            print("Choix Invalide")


# ============================================================
# AFFICHAGE
def afficher_donnees():
    print("=========================")
    print("1. Afficher valide")
    print("2. Afficher invalide")

    choix = input("Entrer votre choix : ")
    if choix == "1":
        pagination(valide)
    elif choix == "2":
        pagination(invalide)
    else:
        print("Choix invalide")


# ============================================================
# AJOUT
def ajouter_eleve():
    code = input("Entrer le code de l'élève : ")
    numero = input("Entrer le numéro de l'élève : ")
    nom = input("Entrer le nom de l'élève : ")
    prenom = input("Entrer le prénom de l'élève : ")
    date_naissance = input("Entrer la date de naissance : ")
    classe = input("Entrer la classe : ")
    note = input("Entrer les notes : ")

    nouvel_eleve = {
        "CODE": code,
        "Numero": numero,
        "Nom": nom,
        "Prénom": prenom,
        "Datedenaissance": date_naissance,
        "Classe": classe,
        "Note": note
    }

    validationligne(nouvel_eleve)


# ============================================================
# MODIFICATION
def modifier_eleve():
    numeleve = input("Entrer le numero de l'eleve a modifier : ")

    for eleve in invalide:
        if eleve["Numero"] == numeleve:
            print(f"Eleve trouve : {eleve}")
            print(f"Erreurs : {eleve['erreurs']}")

            # Pour chaque champ en erreur, on demande la correction
            if "CODE" in eleve["erreurs"]:
                eleve["CODE"] = input("Nouveau CODE : ")

            if "Numero" in eleve["erreurs"]:
                eleve["Numero"] = input("Nouveau Numéro : ")

            if "Prénom" in eleve["erreurs"]:
                eleve["Prénom"] = input("Nouveau Prénom : ")

            if "Nom" in eleve["erreurs"]:
                eleve["Nom"] = input("Nouveau Nom : ")

            if "Datedenaissance" in eleve["erreurs"]:
                eleve["Datedenaissance"] = input("Nouveau Datedenaissance : ")

            if "Classe" in eleve["erreurs"]:
                eleve["Classe"] = input("Nouveau Classe : ")

            if "Note" in eleve["erreurs"]:
                eleve["Note"] = input("Nouveau Note : ")

            invalide.remove(eleve)
            eleve.pop("erreurs")      # on enlève les anciennes erreurs
            validationligne(eleve)    # on revalide proprement
            return

    print("Aucun élève invalide trouvé avec ce numéro.")


# ============================================================
# RECHERCHE
def recherche():
    print("===========================")
    print("1. Rechercher par Numéro")
    print("2. Rechercher par CODE")

    choix = input("Entrez votre choix : ")

    if choix == "1":
        numrecherche = input("Entrez le numero à rechercher : ")
        trouve = False

        for eleve in valide + invalide:
            if eleve["Numero"] == numrecherche:
                print(f"Nom : {eleve['Nom']}")
                print(f"Prénom : {eleve['Prénom']}")
                print(f"Numéro : {eleve['Numero']}")
                print(f"Classe : {eleve['Classe']}")
                trouve = True

        if not trouve:
            print("Aucun élève trouvé avec ce numéro.")

    elif choix == "2":
        coderecherche = input("Entrez le code à rechercher : ")

        nb_valide = 0
        nb_invalide = 0

        for eleve in valide:
            if eleve["CODE"] == coderecherche:
                nb_valide += 1

        for eleve in invalide:
            if eleve["CODE"] == coderecherche:
                nb_invalide += 1

        total = nb_valide + nb_invalide

        if total == 0:
            print("Aucune ligne trouvée avec ce code.")
        else:
            pourcentage_valide = (nb_valide / total) * 100
            pourcentage_invalide = (nb_invalide / total) * 100

            print(f"Total de lignes saisies par ce code : {total}")
            print(f"Lignes valides   : {nb_valide} ({pourcentage_valide:.2f}%)")
            print(f"Lignes invalides : {nb_invalide} ({pourcentage_invalide:.2f}%)")

    else:
        print("Choix invalide")