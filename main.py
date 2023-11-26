from fonctions import *
import time
def menu():
    global president
    verifier = True
    while verifier:
        option = int(input("\nQue voulez-vous faire entre :\n"
                            "-1)Renvoyer la liste des mots non importants\n"
                            "-2)Renvoyer la liste des mots ayant le score TF-IDF le plus élevé\n"
                            "-3)Afficher le ou les mots les plus répétés par un président\n"
                            "-4)Afficher le ou les présidents ayant cité un mot dans un dicours et celui qui a le plus répété ce mot \n"
                            "-5)Afficher le premier président qui a parlé du climat et de l'écologie\n"
                            "-6)Afficher les mots qui ont été utilisé par tous les présidents\n"
                            "-7)Si vous voulez quitter saisissez quitter\n"
                            "Veuillez saisir un entier parmi les 7 propositions\n"
                            "Réponse : "))
        while not (option in [1,2,3,4,5,6,7]):
            print("Vous n'avez pas inscrit la bonne requête. Veuillez réessayer")
            option = int(input("\nQue voulez-vous faire entre :\n"
                            "-1)Renvoyer la liste des mots non importants\n"
                            "-2)Renvoyer la liste des mots ayant le score TF-IDF le plus élevé\n"
                            "-3)Afficher le ou les mots les plus répétés par un président\n"
                            "-4)Afficher le ou les présidents ayant cité un mot dans un dicours et celui qui a le plus répété ce mot \n"
                            "-5)Afficher le premier président qui a parlé du climat et de l'écologie\n"
                            "-6)Afficher les mots qui ont été utilisé par tous les présidents\n"
                            "-7)Si vous voulez quitter saisissez quitter\n"
                            "Veuillez saisir un entier parmi les 7 propositions\n"
                            "Réponse : "))
        if option == 1:
            print(liste_mot_non_importants(score_final(repertoire_cleaned)))
            time.sleep (3)
        elif option == 2:
            print(liste_score_important(score_final(repertoire_cleaned)))
            time.sleep (3)
        elif option == 3:
            verifier = True
            while verifier:
                president = input("\nDe quel président voulez vous afficher la liste des mots les plus répétés :\n"
                                     "-1)Chirac\n"
                                     "-2)Giscard dEstaing\n"
                                     "-3)Hollande\n"
                                     "-4)Macron \n"
                                     "-5)Sarkozy\n"
                                     "-6)Mitterrand\n"
                                     "Veuillez saisir comme indiqué ci-dessus le nom d'un des six presidents\n"
                                     "Réponse : ")
                if president in ["Chirac", "Giscard dEstaing", "Hollande", "Macron", "Sarkozy", "Mitterrand"]:
                    verifier = False
                while (president not in ["Chirac", "Giscard dEstaing", "Hollande", "Macron", "Sarkozy", "Mitterrand"]):
                    print("Vous n'avez pas inscrit la bonne requête. Veuillez réessayer")
                    president = input("\nDe quel président voulez vous afficher la liste des mots les plus répétés :\n"
                                     "-1)Chirac\n"
                                     "-2)Giscard dEstaing\n"
                                     "-3)Hollande\n"
                                     "-4)Macron \n"
                                     "-5)Sarkozy\n"
                                     "-6)Mitterrand\n"
                                     "Veuillez saisir comme indiqué ci-dessus le nom d'un des six presidents\n"
                                     "Réponse : ")
            print(mot_plus_repete(repertoire_cleaned, president))
            time.sleep (3)
            print(menu())
        elif option == 4:
            mot = input("Veuillez saisir le mot recherché : ")
            print(recherche_president(repertoire_cleaned, mot))
            time.sleep(3)
        elif option == 5:
            print(premier_pres_climat(repertoire_cleaned))
            time.sleep(3)
        elif option == 6:
            print(recherche_mot(repertoire_cleaned))
            time.sleep(3)
        else:
            continuer = False
            break

print(menu())
