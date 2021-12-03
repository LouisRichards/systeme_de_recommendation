import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

base_utilisateur = np.array(pd.read_csv(
    r'base_utilisateur\bdd\erreurs_moyenne.csv', delimiter='\t'))

heatmap = sns.heatmap(base_utilisateur, cmap="YlGnBu")
plt.show()
