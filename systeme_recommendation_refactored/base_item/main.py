import pandas as pd


complet_agregation_cosinus = pd.read_csv(r'bdd\complet_agregation_cosinus.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)
complet_severite_cosinus = pd.read_csv(r'bdd/complet_severite_cosinus.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)
complet_agregation_pearson = pd.read_csv(r'bdd\complet_agregation_pearson.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)
complet_severite_pearson = pd.read_csv(r'bdd/complet_severite_pearson.csv', delimiter='\t').drop(['Unnamed: 0'], axis=1)


def suggerer(bdd, utilisateur):
    suggestion = []
    suggere = 0

    for j in range(bdd.shape[1]):
        if bdd.values[utilisateur][j] > 3.5:
            if suggere < 10:
                suggestion.append(j)
                suggere += 1

    return suggestion


print("Que voulez-vous faire ?")
choix_sim = int(input("Cosinus ? (0), Pearson ? (1)\n"))

if choix_sim == 0:
    choix_methode = int(input("Agregation ? (0), Severite ? (1)\n"))
    if choix_methode == 0:
        choix_util = int(input("Quel utilisateur ? (0 a 100)\n"))
        print("Nous lui suggerons les films suivant : ", suggerer(complet_agregation_cosinus, choix_util))
    elif choix_methode == 1:
        choix_util = int(input("Quel utilisateur ? (0 a 100)\n"))
        print("Nous lui suggerons les films suivant : ", suggerer(complet_severite_cosinus, choix_util))
elif choix_sim == 1:
    choix_methode = int(input("Agregation ? (0), Severite ? (1)\n"))
    if choix_methode == 0:
        choix_util = int(input("Quel utilisateur ? (0 a 100)\n"))
        print("Nous lui suggerons les films suivant : ", suggerer(complet_agregation_pearson, choix_util))
    elif choix_methode == 1:
        choix_util = int(input("Quel utilisateur ? (0 a 100)\n"))
        print("Nous lui suggerons les films suivant : ", suggerer(complet_severite_pearson, choix_util))
