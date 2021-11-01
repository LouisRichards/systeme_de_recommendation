import numpy as np
import pandas as pd
from tqdm import tqdm

produits = pd.read_csv(r'bdd\produits.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)
normes = pd.read_csv(r'bdd\normes.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)


def similarite_cosinus(item_a, item_b):
    return produits.values[item_a][item_b] / normes.values[item_a][item_b]

def enregistrer(nom_fichier):
    donnees = []

    for item_a in tqdm(range(produits.shape[0])):
        for item_b in range(produits.shape[0]):
            donnees.append(similarite_cosinus(item_a, item_b))

    similarites = pd.DataFrame(np.array_split(donnees, produits.shape[0]))

    similarites.to_csv(nom_fichier, sep='\t')


enregistrer('bdd/similarite_cosinus.csv')