import outils as o
import numpy as np
import pandas as pd
from tqdm import tqdm


def cosinus(filmA, filmB):  # calcul la similarite de deux utilisateurs par la methode de cosinus
    return o.produitfilm(filmA, filmB)/(o.normfilm(filmA, filmB))


def create(file):

    data = []

    for i in tqdm(range(0, 1000)):
        for j in range(0, 1000):
            data.append(round(cosinus(i, j), 5))

    matriceData = pd.DataFrame(np.array_split(data, 1000))

    matriceData.to_csv(file, sep='\t')
