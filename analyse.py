import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventes.csv")
print(df.head())
#calcul nb ligne et colone
print("Nombre de lignes et colonnes:", df.shape)
print("Valeurs manquantes par colonne:")
print(df.isnull().sum())
# nettoyage de donnees
df = df.dropna()
print("Number of rows after cleaning:", df.shape)
# answer first question: the product bought the must
produit_populaire=df.groupby("produit")["quantite"].sum()
print("Ventes totales par produit: ")
print(produit_populaire)
print("Le produit le plus vendu est:", produit_populaire.idxmax())
# answer second question: the city were we sold the must
ville_populaire=df.groupby("ville")["quantite"].sum()
print("Ventes total par ville")
print(ville_populaire)
print("la ville ou on an vendu le plus : ", ville_populaire.idxmax())
# answer third question: the benefits
#1. calcul des revenus
df["revenu"]=df["quantite"]* df["prix"]
revenu_par_mois=df.groupby("mois")["revenu"].sum()
print("Revenu total par mois:")
print(revenu_par_mois)
# graphique
# Graphique 1: revenu par mois
plt.figure()
revenu_par_mois.plot(kind="bar", title="Revenu par mois")
plt.xlabel("Mois")
plt.ylabel("Revenu (DH)")
plt.tight_layout()
plt.savefig("graphique_revenu_mois.png")

# Graphique 2: quantite vendue par produit
plt.figure()
produit_populaire.plot(kind="bar", title="Quantite vendue par produit", color="orange")
plt.xlabel("Produit")
plt.ylabel("Quantite vendue")
plt.tight_layout()
plt.savefig("graphique_produits.png")

plt.show()


