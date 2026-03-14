import pandas as pd


from my_utils import limpiar_y_lemmatizar  # función de limpieza
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import pickle
import os

# 1 Cargar dataset
csv_path = "Data/dataset_inicial.csv"
df = pd.read_csv(csv_path, sep=";", encoding="utf-8")

# 2 Limpiar nombres de columnas y quitar espacios
df.columns = df.columns.str.strip()
df['texto'] = df['texto'].str.strip()
df['nivel_riesgo'] = df['nivel_riesgo'].str.strip()

# 3 Limpiar textos
df['texto_limpio'] = df['texto'].apply(limpiar_y_lemmatizar)

# 4 Convertir textos a vectores TF-IDF
vectorizer = TfidfVectorizer(max_features=500)
X = vectorizer.fit_transform(df['texto_limpio'])

# 5 Etiquetas
y = df['nivel_riesgo']

# 6 Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7 Entrenar modelo
model = MultinomialNB()
model.fit(X_train, y_train)

# 8 Evaluar modelo
y_pred = model.predict(X_test)
print("Reporte de clasificación:\n")
print(classification_report(y_test, y_pred))

# 9 Guardar modelo y vectorizador para la app
os.makedirs("../../models", exist_ok=True)
with open("../../models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
with open("../../models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print(" Modelo y vectorizador guardados en carpeta 'models'")

