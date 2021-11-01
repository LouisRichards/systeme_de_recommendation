import pandas as pd
from tqdm import tqdm

bdd = pd.read_csv(r'bdd\incomplet.csv', delimiter='\t').dropna(axis=1)
bdd_complet = pd.read_csv(r'bdd\complet.csv', delimiter='\t').dropna(axis=1)
similarite_cosinus = pd.read_csv(r'bdd\similarite_cosinus.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)
similarite_pearson = pd.read_csv(r'bdd\similarite_pearson.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)
moyenne_utilisateur = pd.read_csv(r'bdd\moyenne_utilisateur.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)
complet_agregation_cosinus = pd.read_csv(r'bdd\complet_agregation_cosinus.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)
complet_severite_cosinus = pd.read_csv(r'bdd/complet_severite_cosinus.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)
complet_agregation_pearson = pd.read_csv(r'bdd\complet_agregation_pearson.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)
complet_severite_pearson = pd.read_csv(r'bdd/complet_severite_pearson.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)


def agregation(utilisateur, item, similarite):

    numerateur, denominateur = 0, 0

    for c_utilisateur in range(bdd.shape[0]):
        note_c_utilisateur = bdd.values[c_utilisateur][item]
        if note_c_utilisateur != -1:
            numerateur += similarite.values[utilisateur][c_utilisateur] * note_c_utilisateur
            denominateur += similarite.values[utilisateur][c_utilisateur]
    return numerateur/denominateur


def severite(utilisateur, item, similarite):

    numerateur, denominateur = 0, 0

    for c_utilisateur in range(bdd.shape[0]):
        note_c_utilisateur = bdd.values[c_utilisateur][item]
        if note_c_utilisateur != -1:
            numerateur += similarite.values[utilisateur][c_utilisateur] * \
                          (note_c_utilisateur - moyenne_utilisateur.values[c_utilisateur])
            denominateur += similarite.values[utilisateur][c_utilisateur]

    return moyenne_utilisateur.values[utilisateur] + (numerateur/denominateur)


def enregistrer_agregation(nom_fichier, similarite):

    for utilisateur in tqdm(range(bdd.shape[0])):
        for item in range(bdd.shape[1]):
            if bdd.values[utilisateur][item] == -1:
                bdd.iat[utilisateur, item] = agregation(utilisateur, item, similarite)

    bdd.to_csv(nom_fichier, sep='\t')


def enregistrer_severite(nom_fichier, similarite):
    for utilisateur in tqdm(range(bdd.shape[0])):
        for item in range(bdd.shape[1]):
            if bdd.values[utilisateur][item] == -1:
                bdd.iat[utilisateur, item] = severite(utilisateur, item, similarite)

    bdd.to_csv(nom_fichier, sep='\t')


def evaluation_biais(bdd_complet_sim):

    numerateur, denominateur = 0, 0

    for utilisateur in range(bdd_complet_sim.shape[0]):
        for item in range(bdd_complet_sim.shape[1]):
            if bdd.values[utilisateur][item] == -1:
                numerateur += bdd_complet_sim.values[utilisateur][item] - bdd_complet.values[utilisateur][item]
                denominateur += 1

    return numerateur/denominateur


def erreur_moyenne(bdd_complet_sim):

    numerateur, denominateur = 0, 0

    for utilisateur in range(bdd_complet_sim.shape[0]):
        for item in range(bdd_complet_sim.shape[1]):
            if bdd.values[utilisateur][item] == -1:
                numerateur += abs(bdd_complet_sim.values[utilisateur][item] - bdd_complet.values[utilisateur][item])
                denominateur += 1

    return numerateur / denominateur


