import numpy as np
import pandas as pd
from tqdm import tqdm


def renameArray(array):
    for i in range(0, 1000):
        array.columns.values[i] = i

    array.columns.values[1000] = 1000
    return array


# stock les tableaux de donnees dans des variables
incomplet = pd.DataFrame(renameArray(pd.read_csv(
    r'BDD\toy_incomplet.csv', delimiter='\t'))).dropna(axis=1)


def normUser(userA, userB):  # calcul la norme d'utilisateur userA en verifiant userB pour les -1 en utilisant leur index

    suma = 0
    sumb = 0

    for i in range(0, 1000):  # parcours la matrice
        noteUserA = incomplet.values[userA][i]
        noteUserB = incomplet.values[userB][i]
        if (noteUserA != -1) and (noteUserB != -1):
            suma += (noteUserA**2)
            sumb += (noteUserB**2)

    return np.sqrt(suma) * np.sqrt(sumb)


def produitUser(userA, userB):  # calcul le produit entre deux utilisateurs a partir de leur index

    resultat = 0

    for i in range(0, 1000):
        noteUserA = incomplet.values[userA][i]
        noteUserB = incomplet.values[userB][i]
        if (noteUserA != -1) and (noteUserB != -1):
            resultat += noteUserA * noteUserB

    return resultat


def moyenneUser(user):  # calcul la moyenne.csv d'un utilisateurs a partir de son index
    sum = 0
    j = 0

    for i in range(0, 1000):
        noteUserJ = incomplet.values[user][i]
        if noteUserJ != -1:
            sum += noteUserJ
            j += 1

    return sum/j


def create_moyenne(file):
    data = []

    for i in tqdm(range(0, 100)):
        data.append(moyenneUser(i))

    moyenne = pd.DataFrame(data)

    moyenne.to_csv(file, sep='\t')


def moyenneUserD(userA, userB):

    sum = 0
    j = 0

    for i in range(0, 1000):
        noteUserA = incomplet.values[userA][i]
        noteUserB = incomplet.values[userB][i]
        if noteUserA != -1 and noteUserB != -1:
            sum += noteUserA
            j += 1

    return sum/j
