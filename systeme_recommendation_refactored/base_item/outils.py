import numpy as np
import pandas as pd
from tqdm import tqdm

bdd = pd.read_csv(r'bdd\incomplet.csv', delimiter='\t').dropna(axis=1).transpose()

def norme_items(item_a, item_b):

    somme_a, somme_b = 0, 0

    for utilisateur in range(bdd.shape[1]):
        note_item_a, note_item_b = bdd.values[item_a][utilisateur], bdd.values[item_b][utilisateur]
        if note_item_a != -1 and note_item_b != -1:
            somme_a += note_item_a**2
            somme_b += note_item_b**2

    return np.sqrt(somme_a) * np.sqrt(somme_b)

def produit_items(item_a, item_b):

    produit = 0

    for utilisateur in range(bdd.shape[1]):
        note_item_a, note_item_b = bdd.values[item_a][utilisateur], bdd.values[item_b][utilisateur]
        if note_item_a != -1 and note_item_b != -1:
            produit += note_item_a * note_item_b

    return produit

def moyenne_items(item_a, item_b):

    somme, nb_note = 0, 0

    for utilisateur in range(bdd.shape[1]):
        note_item_a, note_item_b = bdd.values[item_a][utilisateur], bdd.values[item_b][utilisateur]
        if note_item_a != -1 and note_item_b != -1:
            somme += note_item_a
            nb_note += 1

    return somme/nb_note

def moyenne_item(item):

    somme, nb_note = 0, 0

    for utilisateur in range(bdd.shape[1]):
        note_item = bdd.values[item][utilisateur]
        if note_item != -1:
            somme += note_item
            nb_note += 1

    return somme/nb_note

def enregistrer_normes(nom_fichier):

    donnees = []

    for item_a in tqdm(range(bdd.shape[0])):
        for item_b in range(bdd.shape[0]):
            donnees.append(norme_items(item_a, item_b))

    normes = pd.DataFrame(np.array_split(donnees, bdd.shape[0]))

    normes.to_csv(nom_fichier, sep='\t')



def enregistrer_produits(nom_fichier):
    donnees = []

    for item_a in tqdm(range(bdd.shape[0])):
        for item_b in range(bdd.shape[0]):
            donnees.append(produit_items(item_a, item_b))

    produits = pd.DataFrame(np.array_split(donnees, bdd.shape[0]))

    produits.to_csv(nom_fichier, sep='\t')


def enregistrer_moyennes_2items(nom_fichier):
    donnees = []

    for item_a in tqdm(range(bdd.shape[0])):
        for item_b in range(bdd.shape[0]):
            donnees.append(moyenne_items(item_a, item_b))

    moyennes = pd.DataFrame(np.array_split(donnees, bdd.shape[0]))

    moyennes.to_csv(nom_fichier, sep='\t')

def enregistrer_moyennes_1item(nom_fichier):
    donnees = []

    for item in tqdm(range(bdd.shape[0])):
        donnees.append(moyenne_item(item))

    moyennes = pd.DataFrame(donnees)

    moyennes.to_csv(nom_fichier, sep='\t')


enregistrer_moyennes_1item('bdd/moyenne_item.csv')

enregistrer_moyennes_2items('bdd/moyenne_items.csv')

enregistrer_produits('bdd/produits.csv')

enregistrer_normes('bdd/normes.csv')