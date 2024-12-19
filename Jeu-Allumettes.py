#NOM et PRENOM: Aouezghar Safouan

import random as rand

# Fonction pour afficher le nombre d'allumettes restantes
def afficher_allumettes(allumettes):
    print("----------------------------------------")
    print("                Il reste", allumettes, "allumettes")
    print("----------------------------------------")


# Fonction pour gérer le tour du joueur
def tour_joueur(allumettes):
    while True:  # Boucle jusqu'à ce qu'un choix valide soit fait
        try:
            choix = int(input("Choisissez un nombre entre 1 et 3: "))
            if 1 <= choix <= 3:
                if choix > allumettes:
                    print("Vous ne pouvez pas retirer plus d'allumettes qu'il n'en reste")
                else:
                    allumettes -= choix
                    break
            else:
                print("Veuillez choisir un nombre entre 1 et 3.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
    return allumettes


# Fonction pour gérer le tour de l'ordinateur
def tour_ordinateur(allumettes):
    choix = 0
    # Boucle stratégique pour trouver le meilleur coup pour l'ordinateur
    for i in [1, 2, 3]:
        if (allumettes - i) % 4 == 0:
            choix = i
            break

    if allumettes <= 3:
        choix = allumettes
    elif allumettes % 4 == 0:
        choix = rand.randint(1, 3)

    print("L'ordinateur a choisi:", choix)
    allumettes -= choix
    return allumettes


# Fonction principale du jeu où la logique est mise en œuvre
def jouer(allumettes):
    while True:  # Demander qui commence jusqu'à obtenir une réponse valide
        first_to_play = input("Voulez vous commencer en premier? écrivez oui OU non : ").lower()
        if first_to_play == "oui" or first_to_play == "non":
            break
        else:
            print("Entrée invalide. Veuillez répondre par oui OU non")

    joueur_commence = first_to_play == "oui"

    # Boucle principale du jeu, continue jusqu'à ce qu'il n'y ait plus d'allumettes
    while allumettes > 0:
        afficher_allumettes(allumettes)
        if joueur_commence:
            allumettes = tour_joueur(allumettes)
            if allumettes == 0:
                print("\n**************************")
                print("**** VOUS AVEZ GAGNÉ ****")
                print("**************************")
                break
        else:  # Tour de l'ordinateur
            allumettes = tour_ordinateur(allumettes)
            if allumettes == 0:
                print("\n*******************************")
                print("**** L'ORDINATEUR A GAGNÉ ****")
                print("*******************************")
                break

        joueur_commence = not joueur_commence


# Fonction pour demander au joueur s'il veut rejouer
def rejouer():
    while True:  # Boucle jusqu'à obtenir une réponse valide
        rejouer_jeu = input("Voulez-vous rejouer ? Ecrivez oui OU non: ").lower()
        if rejouer_jeu == "oui":
            return True
        elif rejouer_jeu == "non":
            print("Passez une bonne journée!")
            return False
        else:
            print("Entrée invalide. Veuillez répondre par oui OU non: ")


# Fonction principale pour démarrer et gérer le jeu
def principale():
    print("Bienvenue au jeu des allumettes")
    allumettes = rand.randint(15, 30)
    print("Le jeu commence avec", allumettes, "allumettes")

    while True:  # Boucle de rejouer, continue tant que le joueur veut rejouer
        commencer = input("Voulez-vous commencer le jeu ? écrivez oui OU non: ").lower()

        if commencer == "oui":
            jouer(allumettes)
            rejouer()
            break
        elif commencer == "non":
            print("Passez une bonne journée")
            break
        else:
            print("Entrée invalide. Veuillez répondre par oui OU non: ")


# Lancer le jeu en appelant la fonction principale
principale()
