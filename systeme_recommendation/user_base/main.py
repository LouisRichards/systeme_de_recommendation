import pandas as pd
from tqdm import tqdm


def rename_array(array):
    for i in range(0, 1000):
        array.columns.values[i] = i

    array.columns.values[1000] = 1000
    return array


# stock les tableaux de donnees dans des variables
incomplet = pd.DataFrame(rename_array(pd.read_csv(
    r'BDD\toy_incomplet.csv', delimiter='\t'))).dropna(axis=1)

complet = pd.DataFrame(rename_array(pd.read_csv(
    r'BDD\toy_complet.csv', delimiter='\t'))).dropna(axis=1)

simCos = pd.read_csv(r'BDD\simCos.csv', delimiter='\t').drop(
    ['Unnamed: 0'], axis=1)

simPr = pd.read_csv(r'BDD\simPr.csv', delimiter='\t').drop(
    ['Unnamed: 0'], axis=1)

data_agregation_cos = pd.read_csv(
    r'data\data_agregation_cos.csv', delimiter='\t').drop(
    ['Unnamed: 0'], axis=1)

data_severite_cos = pd.read_csv(r'data\data_severite_cos.csv', delimiter='\t').drop(
    ['Unnamed: 0'], axis=1)

data_agregation_pr = pd.read_csv(
    r'data\data_agregation_pr.csv', delimiter='\t').drop(
    ['Unnamed: 0'], axis=1)

data_severite_pr = pd.read_csv(r'data\data_severite_pr.csv', delimiter='\t').drop(
    ['Unnamed: 0'], axis=1)

moyenne = pd.read_csv(r'BDD\moyenne.csv', delimiter='\t').drop(
    ['Unnamed: 0'], axis=1)


# predit la note que l'utilisateur user donnerait au film en utilisant la similarite sim
def agregation(user, film, sim):
    # initialization du numerateur et du denominateur
    numerateur = 0
    denominateur = 0

    for j in range(0, 100):  # parcours les utilisateurs
        # stock la note de utilisateur j pour le film dans une variable
        note_user_j = incomplet.values[j][film]
        if note_user_j != -1:  # si il y a une note alors...
            # concatene la similarite entre utilisateur user et utilisateur j multiplie par la note de J
            numerateur += sim.values[user][j] * note_user_j
            # concatene la similarite entre utilisateur user et utilisateur j
            denominateur += sim.values[user][j]
    return numerateur / denominateur  # sinon...

# predit la note d'un film donne par l'utilisateur avec le methode severite
def severite(user, film, sim):
    # initialization du numerateur et du denominateur
    numerateur = 0
    denominateur = 0

    for j in range(0, 100):  # parcours les utilisateurs
        # stock la note de utilisateur j pour le film dans une variable
        note_user_j = incomplet.values[j][film]
        if note_user_j != -1:  # si il n'y a pas de note alors...
            # concatene la similarite entre utilisateur user et utilisateur j
            # multiplie par la note de J moins la moyenne.csv des notes de l'utilisateur J
            numerateur += sim.values[user][j] * \
                          (note_user_j - moyenne.values[j][0])
            # concatene la similarite entre utilisateur user et utilisateur j
            denominateur += sim.values[user][j]
    # si le resultat est negatif alors retourner 0
    # sinon...
    return moyenne.values[user][0] + (numerateur / denominateur)


def completer_agregation(sim):  # complete le tableau incomplet avec la methode de agregation et la similarite sim donnee
    for i in tqdm(range(0, 100)):
        for j in range(0, 1000):
            if incomplet.values[i][j] == -1:
                incomplet.iat[i, j] = agregation(i, j, sim)

    incomplet.to_csv('data/data_agregation_pr.csv', sep='\t')


def completer_severite(sim):  # complete le tableau incomplet avec la methode de severite et la similarite sim donnee
    for i in tqdm(range(0, 100)):  # parcours chaque utilisateur
        for j in range(0, 1000):  # parcours chaque film
            # si l'utilisateur n'a pas note le film alors...
            if incomplet.values[i][j] == -1:
                # remplace la note par la prediction par la technique de severite
                incomplet.iat[i, j] = severite(i, j, sim)

    # enregistre le tableau dans une BDD csv en separent les valeurs par des espaces
    incomplet.to_csv('data/data_severite_pr.csv', sep='\t')


def eval_biais(bdd):
    numerateur = 0
    denominateur = 0

    for i in tqdm(range(0, 100)):
        for j in range(0, 1000):
            if incomplet.values[i][j] == -1:
                numerateur += bdd.values[i][j] - complet.values[i][j]
                denominateur += 1

    return numerateur / denominateur


def erreur_moyenne(bdd):  # calcul l'erreur moyenne entre la prediction et la vraie valeur
    numerateur = 0
    denominateur = 0

    for i in tqdm(range(0, 100)):
        for j in range(0, 1000):
            if incomplet.values[i][j] == -1:
                numerateur += abs(bdd.values[i][j] - complet.values[i][j])
                denominateur += 1

    return numerateur / denominateur


def suggest(user):  # sugere les 10 premiers film qui ont une note superieur a 3.5
    data = []
    nb_film = 0

    for i in range(0, 1000):
        if nb_film < 10:
            if incomplet.values[user][i] == -1:
                if data_severite_pr.values[user][i] > 3.5:
                    data.append(i)
                    nb_film += 1
        else:
            break

    return data



