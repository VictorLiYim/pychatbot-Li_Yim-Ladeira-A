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

def separe_chaine(phrase, delimitation=' '):
    nphrase = ""
    for mot in phrase:
        for i in mot:  # On ouvre chaque fichier et on regarde chaque caractère individuellement
            if ord (i) >= 65 and ord (i) <= 90:
                nphrase += chr(ord(i) + 32)
            elif ord(i) == 39:
                nphrase += "e "
            elif (ord(i) == 44) or (ord(i) == 10):
                nphrase += ""
            elif (ord (i) >= 33 and ord (i) != 39 and ord (i) <= 47) or (ord (i) >= 58 and ord (i) <= 64) or (
                    ord (i) >= 91 and ord (i) <= 96) or (ord (i) >= 123 and ord (i) <= 126):
                nphrase += " "
            else:
                nphrase += i
    split_list = []
    mot = ''
    for c in nphrase:
        if c != delimitation:
            mot += c
        else:
            if mot != "":
                split_list.append(mot)
                mot = ''
    # Ajouter le dernier mot après la dernière occurrence du délimiteur
    if mot != "":
        split_list.append(mot)
    return split_list

def take_name():
    liste_noms = []
    noms = []
    for i in files_names:
        i = separe_chaine(i) #Décompose la liste des noms des fichiers par mots
        if len(i) == 4: #Pour le cas de Giscard d estaing
            liste_noms.append(i[1]+" "+i[2])
        else:
            liste_noms.append(i[1])
        nvnom = ""
        if len(i) == 4:  # Pour le cas de Giscard d estaing
            for j in range(0, len(i[1])):  # On transforme la première lettre de Giscard en majuscule
                if j == 0:
                    nvnom += chr(ord(i[1][j]) - 32)
                else:
                    nvnom += i[1][j]
            nvnom += " "
            for l in range(0, len(i[2]) - 1):  # On transforme la deuxième lettre de d estaing comme dans le fichier en majuscule
                if l == 1:
                    nvnom += chr(ord(i[2][l]) - 32)
                else:
                    nvnom += i[2][l]
            noms.append(nvnom)
            nvnom = ""
        else:
            for k in range(0, len(i[1])):
                if k == 0:
                    nvnom += chr(ord(i[1][k]) - 32)
                else:
                    nvnom += i[1][k]
            noms.append(nvnom)
            nvnom = ""
    nom = ""
    verif = True
    for i in range(0, len(noms)):
        for j in range(0,len(noms[i])):
            if (ord(noms[i][j])>=57 or ord(noms[i][j])<=48) and verif:
                nom += noms[i][j]
                verif = False
            verif = True
        noms[i] = nom
        nom = ""
    noms = set(noms)
    noms = tri_selection(list(noms))
    return noms

noms = take_name()
files_names = tri_selection(files_names)

def take_name_numerote():
    noms_num = []
    for i in files_names:
        i = separe_chaine(i)  # Décompose la liste des noms des fichiers par mots
        nvnom = ""
        if len(i) == 4:  # Pour le cas de Giscard d estaing
            for j in range(0, len(i[1])): #On transforme la première lettre de Giscard en majuscule
                if j == 0:
                    nvnom += chr(ord(i[1][j]) - 32)
                else:
                    nvnom += i[1][j]
            nvnom += " "
            for l in range(0, len(i[2])-1):#On transforme la deuxième lettre de d estaing comme dans le fichier en majuscule
                if l == 1:
                    nvnom += chr(ord(i[2][l]) - 32)
                else:
                    nvnom += i[2][l]
            noms_num.append(nvnom)
            nvnom = ""
        else:
            for k in range(0, len(i[1])):
                if k == 0:
                    nvnom += chr(ord(i[1][k])-32)
                else:
                    nvnom += i[1][k]
            noms_num.append(nvnom)
            nvnom = ""
    noms_num = set(noms_num)
    noms_num = tri_selection(list(noms_num))
    return noms_num

noms = take_name()
files_names = tri_selection(files_names)
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
        with open ("speeches-20231105/" + i, "r") as f1, open ("cleaned/" + i,"w") as f2:
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
    chaine_de_caractere = ""    # On initialise une chaine de caractère ne contenant aucun caractère
    for i in chaine:
        if i != " " and ord(i)!=10:
            chaine_de_caractere += i
            # Pour chaque chaine de caractère, on ajoute à la chaine de caractère tous les caractères jusqu'à ce qu'il y ait un espace ou un retour à la ligne
        else:
            if chaine_de_caractere != "":
                if chaine_de_caractere in mot.keys():
                    mot[chaine_de_caractere] += 1
                else:
                    mot[chaine_de_caractere] = 1
            chaine_de_caractere = ""
        # Lorsqu'on rencontre un espace ou un retour à la ligne, on vérifie si le mot appartient au dictionnaire "mot" en temps que clef. Si c'est le cas, on rajoute 1 occurence pour le mot, sinon on le rajoute en temps que clef et on initialise sa valeur à 1. Enfin, on réinitialise la chaine de caractère.
    if chaine_de_caractere in mot.keys():
        mot[chaine_de_caractere] += 1
    else:
        if chaine_de_caractere != "":
            mot[chaine_de_caractere] = 1
    return mot
    # On refait la même manipulation une dernière fois pour le dernier mot du fichier qui n'a pas été comptabilisé dans la boucle, puis on retourne le dictionnaire

