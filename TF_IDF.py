import os
from math import *

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
directory = "/workspaces/pychatbot-Li_Yim-Ladeira-A/speeches-20231105"
files_names = list_of_files(directory, "txt")

def tri_selection(t):
    for i in range(len(t) - 1):
        j_min = i
        for j in range(i + 1, len(t)):
            if t[j] < t[j_min]:
                j_min = j
        if j_min != i:
            t[i], t[j_min] = t[j_min], t[i]
    return t

def take_name():
    noms = [nom.split('_')[1].split('.')[0] for nom in files_names]
    # L'indice indique quelle partie on veut garder. On suprrime la première partie du nom du fichier avec le premier split
    # Ensuite on fait un deuxième split pour supprimer cette fois ci tout ce qui est écrit après le point
    nom = ""
    verif = True
    for i in range(0, len(noms)-1):
        for j in range(0,len(noms[i])):
            if (ord(noms[i][j])>=57 or ord(noms[i][j])<=48) and verif:
                nom += noms[i][j]
                verif = False
            verif = True
        noms[i] = nom
        nom = ""
    noms = set(noms)
    noms = list(noms)
    noms = list(tri_selection(noms))
    return noms

noms = take_name()
def take_name_numerote():
    noms_num = [nom.split('_')[1].split('.')[0] for nom in files_names]
    noms_num = set(noms_num)
    noms_num = tri_selection(list(noms_num))
    return noms_num
noms_num = take_name_numerote()

def asso_prenom():
    for i in noms:
        if i == "Chirac":
            print("Jacques", i)
        elif i == "Giscard dEstaing ":
            print("Valery", i)
        elif i == "Hollande":
            print("François", i)
        elif i == "Macron":
            print("Emmanuel", i)
        elif i == "Mitterand":
            print("François", i)
        else:
            print("Nicolas", i)
    return " "


def crea_doss():
    try:
        os.mkdir("/workspaces/pychatbot-Li_Yim-Ladeira-A/cleaned")
    except:
        return " "

def copy_file(file):
    for i in file:
        with open ("/workspaces/pychatbot-Li_Yim-Ladeira-A/speeches-20231105/" + i, "r") as f1, open ("/workspaces/pychatbot-Li_Yim-Ladeira-A/cleaned/" + i,"w") as f2:
             lignes = f1.readlines()
             for mot in lignes:
                for j in mot:
                # On ouvre chaque fichiers et on regarde chaque caractère individuellement
                    if ord(j)>= 65 and ord(j)<=90:
                        j = chr(ord(j)+32)
                    elif ord(j) == 39:
                        j = "e "
                    elif (ord(j) == 44):
                        j = ""
                    elif (ord(j)>= 33 and ord(j) != 39 and ord(j)<=47) or (ord(j)>= 58 and ord(j)<=64) or (ord(j)>= 91 and ord(j)<=96) \
                            or (ord(j)>= 123 and ord(j)<=126):
                        j = " "
                    f2.write(j)
                    # On re écrit chaque caractère dans le dossier "cleaned" en écrivant tous les caractères en minuscule et en enlevant toute ponctuation 
    f1.close()
    f2.close()
    return " "

print(copy_file(files_names))

def count_TF(chaine, mot):
    chaine_de_caractere = ""
    # On initialise une chaine de caractère ne contenant aucun caractère
    for i in chaine:
        if i != " " and ord(i)!=10:
            chaine_de_caractere += i
            # Pour chaque chaine de caractère, tant que 
        else:
            if chaine_de_caractere != "":
                if chaine_de_caractere in mot.keys():
                    mot[chaine_de_caractere] += 1
                else:
                    mot[chaine_de_caractere] = 1
            chaine_de_caractere = ""
    if chaine_de_caractere in mot.keys():
        mot[chaine_de_caractere] += 1
    else:
        mot[chaine_de_caractere] = 1
    return mot


def TF(directory):
    occurence = {}
    for i in files_names:
        with open(directory +"/"+i, "r") as fichier:
            for ligne in fichier:
                occurence = count_TF(ligne, occurence)
    fichier.close()
    return occurence
repertoire_cleaned = "/workspaces/pychatbot-Li_Yim-Ladeira-A/cleaned"

def TF_document(repertoire,name):
    occurence = {}
    for i in files_names:
        with open(repertoire+"/" + i, "r") as fichier:
            if name in fichier.name:  # Vérifier si le nom est dans le nom de fichier
                for ligne in fichier:
                    occurence = count_TF(ligne, occurence)
    fichier.close()
    return occurence

def TF_president(repertoire, name):
    occurence = {}
    for i in files_names:
        with open(repertoire+"/" + i, "r") as fichier:
            if name in fichier.name:  # Vérifier si le nom est dans le nom de fichier
                for ligne in fichier:
                    occurence = count_TF(ligne, occurence)
    fichier.close()
    return occurence

def liste_totale(repertoire, option):
    L1,L2,L3,L4,L5,L6,L7,L8 = [],[],[],[],[],[],[],[]
    n = 0
    for i in files_names:
        L = [L1,L2,L3,L4,L5,L6,L7,L8]
        with open(repertoire+"/" + i, "r") as f1:
             for phrase in f1:
                for word in phrase.split():
                    if word not in L[n]:
                        L[n].append(word)
        n+=1
    Liste = set(L1+L2+L3+L4+L5+L6+L7+L8)
    Liste = tri_selection(list(Liste))
    f1.close()
    if option == 0:
        return Liste
    else:
        return L
    
def IDF(repertoire):
    Liste = liste_totale(repertoire, 0)
    L = liste_totale(repertoire,1)
    dico_mot = {}
    for j in Liste:
        cpt = 0
        for h in range(0, 8):
            if j in L[h]:
                cpt += 1
        dico_mot[j] = cpt
    dico_idf = {}
    for k in dico_mot:
        score = log10(len(files_names)/(dico_mot[k])+1)
        dico_idf[k] = score
    return dico_idf

def score_final(repertoire):
    Liste_totale = liste_totale(repertoire_cleaned, 0)
    dico_idf = IDF(repertoire_cleaned)
    TFIDF = []
    for i in range(0,len(Liste_totale)):
        TFIDF.append([])
        valeuridf = dico_idf[Liste_totale[i]]
        for j in noms_num:
            dico_tf = TF_document(repertoire, j)
            if Liste_totale[i] in dico_tf:
                valeurtf = dico_tf[Liste_totale[i]]
            else:
                valeurtf = 0
            valeur_tfidf = valeurtf*valeuridf
            TFIDF[i].append(valeur_tfidf)
    return TFIDF

def premier_pres_climat():
    liste_presidents = ["deGaulle", "Pompidou", "Giscard dEstaing", "Mitterrand", "Chirac", "Sarkozy", "Hollande", "Macron"]
    # On crée une liste avec tous les présidents de France dans l'ordre chronologique
    for i in liste_presidents:
        if i in noms:
            liste_mots = TF_president(i)
            if "clima" in str(liste_mots.keys()) or "écologi" in str(liste_mots.keys()):
                return i
    # On parcourt chaque texte dans l'ordre chronologique pour voir si le texte contient un mot commençant par "clima" ou "écologi" pour prendre en compte les mots "écologiques", "climatique", ect... puis on retourne le nom du président

