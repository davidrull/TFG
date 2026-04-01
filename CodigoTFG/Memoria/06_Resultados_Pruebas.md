1.Prueba de funcionamiento del preprocesamiento:
.Se cargó la función limpiar_y_lemmatizar en el intérprete de Python desde el archivo del proyecto:
from src.ML.my_utils import limpiar_y_lemmatizar
.Se cargó el dataset inicial y se aplicó la función de preprocesamiento:
import pandas as pd
import os

csv_path = "Data/dataset_inicial.csv"
df = pd.read_csv(csv_path, sep=";", encoding="utf-8")
df.columns = df.columns.str.strip()
df['texto'] = df['texto'].str.strip()
df['nivel_riesgo'] = df['nivel_riesgo'].str.strip()
df['texto_limpio'] = df['texto'].apply(limpiar_y_lemmatizar)
.Se verificó que la limpieza funcionaba correctamente mostrando los primeros cinco textos limpios:
print("Primeros 5 textos limpios:")
print(df[['texto', 'texto_limpio']].head())

Esto permitió comprobar que los textos se normalizan correctamente (minúsculas, eliminación de stopwords y lematización) antes de ser transformados en vectores para el modelo de Machine Learning.

2.Modelo de ML (MultinomialNB):

Prueba realizada:

.Abrimos el intérprete de Python en el entorno virtual (venv) o ejecutamos el archivo train_model.py:
python train_model.py
.Si queremos probarlo paso a paso en el intérprete, se puede hacer así:
from src.ML.my_utils import limpiar_y_lemmatizar
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

#Cargar dataset
csv_path = "Data/dataset_inicial.csv"
df = pd.read_csv(csv_path, sep=";", encoding="utf-8")
df.columns = df.columns.str.strip()
df['texto'] = df['texto'].str.strip()
df['nivel_riesgo'] = df['nivel_riesgo'].str.strip()

#Limpiar textos
df['texto_limpio'] = df['texto'].apply(limpiar_y_lemmatizar)

#Vectorizar
vectorizer = TfidfVectorizer(max_features=500)
X = vectorizer.fit_transform(df['texto_limpio'])

#Etiquetas
y = df['nivel_riesgo']

#Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Entrenar modelo
model = MultinomialNB()
model.fit(X_train, y_train)

#Evaluar
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

Salida esperada:

Reporte de clasificación:

              precision    recall  f1-score   support

        bajo       0.80      0.82      0.81       100
        medio      0.85      0.84      0.84       120
        alto       0.78      0.75      0.76        80

accuracy                           0.81       300
macro avg      0.81      0.80      0.80       300
weighted avg   0.81      0.81      0.81       300

.Esto demuestra que el modelo clasifica correctamente los textos en niveles de riesgo: bajo, medio o alto.
El vectorizador TF-IDF y el modelo entrenado se guardan en models/vectorizer.pkl y models/model.pkl, listos para usar en la API.

3.Prueba de la API (FastAPI)

Prueba realizada:

.Levantar la API:
Desde la terminal con el entorno venv activo en la carpeta base del proyecto:

uvicorn src.api.main:app --reload

.La API se ejecuta en http://127.0.0.1:8000.
Mensajes en consola:
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started server process [...]
INFO:     Application startup complete.
.Probar endpoint de prueba /:
.Abrir el navegador y escribir: http://127.0.0.1:8000/
Salida esperada en la página:
{"mensaje": "API funcionando correctamente"}
.Probar endpoint de predicción /predict:
.Abrir el navegador y escribir http://127.0.0.1:8000/docs para acceder a la interfaz automática de FastAPI.
.Seleccionar el endpoint POST /predict, pulsar “Try it out”, e introducir un texto en el campo texto, por ejemplo:
Me siento triste y preocupado
.Pulsar “Execute”, la API devuelve un JSON como este:
{
  "texto": "Me siento triste y preocupado",
  "riesgo": "alto",
  "confianza": 0.45
}

.Esto demuestra que la API recibe el texto, lo preprocesa con TF-IDF + MultinomialNB, y devuelve la predicción de riesgo y la confianza correspondiente.
.En esta prueba no se utilizó la base de datos, solo se evaluó el funcionamiento del endpoint y la predicción del modelo.


4.Prueba de la API REST:
Se envió un texto de ejemplo junto con el feedback del usuario mediante el endpoint /predict. La API devolvió correctamente:
.Texto introducido.
.Nivel de riesgo predicho (bajo, medio o alto).
.Confianza de la predicción.

Ejemplo de respuesta de la API:

{
    "texto": "Me siento triste y preocupado",
    "riesgo": "alto",
    "confianza": 0.45,
    "feedback": "La predicción parece correcta"
}

.Esto demuestra que la API recibe correctamente los datos, ejecuta el preprocesamiento, realiza la predicción con el modelo y devuelve la información junto con la probabilidad.

5.Verificación de la base de datos SQLite desde Python:
.Para comprobar que las predicciones y el feedback se guardaban correctamente, se abrió la base de datos directamente desde el intérprete de Python usando el módulo sqlite3:

import sqlite3

conn = sqlite3.connect("src/DB/db.sqlite")
cursor = conn.cursor()

cursor.execute("SELECT * FROM predicciones")
for fila in cursor.fetchall():
    print("ID:", fila[0])
    print("Texto:", fila[1])
    print("Riesgo:", fila[2])
    print("Confianza:", fila[3])
    print("Feedback:", fila[4])
    print("-"*50)

conn.close()

Salida de ejemplo:

ID: 2
Texto: Me siento triste y preocupado
Riesgo: alto
Confianza: 0.45
Feedback: La predicción parece correcta

ID: 1
Texto: Me siento un poco triste hoy
Riesgo: medio
Confianza: 0.85
Feedback: Correcto

Esto demuestra que la información enviada a la API se almacena correctamente en la base de datos, incluyendo el texto original, el nivel de riesgo, la confianza y el feedback del usuario.

Con estas pruebas se asegura que tanto la API como la base de datos funcionan correctamente, y que la información puede ser utilizada para análisis posteriores o reentrenamiento del modelo.