import random as rand


def afficher_allumettes(allumettes):
    print("----------------------------------------")
    print("                Il reste", allumettes, "allumettes")
    print("----------------------------------------")


def tour_joueur(allumettes):
    while True:
        try:
            choix = int(input("Choisissez un nombre entre 1 et 3: "))
            if 1 <= choix <= 3:
                if choix > allumettes:
                    print("Vous ne pouvez pas retirer plus d'allumettes qu'il n'en reste!")
                else:
                    allumettes -= choix
                    break
            else:
                print("Veuillez choisir un nombre entre 1 et 3.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
    return allumettes


def tour_ordinateur(allumettes):
    choix = 0
    for i in [1,2,3]:
        if (allumettes - i) % 4 == 0:
            choix = i
            break

    if allumettes <= 3:
        choix = allumettes
    elif allumettes %4 == 0:
        choix = rand.randint(1, 3)

    print("L'ordinateur a choisi:", choix)
    allumettes -= choix
    return allumettes


def jouer(allumettes):
    while True:
        first_to_play = input("Voulez-vous commencer en premier ? (oui/non): ").lower()
        if first_to_play == "oui" or first_to_play == "non":
            break
        else:
            print("Entrée invalide. Veuillez répondre par 'oui' ou 'non'.")

    joueur_commence = first_to_play == "oui"

    while allumettes > 0:
        afficher_allumettes(allumettes)
        if joueur_commence:
            allumettes = tour_joueur(allumettes)
            if allumettes == 0:
                print("\n**************************")
                print("**** VOUS AVEZ GAGNÉ ****")
                print("**************************")
                break
        else:
            allumettes = tour_ordinateur(allumettes)
            if allumettes == 0:
                print("\n*******************************")
                print("**** L'ORDINATEUR A GAGNÉ ****")
                print("*******************************")
                break

        joueur_commence = not joueur_commence


def rejouer():
    while True:
        rejouer_jeu = input("Voulez-vous rejouer ? Ecrire Oui ou Non: ").lower()
        if rejouer_jeu == "oui":
            return True
        elif rejouer_jeu == "non":
            print("Passez une bonne journée!")
            return False

        else:
            print("Entrée invalide. Veuillez répondre par 'oui' ou 'non'.")


def principale():
    print("Bienvenue au jeu des allumettes!")
    allumettes = rand.randint(15, 30)
    print("Le jeu commence avec", allumettes, "allumettes.")

    while True:
        commencer = input("Voulez-vous commencer le jeu ? (oui/non): ").lower()

        if commencer == "oui":
            jouer(allumettes)
            rejouer()
            break
        elif commencer == "non":
            print("Au revoir! À la prochaine.")
            break
        else:
            print("Entrée invalide. Veuillez répondre par 'oui' ou 'non'.")


principale()
