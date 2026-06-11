def pagination(liste):
    """
    Affiche une liste de dictionnaires (élèves) page par page.
    Demande à l'utilisateur le nombre de lignes par page (5 par défaut).
    """
    if not liste:
        print("Aucune donnée à afficher.")
        return

    nbreligne = input("Vous voulez combien de ligne par page : ")
    if nbreligne == "":
        nbreligne = 5
    else:
        nbreligne = int(nbreligne)

    page_actuel = 0
    while True:
        debut = page_actuel * nbreligne
        fin = debut + nbreligne

        page = liste[debut:fin]
        if not page:
            print("Fin de la liste.")
            break

        for eleve in page:
            print(eleve)

        suite = input("Page suivante ? (o/n) : ")
        if suite.lower() == "o":
            page_actuel += 1  # on passe à la page suivante
        else:
            break


# Page 0 -> debut = 0x5 = 0  | fin = 0+5 = 5  -> élèves [0:5]
# Page 1 -> debut = 1x5 = 5  | fin = 5+5 = 10 -> élèves [5:10]
# Page 2 -> debut = 2x5 = 10 | fin = 10+5= 15 -> élèves [10:15]