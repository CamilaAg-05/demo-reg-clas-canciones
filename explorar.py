import pandas as pd

d = pd.read_csv("data/canciones.csv")
print("Forma:", d.shape)
print("\nNulos por columna:\n", d.isna().sum())
print("\nDuplicados:", d.duplicated().sum())
print("\nResumen (busque valores extremos):\n", d.describe().round(2))
print("\nCorrelación con popularidad:\n",
      d.corr(numeric_only=True)["popularidad"].sort_values().round(2))
print("\nMatriz de correlación (busque variables repetidas):\n",
      d.corr(numeric_only=True).round(2))