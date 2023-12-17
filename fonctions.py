# Ce fichier permet de regrouper toutes les fonctions interactives avec l'utilisateur, il s'agit des fonctionnalités 
# à développer lors de la partie 1 du projet

from TF_IDF import *

# Fonction renvoyant la liste des mots jugées non importants
def liste_mot_non_importants(Matrice):
    liste_non_important = [] # On crée une liste dans laquelle on va rajouter tous les mots nons-importants
    Liste = liste_totale(repertoire_cleaned, 0) #importation de la liste de tout les mots
    for i in range(0,len(Matrice)):
        cpt = 0
        for j in Matrice[i]:
            if j != 0:
                cpt+=1
        if cpt == 0:
            liste_non_important.append(Liste[i])
    if liste_non_important == []:
        return "Il n'y a pas de mots considéré comme non important"
    else:
        return liste_non_important
    # Si la liste contient des valeurs, on retourne la liste contenant ces valeurs, sinon on retourne la chaine de caractère disant qu'il n'y a aucun mot non important

# Fonction renvoyant la liste du ou des mots ayant le score TF-IDF le plus important
def liste_score_important(Matrice):
    Liste = liste_totale(repertoire_cleaned, 0)
    score_eleve = []
    max = 0
    for ligne in range(0, len(Matrice)):
        for score in Matrice[ligne]:
            if score > max:
                max = score
                score_eleve = [Liste[ligne]]
            elif score == max:
                score_eleve.append(Liste[ligne])
    return score_eleve, max

# Fonction qui renvoie le ou les mots le plus répété par un président spécifique
def mot_plus_repete(repertoire, president):
    dico = TF_president(repertoire, president)
    liste_non_important = liste_mot_non_importants(score_final(repertoire_cleaned))
    non_mots = ["à", "elle", "ne", "pas", "nous", "nos", "notre", "parce", "que", "veut", "au"]
    # La liste liste_non_mots permet d'éviter de compter tout les déterminants qui seront affichés avant les mots qu'on souhaite réellement afficher
    liste = []
    #liste permet de contenir les mots qui ont le même score TF
    max = 0
    # max permet de comparé les différentes valeurs de TF entre les mots
    for tf in dico:
        if dico[tf] > max and tf not in liste_non_important and tf not in non_mots:  # vérifie si la valeur TF est supérieur au maximum et si le mot ne fait pas partie des déterminants
            max = dico[tf]  # Remplace la valeur de max par la nouvelle si la condition est vérifiée
            liste = [tf]  # Si la valeur est strictement supérieure au maximum réinitialise la liste tout en insérant le mot concerné
        elif dico[tf] == max and tf not in liste_non_important and tf not in non_mots:
            liste.append(tf)  # si la valeur TF du mot est la même que le maximum au lieu de réinitialiser on l'insère dans la liste directement
    return liste, max, "fois"

# Fonction qui renvoi la liste des présidents ayant cité un mot précisé par l'utilisateur ainsi que le nom de celui qui
# l'a répété le plus de fois
def recherche_president(repertoire, mot):
    liste_president = [] #liste des présidents ayant cité le mot recherché
    ocurrence = {} #dictionnaire des ocurrences du mot
    max = 0 #permet de savoir la plus grande ocurrence
    nom = "" #permettra de renvoyer le nom du président ayant cité le plus de fois ce mot
    if mot not in liste_totale(repertoire, 0):
        return "Ce mot n'est pas cité dans aucuns des discours enregistrés."    
    for name in noms:
        dico = TF_president(repertoire, name)
        if mot in dico:
            ocurrence[name] = dico[mot] #actualise le dictionnaire avec comme clé le nom du président et comme valeur le nombre d'ocurrence
            liste_president.append(name) #actualise la liste des président ayant cité le mot recherché
    for president in ocurrence: #parcourt le dictionnaire ocurrence
        if ocurrence[president]>= max:
            max = ocurrence[president] #récupère la valeur de la plus grande ocurrence du mot recherché
            nom = president #récupère le nom du président qui a la plus grande ocurrence du mot recherché
    return "Voici la liste des présidents qui ont cité le mot", mot, liste_president, "et celui qui a le plus répété ce mot est", nom, max, "fois."

# Fonction qui renvoi le nom du ou des présidents ayant parlé du climat ou de l'écologie
def premier_pres_climat(repertoire):
    liste_president = []#Initialisation d'une liste qui va contenir les noms des présidents ayant parle de l'écologie ou du climat
    for i in noms: #liste composé de ['Chirac', 'Giscard dEstaing', 'Hollande', 'Macron', 'Mitterrand', 'Sarkozy']
        liste_mots = TF_president(repertoire,i)
        if "clima" in str(liste_mots.keys()) or "écologi" in str(liste_mots.keys()):# On parcourt chaque texte pour voir si le texte contient un mot commençant par "clima"
        # ou "écologi" pour prendre en compte les mots "écologiques", "climatique", ect...
            liste_president.append(i) #Si la condition est vérifiée on ajoute le nom du président
    return "les présidents ayant parlé du climat ou de l'écologie sont :",liste_president

#Fonction qui recherche les mots répétés par tous les présidents
def recherche_mot(repertoire):#fonction supprimée de l'énoncé
    matrice = score_final(repertoire)
    Liste = liste_totale(repertoire, 0)
    liste_mot = []
    for mot in range(0, len(matrice)):
        cpt = 0 #compteur initialisé à 0 à chaque fois que l'on va changer de ligne
        for score in matrice[mot]:
            if score != 0: #si le score tf-idf est différent de 0 cela signifie qu'il est présent dans le document 
                cpt+=1
        if cpt == 8: #si le compteur est égal à 8 cela signifie que le mot concerné est présent dans les 8 documents
            liste_mot.append(Liste[mot]) 
    return liste_mot, "fonction inutile"
