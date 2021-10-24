import numpy as np
import pandas as pd
from tqdm import tqdm


def rename_array(array):
    for i in range(0, 1000):
        array.columns.values[i] = i

    array.columns.values[1000] = 1000
    return array


# stock les tableaux de donnees dans des variables
incomplet = pd.DataFrame(rename_array(pd.read_csv(
    r'BDD\toy_incomplet.csv', delimiter='\t'))).dropna(axis=1).transpose()


def normfilm(filmA, filmB):  # calcul la norme d'utilisateur filmA en verifiant filmB pour les -1 en utilisant leur index

    suma = 0
    sumb = 0

    for i in range(0, 100):  # parcours la matrice
        notefilmA = incomplet.values[filmA][i]
        notefilmB = incomplet.values[filmB][i]
        if (notefilmA != -1) and (notefilmB != -1):
            suma += (notefilmA**2)
            sumb += (notefilmB**2)

    return np.sqrt(suma) * np.sqrt(sumb)


def produitfilm(filmA, filmB):  # calcul le produit entre deux utilisateurs a partir de leur index

    resultat = 0

    for i in range(0, 100):
        notefilmA = incomplet.values[filmA][i]
        notefilmB = incomplet.values[filmB][i]
        if (notefilmA != -1) and (notefilmB != -1):
            resultat += notefilmA * notefilmB

    return resultat


def moyennefilm(film):  # calcul la moyenne.csv d'un utilisateurs a partir de son index
    sum = 0
    j = 0

    for i in range(0, 100):
        notefilmJ = incomplet.values[film][i]
        if notefilmJ != -1:
            sum += notefilmJ
            j += 1

    return sum/j


def create_moyenne(file):
    data = []

    for i in tqdm(range(0, 1000)):
        data.append(moyennefilm(i))

    moyenne = pd.DataFrame(data)

    moyenne.to_csv(file, sep='\t')


def moyennefilmD(filmA, filmB):

    sum = 0
    j = 0

    for i in range(0, 100):
        notefilmA = incomplet.values[filmA][i]
        notefilmB = incomplet.values[filmB][i]
        if notefilmA != -1 and notefilmB != -1:
            sum += notefilmA
            j += 1

    return sum/j