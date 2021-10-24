import numpy as np
import pandas as pd
import outils as o
from tqdm import tqdm


def renameArray(array):
    for i in range(0, 1001):
        array.columns.values[i] = i

    array.columns.values[1000] = 1000
    return array


# stock les tableaux de donnees dans des variables
incomplet = pd.DataFrame(renameArray(pd.read_csv(
    r'BDD\toy_incomplet.csv', delimiter='\t'))).dropna(axis=1)


def pearson(userA, userB):  # calcul la similarite de deux utilisateurs par la methode de pearson
    numerateur = 0

    moya = o.moyenneUserD(userA, userB)
    moyb = o.moyenneUserD(userB, userA)

    suma = 0
    sumb = 0

    for i in range(0, 1000):
        noteUserA = incomplet.values[userA][i]
        noteUserB = incomplet.values[userB][i]
        if (noteUserA != -1) and (noteUserB != -1):
            numerateur += ((noteUserA - moya) * (noteUserB - moyb))
            suma += ((noteUserA - moya)**2)
            sumb += ((noteUserB - moyb)**2)

    denominateur = np.sqrt(suma * sumb)

    return numerateur/denominateur


def create(file):

    data = []

    for i in tqdm(range(0, 100)):
        for j in range(0, 100):
            data.append(round(pearson(i, j), 5))

    matriceData = np.array_split(data, 100)

    similaritePearson = pd.DataFrame(matriceData)

    similaritePearson.to_csv(file, sep='\t')
