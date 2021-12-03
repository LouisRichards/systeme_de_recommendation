import pandas as pd
from tqdm import tqdm


bdd = pd.read_csv(r'bdd\incomplet.csv', delimiter='\t').dropna(axis=1).transpose()
bdd_complet = pd.read_csv(r'bdd\complet.csv', delimiter='\t').dropna(axis=1).transpose()
similarite_cosinus = pd.read_csv(r'bdd\similarite_cosinus.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)
similarite_pearson = pd.read_csv(r'bdd\similarite_pearson.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)
moyenne_item = pd.read_csv(r'bdd\moyenne_item.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)


def agregation(item, utilisateur, similarite):

    numerateur, denominateur = 0, 0

    for c_item in range(bdd.shape[0]):
        note_c_item = bdd.values[c_item][utilisateur]
        if note_c_item != -1:
            numerateur += similarite.values[item][c_item] * note_c_item
            denominateur += similarite.values[item][c_item]
    return numerateur/denominateur


def severite(item, utilisateur, similarite):

    numerateur, denominateur = 0, 0

    for c_item in range(bdd.shape[0]):
        note_c_item = bdd.values[c_item][utilisateur]
        if note_c_item != -1:
            numerateur += similarite.values[item][c_item] * \
                          (note_c_item - moyenne_item.values[c_item])
            denominateur += similarite.values[item][c_item]

    return moyenne_item.values[item] + (numerateur/denominateur)


def enregistrer_agregation(nom_fichier, similarite):

    for item in tqdm(range(bdd.shape[0])):
        for utilisateur in range(bdd.shape[1]):
            if bdd.values[item][utilisateur] == -1:
                bdd.iat[item, utilisateur] = agregation(item, utilisateur, similarite)

    bdd.to_csv(nom_fichier, sep='\t')


def enregistrer_severite(nom_fichier, similarite):
    for item in tqdm(range(bdd.shape[0])):
        for utilisateur in range(bdd.shape[1]):
            if bdd.values[item][utilisateur] == -1:
                bdd.iat[item, utilisateur] = severite(item, utilisateur, similarite)

    bdd.to_csv(nom_fichier, sep='\t')


def evaluation_biais(bdd_complet_sim):

    numerateur, denominateur = 0, 0

    for item in range(bdd_complet_sim.shape[0]):
        for utilisateur in range(bdd_complet_sim.shape[1]):
            if bdd.values[item][utilisateur] == -1:
                numerateur += bdd_complet_sim.values[item][utilisateur] - bdd_complet.values[item][utilisateur]
                denominateur += 1

    return numerateur/denominateur


def erreur_moyenne(bdd_complet_sim):

    numerateur, denominateur = 0, 0

    for item in range(bdd_complet_sim.shape[0]):
        for utilisateur in range(bdd_complet_sim.shape[1]):
            if bdd.values[item][utilisateur] == -1:
                numerateur += abs(bdd_complet_sim.values[item][utilisateur] - bdd_complet.values[item][utilisateur])
                denominateur += 1

    return numerateur / denominateur


print(evaluation_biais(complet))