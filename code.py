 
import os
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =============================
# Préparation du dossier résultats
# =============================
os.makedirs("resultats", exist_ok=True)

# =============================
# Définir les chemins des fichiers
# =============================
base_dir = Path(__file__).parent
file_list = [
    base_dir / "data" / "ankle_Series1_trial1.csv",
    base_dir / "data" / "ankle_Series1_trial2.csv",
    base_dir / "data" / "wrist_Series1_trial1.csv",
    base_dir / "data" / "wrist_Series1_trial2.csv"
]

# =============================
# Fonctions pour ENMO et MAD
# =============================
def calculate_enmo(x, y, z):
    enmo = np.sqrt(x**2 + y**2 + z**2) - 1
    enmo[enmo < 0] = 0
    return enmo

def calculate_mad(x, y, z):
    magnitude = np.sqrt(x**2 + y**2 + z**2)
    mad = np.mean(np.abs(magnitude - np.mean(magnitude)))
    return mad

# =============================
# Lire et combiner les fichiers
# =============================
dfs = []
for f in file_list:
    if not f.exists():
        print(f"Le fichier {f} n'existe pas. Ignoré.")
        continue
    
    # Lecture automatique du séparateur
    try:
        df = pd.read_csv(f, header=None, sep=None, engine='python', comment='#')
    except Exception as e:
        print(f"Erreur lecture {f.name} : {e}. Ignoré.")
        continue
    
    # Supprimer lignes vides
    df.dropna(how='all', inplace=True)
    
    # Vérifier le nombre de colonnes
    if df.shape[1] < 4:
        print(f"Le fichier {f.name} a moins de 4 colonnes. Ignoré.")
        continue
    if df.shape[1] > 4:
        df = df.iloc[:, :4]  # garder seulement les 4 premières colonnes
    
    # Renommer les colonnes
    df.columns = ["time", "x", "y", "z"]
    
    # Convertir x, y, z en float
    df[["x","y","z"]] = df[["x","y","z"]].astype(float)
    
    # Ajouter localisation
    df["location"] = "ankle" if "ankle" in f.name.lower() else "wrist"
    
    # Calculer ENMO et MAD
    df["ENMO"] = calculate_enmo(df["x"].values, df["y"].values, df["z"].values)
    df["MAD"] = calculate_mad(df["x"].values, df["y"].values, df["z"].values)
    
    dfs.append(df)

# Combiner tous les fichiers
if not dfs:
    raise ValueError("Aucun fichier valide n'a été trouvé.")
data = pd.concat(dfs, ignore_index=True)

# =============================
# Boxplot comparatif ENMO
# =============================
plt.figure(figsize=(8,5))
sns.boxplot(x="location", y="ENMO", data=data)
plt.title("Comparaison ENMO : Ankle vs Wrist")
plt.ylabel("ENMO (g)")
plt.savefig("resultats/comparaison_ENMO.png", dpi=300)
plt.show()  # Affiche le graphique

# =============================
# Boxplot comparatif MAD
# =============================
plt.figure(figsize=(8,5))
sns.boxplot(x="location", y="MAD", data=data)
plt.title("Comparaison MAD : Ankle vs Wrist")
plt.ylabel("MAD (g)")
plt.savefig("resultats/comparaison_MAD.png", dpi=300)
plt.show()  # Affiche le graphique

print("Les graphiques ont été générés, sauvegardés et affichés.")
