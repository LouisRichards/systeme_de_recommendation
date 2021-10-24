import pandas as pd
import cosinus as cos
import outils as o
from tqdm import tqdm


def rename_array(array):
    for i in range(0, 1000):
        array.columns.values[i] = i

    array.columns.values[1000] = 1000
    return array


# stock les tableaux de donnees dans des variables
incomplet = pd.DataFrame(rename_array(pd.read_csv(
    r'BDD\toy_incomplet.csv', delimiter='\t'))).dropna(axis=1).transpose()

complet = pd.DataFrame(rename_array(pd.read_csv(
    r'BDD\toy_complet.csv', delimiter='\t'))).dropna(axis=1).transpose()

simCos = pd.read_csv(r'BDD\simCos.csv', delimiter='\t').drop(
    ['Unnamed: 0'], axis=1)

simPr = pd.read_csv(r'BDD\simPr.csv', delimiter='\t').drop(
    ['Unnamed: 0'], axis=1)

moyenne = pd.read_csv(r'BDD\moyenne.csv', delimiter='\t').drop(
    ['Unnamed: 0'], axis=1)

data_agregation_cos = pd.read_csv(
    r'data\data_agregation_cos.csv', delimiter='\t').drop(
    ['Unnamed: 0'], axis=1)

data_severite_cos = pd.read_csv(r'data\data_severite_cos.csv', delimiter='\t').drop(
    ['Unnamed: 0'], axis=1)


# predit la note que l'film film donnerait au user en utilisant la similarite sim
def agregation(film, user, sim):

    # initialization du numerateur et du denominateur
    numerateur = 0
    denominateur = 0

    for film_n in range(0, 1000):  # parcours les films
        # stock la note de film j pour le user dans une variable
        note_film_j = incomplet.values[film_n][user]
        if note_film_j != -1:  # si il y a une note alors...
            # concatene la similarite entre film film et film j multiplie par la note de J
            numerateur += sim.values[film_n][film] * note_film_j
            # concatene la similarite entre film film et film j
            denominateur += sim.values[film_n][film]
    return numerateur/denominateur  # sinon...


def severite(film, user, sim):

    # initialization du numerateur et du denominateur
    numerateur = 0
    denominateur = 0

    for film_n in range(0, 1000):  # parcours les films
        # stock la note de film j pour le user dans une variable
        note_film_j = incomplet.values[film_n][user]
        if note_film_j != -1:  # si il n'y a pas de note alors...
            # concatene la similarite entre film film et film j
            # multiplie par la note de J moins la moyenne.csv des notes de l'film J
            numerateur += sim.values[film][film_n] * \
                (note_film_j - moyenne.values[film_n][0])
            # concatene la similarite entre film film et film j
            denominateur += sim.values[film][film_n]
            print(denominateur)
    # si le resultat est negatif alors retourner 0
    # sinon...
    return moyenne.values[film][0] + (numerateur/denominateur)


def completer_agregation(sim):
    for film in tqdm(range(0, 1000)):
        for user in range(0, 100):
            if incomplet.values[film][user] == -1:
                incomplet.iat[film, user] = agregation(film, user, sim)

    incomplet.to_csv('data/data_agregation_pr.csv', sep='\t')


def completer_severite(sim):
    for film in tqdm(range(0, 1000)):  # parcours chaque film
        for user in range(0, 100):  # parcours chaque user
            # si l'film n'a pas note le user alors...
            if incomplet.values[film][user] == -1:
                # remplace la note par la prediction par la technique de severite
                incomplet.iat[film, user] = severite(film, user, sim)

    # enregistre le tableau dans une BDD csv en separent les valeurs par des espaces
    incomplet.to_csv('data/data_severite_pr.csv', sep='\t')


def eval_biais(bdd):

    numerateur = 0
    denominateur = 0

    for film in tqdm(range(0, 1000)):
        for user in range(0, 100):
            if incomplet.values[film][user] == -1:
                numerateur += bdd.values[film][user] - complet.values[film][user]
                denominateur += 1

    return numerateur/denominateur


def erreur_moyenne(bdd):
    numerateur = 0
    denominateur = 0

    for film in tqdm(range(0, 1000)):
        for user in range(0, 100):
            if incomplet.values[film][user] == -1:
                numerateur += abs(bdd.values[film][user] - complet.values[film][user])
                denominateur += 1

    return numerateur/denominateur


print(severite(0, 1, simPr))