def TF(directory):
    occurence = {}
    for i in files_names:
        with open(directory +"/"+i, "r") as fichier:
            for ligne in fichier:
                occurence = count_TF(ligne, occurence)
    fichier.close()
    return occurence

repertoire_cleaned = "cleaned"#on l'utilisera pour l'execution des fonctions demandant un répertoire

def TF_document(repertoire,name):
    occurence = {}
    # On crée un dictionnaire qui contiendra le nombre d'occurences de chaque mot pour chaque document
    for i in files_names:
        with open(repertoire+"/" + i, "r") as fichier:
            if name in fichier.name:  # Vérifier si le nom est dans le nom de fichier
                for ligne in fichier:
                    occurence = count_TF(ligne, occurence)
    fichier.close()
    return occurence

def TF_president(repertoire, name):
    occurence = {}
    # On crée un dictionnaire qui contiendra le nombre d'occurences de chaque mot pour chaque président
    for i in files_names:   # Pour chaque document, on parcourt les fichiers et on compte le nombre d'occurences de chaque mot grâce à la fonction count_TF
        with open(repertoire+"/" + i, "r") as fichier:
            if name in fichier.name:  # Vérifier si le nom est dans le nom de fichier
                for ligne in fichier:
                    occurence = count_TF(ligne, occurence)
    fichier.close()
    return occurence

def liste_totale(repertoire, option):
    L1,L2,L3,L4,L5,L6,L7,L8 = [],[],[],[],[],[],[],[]
    # On crée une liste pour chaque texte, chaque liste contenant l'ensemble des mots de chaque texte
    n = 0
    # On initialise une variable n pour séléctionner les listes ci dessus
    for i in files_names:
        # On parcours l'ensemble des fichiers
        L = [L1,L2,L3,L4,L5,L6,L7,L8]
        # On crée une liste qui contient les listes L1 à L8 pour pouvoir les remplir
        with open(repertoire+"/" + i, "r") as f1:
             for phrase in f1:
                for word in separe_chaine(phrase):
                    if word not in L[n]:
                        L[n].append(word)
              # Les deux "for" permettent de prendre chaque mot individuellement, puis les ajouter aux listes L1 à L8 en fonction du fichier
        n+=1
    Liste = set(L1+L2+L3+L4+L5+L6+L7+L8)
    Liste = tri_selection(list(Liste))
        # On incrémente la variable n pour pouvoir passer de L1 à L2, puis à L3 etc...
    # On crée un set avec toutes les valeurs de L1, L2, etc... pour éliminer les doublons, puis on la convertit en liste et on la trie grâce à la fonction "tri_selection"
    f1.close()
    if option == 0:
        return Liste
    else:
        return L
    # En fonction du paramètre "option", on retourne soit la liste contenant l'ensemble des mots du corpus de texte sans les doublons, soit la liste L contenant l'ensemble des mots de chaque texte 
    
def IDF(repertoire):
    Liste = liste_totale(repertoire, 0)
    L = liste_totale(repertoire,1)
    dico_mot = {}
    # On initialise 2 variables Liste et L qui contiennent respectivement l'ensemble des mots du corpus de texte et l'ensemble des mots dans chaque texte
    dico_mot = {}    
    # On initialise un dictionnaire dico_mot qui contiendra le nombre de texte dans lequel est chaque mot
    for j in Liste:
        cpt = 0
        for h in range(0, 8):
            if j in L[h]:
                cpt += 1
        dico_mot[j] = cpt
    dico_idf = {}
    # On compte le nombre de texte dans lequel est chaque mot et on ajoute cette valeur dans le dictionnaire
    # On initialise un dictionnaire dico_idf qui contiendra les scores IDF de chaque mot.
    for k in dico_mot:
        score = log10(len(files_names)/(dico_mot[k]))
        dico_idf[k] = score
    return dico_idf
    # On calcule le score IDF pour chaque mot et on les ajoute dans le dictionnaire qu'on retourne juste après

def score_final(repertoire):
    Liste_totale = liste_totale(repertoire_cleaned, 0) #liste de tout les mots de tout les fichiers réunis
    dico_idf = IDF(repertoire_cleaned) #dictionnaire de toutes les valeurs de IDF
    TFIDF = []# On initialise une liste qui contiendra les scores finaux de chaque mot pour chaque texte
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

def transpose_matrice(matrice):
    # Trouver le nombre de lignes et de colonnes dans la matrice
    ligne = len(matrice)
    colonne = len(matrice[0])
    transposee = [] # Initialiser une nouvelle matrice pour la transposée
    for j in range(colonne): # Parcourir les colonnes de la matrice d'entrée
        nligne = []# Initialiser une nouvelle ligne pour chaque colonne
        for i in range(ligne): # Parcourir les lignes de la matrice d'entrée
            nligne.append(matrice[i][j])# Ajouter les éléments transposés à la nouvelle ligne
        transposee.append(nligne)# Ajouter la nouvelle ligne à la matrice transposée
    return transposee