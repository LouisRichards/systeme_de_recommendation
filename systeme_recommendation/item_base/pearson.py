import numpy as np
import pandas as pd
import outils as o
from tqdm import tqdm


def rename_array(array):
    for i in range(0, 1000):
        array.columns.values[i] = i

    array.columns.values[1000] = 1000
    return array


# stock les tableaux de donnees dans des variables
incomplet = pd.DataFrame(rename_array(pd.read_csv(
    r'BDD\toy_incomplet.csv', delimiter='\t'))).dropna(axis=1).transpose()


def pearson(filmA, filmB):  # calcul la similarite de deux utilisateurs par la methode de pearson
    numerateur = 0

    moya = o.moyennefilmD(filmA, filmB)
    moyb = o.moyennefilmD(filmB, filmA)

    suma = 0
    sumb = 0

    for i in range(0, 100):
        notefilmA = incomplet.values[filmA][i]
        notefilmB = incomplet.values[filmB][i]
        if (notefilmA != -1) and (notefilmB != -1):
            numerateur += ((notefilmA - moya) * (notefilmB - moyb))
            suma += ((notefilmA - moya)**2)
            sumb += ((notefilmB - moyb)**2)

    denominateur = np.sqrt(suma * sumb)

    return numerateur/denominateur


def create(file):

    data = []

    for i in tqdm(range(0, 1000)):
        for j in range(0, 1000):
            data.append(round(pearson(i, j), 5))

    matriceData = np.array_split(data, 1000)

    similaritePearson = pd.DataFrame(matriceData)

    similaritePearson.to_csv(file, sep='\t')