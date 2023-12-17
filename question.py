"""
PROJET PYTHON CHATBOT,
Victor LI YIM, Evan LADEIRA,
Fichier utilisé par le chatbot,
Il comporte toutes les fonctions permettant au traitement de la question posée par l'utilisateur.
"""

from TF_IDF import*

# Fonction permet de séparer dans une liste tous les termes qui compose la question en nettoyant la question de tous
# les caractères spéciaux
def separation(question):
    nquestion = separe_chaine(question)
    return nquestion

#print(separation(question))
# Fonction permettant de faire le tri, autrement dit la fonction supprime les mots ne faisant pas partie du corpus du
# document
def tri(liste):
    mot_corpus = []
    Liste = liste_totale(repertoire_cleaned, 0)
    for i in liste: #parcours de la liste des mots de la question
        if i in Liste: #Vérification si la valeur de i se trouve dans un des discours
            mot_corpus.append(i)
    return mot_corpus
#print(tri(separation(question)))

# Fonction qui calcule le vecteur Tf-idf de la question posée par l'utilisateur
def calcul_tfidf(question, repertoire = repertoire_cleaned):# Fonction pour calculer le vecteur TF-IDF d'une question
    # Calcul du score TF pour chaque mot dans la question
    tf_scores = {}
    mots_question = separation(question) #liste tout les mots composants la question
    mots_separe = tri_selection(list(set(mots_question))) #copie la liste précédente en supprimant les doublons et en la triant par ordre ascii
    mots_separe = tri(mots_separe) #supprime les mots n'existant pas dans le corpus des documents
    idf = IDF(repertoire)
    Liste = liste_totale(repertoire, 0) #liste des mots du corpus
    #Calcul du TF de la question
    for mot in mots_separe: #parcours de triés de la question
        cpt = 0 #compteur initialisé à 0
        for i in mots_question: #parcours de tous les mots de la question
            if i == mot:
                cpt+=1 #compte le nombre d'occurrence du mot concerné dans la question
        tf_scores[mot] = cpt #actualisation du dictionnaire TF
    # Calcul du vecteur TF-IDF en utilisant les scores TF et IDF du corpus
    vecteur_tfidf = [] #liste de dimension M représentant le nombre de mots
    for mot in Liste:
        if mot in mots_separe:
            vecteur_tfidf.append(tf_scores[mot] * idf[mot])#calcul du tf-idf
        else:
            vecteur_tfidf.append(0)  # Met un 0 pour les mots du corpus non présents dans la question
    return vecteur_tfidf
#print(calcul_tfidf(question))

score_transpo = transpose_matrice(score_final(repertoire_cleaned))

#Fonction calculant le produit scalaire de la question et de la matrice score final
def produit_scalaire(vecteurA, vecteurB):
    somme = 0
    l = []
    for i in range(len(files_names)):
        for j in range(len(vecteurA)):
            produit = vecteurA[j] * vecteurB[i][j]
            somme += produit
        l.append(somme)
        somme = 0
    return l

#print(produit_scalaire(calcul_tfidf(question, repertoire_cleaned), transpose_matrice(score_final(repertoire_cleaned))))
# Fonction qui prend en paramètre un vecteur et qui renvoi sa norme
def norme_vecteur(vecteur):
    somme = 0
    for i in range(len(vecteur)):
        carre = vecteur[i] ** 2
        somme += carre
    norme = sqrt(somme)
    return norme
#print(norme_vecteur(calcul_tfidf (question, repertoire_cleaned)))

#Fonction qui prend en paramètre deux vecteurs et qui renvoie le score de similarité entre les deux
def similarite(vecteurA, vecteurB):
    """
    :param vecteurA: vecteur tf-idf de la question
    :param vecteurB: matrice du score final du corpus
    :return: score de similarité
    """
    score = []
    for i in range(0,len(vecteurB)):
        score.append((produit_scalaire(vecteurA, vecteurB)[i])/norme_vecteur(vecteurA)*norme_vecteur(vecteurB[i]))
    return score

#print(similarite(calcul_tfidf(question, repertoire_cleaned), score_transpo))
# Fonction qui renvoie le nom du document trouvé le plus pertinent selon les calculs
def document_pertinent(similarite):
    """
    :param similarite: score de similarité
    :return: nom du document le plus pertinent
    """
    max = similarite[0]
    indice = 0
    for i in range(0, len(similarite)):
        if similarite[i] > max:
            max = similarite[i]
            indice = i
    return files_names[indice]

#print(document_pertinent(similarite(calcul_tfidf (question, repertoire_cleaned), score_transpo)))
# Fonction permettant de renvoyer le mot avec le score TF-IDF le plus élevé dans une question
def maxTFIDF(liste): 
    max = liste[0]
    indice = 0
    Liste = liste_totale(repertoire_cleaned, 0)
    for i in range(0, len(liste)):
        if liste[i] > max:
            max = liste[i]
            indice = i
    return Liste[indice]

#print(maxTFIDF(calcul_tfidf(question, repertoire_cleaned)))

# Fonction qui va renvoyer la phrase jugée adaptée à la question
def generation_reponse(question, repertoire):
    """
    :param question: question posée
    :param repertoire: repertoire cleaned
    :return: réponse
    """
    mot = maxTFIDF(calcul_tfidf(question, repertoire))
    document = document_pertinent(similarite(calcul_tfidf(question, repertoire_cleaned), score_transpo))
    with open("speeches-20231105/"+document, "r") as file:
        for i in file:
            if mot in i:
                return i
                
#Fonction permettant de rendre la réponse plus vivante
def affiner_reponse(question,reponse):
    nouvelle_question = separation(question)
    question_starters = {#on met les clés en minuscule car on va utiliser la fonction separation qui transforme la question en minuscule
    "comment": "Après une analyse approfondie, ",
    "pourquoi": "Cela s'explique par le fait que ",
    "peux": "Oui, absolument! ",
    "que": "À mon avis, ", #Pour que penses-tu de ...
    "quel": "Après avoir étudié votre requête. Le choix optimal serait : ",
    "connais": "Oui, bine sûr! Je suis familier avec cela. ",#pour connais-tu
    "pourriez": "Certainement! ",
    "saurais": "Oui, je sais comment faire cela. ",
    "sais": "Évidemment! ",#sais pour sais-tu
    }
    if nouvelle_question[0] in question_starters:
        reponse = question_starters[nouvelle_question[0]]+reponse
    return reponse
