import numpy as np
import pandas as pd
from tqdm import tqdm

bdd = pd.read_csv(r'bdd\incomplet.csv', delimiter='\t').dropna(axis=1).transpose()
moyennes = pd.read_csv(r'bdd\moyenne_items.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)


def similarite_pearson(item_a, item_b):
    numerateur, somme_a, somme_b = 0, 0, 0

    moyenne_a, moyenne_b = moyennes.values[item_a][item_b], moyennes.values[item_b][item_a]

    for utilisateur in range(bdd.shape[1]):

        note_item_a, note_item_b = bdd.values[item_a][utilisateur], bdd.values[item_b][utilisateur]

        if note_item_a != -1 and note_item_b != -1:
            numerateur += (note_item_a - moyenne_a) * (note_item_b - moyenne_b)
            somme_a += (note_item_a - moyenne_a)**2
            somme_b += (note_item_b - moyenne_b)**2

    denominateur = np.sqrt(somme_a * somme_b)

    return numerateur/denominateur

def enregistrer(nom_fichier):
    donnees = []

    for item_a in tqdm(range(bdd.shape[0])):
        for item_b in range(bdd.shape[0]):
            donnees.append(similarite_pearson(item_a, item_b))

    similarites = pd.DataFrame(np.array_split(donnees, bdd.shape[0]))

    similarites.to_csv(nom_fichier, sep='\t')



print(similarite_pearson(0, 1))
