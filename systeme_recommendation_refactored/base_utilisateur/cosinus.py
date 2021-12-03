import numpy as np
import pandas as pd


produits = pd.read_csv(r'bdd\produits.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)
normes = pd.read_csv(r'bdd\normes.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)


def similarite_cosinus(utilisateur_a, utilisateur_b):
    return produits.values[utilisateur_a][utilisateur_b] / normes.values[utilisateur_a][utilisateur_b]

def enregistrer(nom_fichier):
    donnees = []

    for utilisateur_a in range(produits.shape[0]):
        for utilisateur_b in range(produits.shape[0]):
            donnees.append(similarite_cosinus(utilisateur_a, utilisateur_b))

    similarites = pd.DataFrame(np.array_split(donnees, produits.shape[0]))

    similarites.to_csv(nom_fichier, sep='\t')


