"""
PROJET PYTHON CHATBOT,
Victor LI YIM, Evan LADEIRA,
Fichier permettant l'exécution du menu ainsi que du chatbot,
Ce fichier est le seul qui aura une interaction avec l'utilisateur.
"""

from fonctions import *
from question import *
import time

#La fonction chatbot reprend toutes le fonctions du fichier question permettant de répondre à la question de l'utilisateur
def chatbot():
    continuer = True
    while continuer:
        question = input("Si vous souhaitez quitter le mode chatbot veuillez écrire quitter\n"
                         "              Bienvenue sur ChatEFREI, veuillez poser votre question : \n")
        if question == "quitter":
            continuer = False
        else:
            print("Veuillez patienter quelques secondes, je suis actuellement en train de chercher la réponse la "
                  "plus optimale afin de satisfaire vos attentes.")
            print("Question :", question, "\n"
                  "Document pertinent retourné :",document_pertinent(similarite(calcul_tfidf(question, repertoire_cleaned), score_transpo)),"\n"
                  "Mot ayant le TF-IDF le plus élevé :", maxTFIDF(calcul_tfidf(question, repertoire_cleaned)), "\n"
                  "Réponse :", affiner_reponse(question, generation_reponse(question, repertoire_cleaned)))

#La fonction menu permet à l'utilisateur de tester les fonctions de traitement de documents ou bien le chatbot
def menu():
    continuer = True
    while continuer:
        option = int(input("\nQue voulez-vous faire entre :\n"
                            "-1)Renvoyer la liste des mots non importants\n"
                            "-2)Renvoyer la liste des mots ayant le score TF-IDF le plus élevé\n"
                            "-3)Afficher le ou les mots les plus répétés par un président\n"
                            "-4)Afficher le ou les présidents ayant cité un mot dans un dicours et celui qui a le plus répété ce mot \n"
                            "-5)Afficher le ou les présidents ayant parlé du climat et de l'écologie\n"
                            "-6)Afficher les mots qui ont été utilisé par tous les présidents\n"
                            "-7)Utiliser le chatbot\n"
                            "-8)Quitter\n"
                            "Veuillez saisir un entier parmi les 8 propositions\n"
                            "Réponse : "))
        while not (option in [1,2,3,4,5,6,7,8]):
            print("Vous n'avez pas inscrit la bonne requête. Veuillez réessayer")
            option = int(input("\nQue voulez-vous faire entre :\n"
                            "-1)Renvoyer la liste des mots non importants\n"
                            "-2)Renvoyer la liste des mots ayant le score TF-IDF le plus élevé\n"
                            "-3)Afficher le ou les mots les plus répétés par un président\n"
                            "-4)Afficher le ou les présidents ayant cité un mot dans un dicours et celui qui a le plus répété ce mot \n"
                            "-5)Afficher le ou les présidents ayant parlé du climat et de l'écologie\n"
                            "-6)Afficher les mots qui ont été utilisé par tous les présidents\n"
                            "-7)Utiliser le chatbot\n"
                            "-8)Quitter\n"
                            "Veuillez saisir un entier parmi les 8 propositions\n"
                            "Réponse : "))
        if option == 1:
            print(liste_mot_non_importants(score_final(repertoire_cleaned)))
            time.sleep(3)
        elif option == 2:
            print(liste_score_important(score_final(repertoire_cleaned)))
            time.sleep(3)
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
            time.sleep(2)
            print(menu())
        elif option == 4:
            mot = input("Veuillez saisir le mot recherché : ")
            print(recherche_president(repertoire_cleaned, mot))
            time.sleep(2)
        elif option == 5:
            print(premier_pres_climat(repertoire_cleaned))
            time.sleep(2)
        elif option == 6:
            print(recherche_mot(repertoire_cleaned))
            time.sleep(2)
        elif option == 7:
            print(chatbot())
            time.sleep(2)
        else:
            continuer = False
