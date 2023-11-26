from TF_IDF import *

def liste_mot_non_importants(Matrice):
    liste_non_important = []
    for i in Matrice:
        cpt = 0
        for j in i:
            if j != 0:
                cpt+=1
        if cpt == 0:
            liste_non_important.append(i)
    if liste_non_important == []:
        return "Il n'y a pas de mots considéré comme non important"
    else:
        return liste_non_important

dico_score_final = score_final(repertoire_cleaned)

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

def mot_plus_repete(repertoire, president):
    dico = TF_president(repertoire, president)
    liste_non_mots = ["le", "nos", "de", '', 'la', 'et', "les", "à", "une", "des", "que", "je", "pour", "elle", "ce", "se", "est", "du"
                      "a", "notre", "parce"]
    #La liste liste_non_mots permet d'éviter de compter tout les déterminants qui seront affichés avant les mots qu'on souhaite réellement afficher
    liste = []
    #liste permet de contenir les mots qui ont le même score TF
    max = 0
    #max permet de comparé les différentes valeurs de TF entre les mots
    for tf in dico:
        if dico[tf] > max and tf not in liste_non_mots and len(tf)>4: #vérifie si la valeur TF est supérieur au maximum et si le mot ne fait pas partie des déterminants
            max = dico[tf] #Remplace la valeur de max par la nouvelle si la condition est vérifiée
            liste = [tf] #Si la valeur est strictement supérieure au maximum réinitialise la liste tout en insérant le mot concerné
        elif dico[tf] == max and tf not in liste_non_mots and len(tf)>4:
            liste.append(tf) #si la valeur TF du mot est la même que le maximum au lieu de réinitialiser on l'insère dans la liste directement
    return liste, max, "fois"

def premier_pres_climat():
    liste_presidents = ["deGaulle", "Pompidou", "Giscard dEstaing", "Mitterrand", "Chirac", "Sarkozy", "Hollande", "Macron"]
    # On crée une liste avec tous les présidents de la Ve république dans l'ordre chronologique pour que la fonction fonctionne si l'on rajoute des textes d'autres présidents
    for i in liste_presidents:
        if i in noms:
            liste_mots = TF_president(i)
            if "clima" in str(liste_mots.keys()) or "écologi" in str(liste_mots.keys()):
                return i
    # On parcourt chaque texte dans l'ordre chronologique pour voir si le texte contient un mot commençant par "clima" ou "écologi" pour prendre en compte les mots "écologiques", "climatique", ect... puis on retourne le nom du président

def recherche_president(repertoire, mot):
    liste_president = [] #liste des présidents ayant cité le mot recherché
    ocurrence = {} #dictionnaire des ocurrences du mot
    max = 0 #permet de savoir la plus grande ocurrence
    nom = "" #permettra de renvoyer le nom du président ayant cité le plus de fois ce mot
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

def recherche_mot(repertoire):
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
    return liste_mot