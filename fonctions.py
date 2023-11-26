from TF-IDF import *

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