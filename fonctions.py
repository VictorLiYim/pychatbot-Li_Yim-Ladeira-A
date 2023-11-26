from TF-IDF import *

def liste_mot_non_importants(Matrice):
    liste_non_important = []
    # On crée une liste dans laquelle on va rajouter tous les mots nons-importants
    for i in Matrice:
        cpt = 0
        for j in i:
            if j != 0:
                cpt+=1
        if cpt == 0:
            liste_non_important.append(i)
    # On parcourt la matrice avec les scores finaux et on ajoute à la liste les mots ayant un score de 0
    if liste_non_important == []:
        return "Il n'y a pas de mots considéré comme non important"
    else:
        return liste_non_important
    # Si la liste contient des valeurs, on retourne la liste contenant ces valeurs, sinon on retourne la chaine de caractère disant qu'il n'y a aucun mot non important

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
    dico = TF_president(repertoire_cleaned, president)
    liste_non_mots = ["le", "nos"]
    max = 0
    for tf in dico:
        if tf > max:
            max = tf
            score_eleve = []
        elif tf == max:
            score_eleve.append ()
    return score_eleve, max

print(TF(repertoire_cleaned))

def premier_pres_climat():
    liste_presidents = ["deGaulle", "Pompidou", "Giscard dEstaing", "Mitterrand", "Chirac", "Sarkozy", "Hollande", "Macron"]
    # On crée une liste avec tous les présidents de France dans l'ordre chronologique
    for i in liste_presidents:
        if i in noms:
            liste_mots = TF_president(i)
            if "clima" in str(liste_mots.keys()) or "écologi" in str(liste_mots.keys()):
                return i
    # On parcourt chaque texte dans l'ordre chronologique pour voir si le texte contient un mot commençant par "clima" ou "écologi" pour prendre en compte les mots "écologiques", "climatique", ect... puis on retourne le nom du président
