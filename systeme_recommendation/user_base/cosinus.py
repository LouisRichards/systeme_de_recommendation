import outils as o
import numpy as np
import pandas as pd
from tqdm import tqdm


def cosinus(userA, userB):  # calcul la similarite de deux utilisateurs par la methode de cosinus
    return o.produitUser(userA, userB)/(o.normUser(userA, userB))


def create(file):

    data = []

    for i in tqdm(range(0, 100)):
        for j in range(0, 100):
            data.append(round(cosinus(i, j), 5))

    matriceData = pd.DataFrame(np.array_split(data, 100))

    matriceData.to_csv(file, sep='\t')
