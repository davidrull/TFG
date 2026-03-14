import pandas as pd
from my_utils import limpiar_y_lemmatizar  # Importamos la función desde nuestro archivo
import os

# 1 Ruta del CSV
csv_path = "Data/dataset_inicial.csv"

# 2 Verificar que el CSV exista
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"No se encuentra el CSV en {csv_path}")

# 3 Cargar CSV
df = pd.read_csv(csv_path, sep=";", encoding="utf-8")

# 4 Limpiar nombres de columnas y quitar espacios extra
df.columns = df.columns.str.strip()
df['texto'] = df['texto'].str.strip()
df['nivel_riesgo'] = df['nivel_riesgo'].str.strip()

# 5 Aplicar limpieza
df['texto_limpio'] = df['texto'].apply(limpiar_y_lemmatizar)

# 6 Mostrar primeros 5 ejemplos
print("Primeros 5 textos limpios:")
print(df[['texto', 'texto_limpio']].head())

# df['texto'].apply(limpiar_y_lemmatizar)
# Aplica la función a cada fila de la columna texto y devuelve la columna nueva texto_limpio.

# print(df[['texto', 'texto_limpio']].head())
# Muestra los primeros 5 ejemplos, para verificar que la limpieza funciona.