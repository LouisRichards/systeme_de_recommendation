import numpy as np
import pandas as pd

bdd = pd.read_csv(r'bdd\incomplet.csv', delimiter='\t').dropna(axis=1)
moyennes = pd.read_csv(r'bdd\moyenne_utilisateurs.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)


def similarite_pearson(utilisateur_a, utilisateur_b):
    numerateur, somme_a, somme_b = 0, 0, 0

    moyenne_a, moyenne_b = moyennes.values[utilisateur_a][utilisateur_b], moyennes.values[utilisateur_b][utilisateur_a]

    for item in range(bdd.shape[1]):
        note_utilisateur_a, note_utilisateur_b = bdd.values[utilisateur_a][item], bdd.values[utilisateur_b][item]
        if note_utilisateur_a != -1 and note_utilisateur_b != -1:
            numerateur += (note_utilisateur_a - moyenne_a) * (note_utilisateur_b - moyenne_b)
            somme_a += (note_utilisateur_a - moyenne_a)**2
            somme_b += (note_utilisateur_b - moyenne_b)**2

    denominateur = np.sqrt(somme_a * somme_b)

    return numerateur/denominateur

def enregistrer(nom_fichier):
    donnees = []

    for utilisateur_a in range(bdd.shape[0]):
        for utilisateur_b in range(bdd.shape[0]):
            donnees.append(similarite_pearson(utilisateur_a, utilisateur_b))

    similarites = pd.DataFrame(np.array_split(donnees, bdd.shape[0]))

    similarites.to_csv(nom_fichier, sep='\t')

