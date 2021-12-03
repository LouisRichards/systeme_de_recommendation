import numpy as np
import pandas as pd

bdd = pd.read_csv(r'bdd\incomplet.csv', delimiter='\t').dropna(axis=1)


def norme_utilisateurs(utilisateur_a, utilisateur_b):

    somme_a, somme_b = 0, 0

    for item in range(bdd.shape[1]):
        note_utilisateur_a, note_utilisateur_b = bdd.values[utilisateur_a][item], bdd.values[utilisateur_b][item]
        if note_utilisateur_a != -1 and note_utilisateur_b != -1:
            somme_a += note_utilisateur_a**2
            somme_b += note_utilisateur_b**2

    return np.sqrt(somme_a) * np.sqrt(somme_b)


def produit_utilisateurs(utilisateur_a, utilisateur_b):

    produit = 0

    for item in range(bdd.shape[1]):
        note_utilisateur_a, note_utilisateur_b = bdd.values[utilisateur_a][item], bdd.values[utilisateur_b][item]
        if note_utilisateur_a != -1 and note_utilisateur_b != -1:
            produit += note_utilisateur_a * note_utilisateur_b

    return produit


def moyenne_utilisateurs(utilisateur_a, utilisateur_b):

    somme, nb_note = 0, 0

    for item in range(bdd.shape[1]):
        note_utilisateur_a, note_utilisateur_b = bdd.values[utilisateur_a][item], bdd.values[utilisateur_b][item]
        if note_utilisateur_a != -1 and note_utilisateur_b != -1:
            somme += note_utilisateur_a
            nb_note += 1

    return somme/nb_note


def moyenne_utilisateur(utilisateur):

    somme, nb_note = 0, 0

    for item in range(bdd.shape[1]):
        note_utilisateur = bdd.values[utilisateur][item]
        if note_utilisateur != -1:
            somme += note_utilisateur
            nb_note += 1

    return somme/nb_note


def enregistrer_normes(nom_fichier):

    donnees = []

    for utilisateur_a in range(bdd.shape[0]):
        for utilisateur_b in range(bdd.shape[0]):
            donnees.append(norme_utilisateurs(utilisateur_a, utilisateur_b))

    normes = pd.DataFrame(np.array_split(donnees, bdd.shape[0]))

    normes.to_csv(nom_fichier, sep='\t')


def enregistrer_produits(nom_fichier):
    donnees = []

    for utilisateur_a in range(bdd.shape[0]):
        for utilisateur_b in range(bdd.shape[0]):
            donnees.append(produit_utilisateurs(utilisateur_a, utilisateur_b))

    produits = pd.DataFrame(np.array_split(donnees, bdd.shape[0]))

    produits.to_csv(nom_fichier, sep='\t')


def enregistrer_moyennes_2utilisateurs(nom_fichier):
    donnees = []

    for utilisateur_a in range(bdd.shape[0]):
        for utilisateur_b in range(bdd.shape[0]):
            donnees.append(moyenne_utilisateurs(utilisateur_a, utilisateur_b))

    moyennes = pd.DataFrame(np.array_split(donnees, bdd.shape[0]))

    moyennes.to_csv(nom_fichier, sep='\t')

def enregistrer_moyennes_1utilisateur(nom_fichier):
    donnees = []

    for utilisateur in range(bdd.shape[0]):
        donnees.append(moyenne_utilisateur(utilisateur))

    moyennes = pd.DataFrame(donnees)

    moyennes.to_csv(nom_fichier, sep='\t')

