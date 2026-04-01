# Importamos FastAPI para crear la API
from fastapi import FastAPI

# Importamos BaseModel de Pydantic para definir la estructura de los datos
# que recibirá nuestra API (validación automática)
from pydantic import BaseModel

# Librerías estándar de Python
import os
import pickle
import sys

# CONFIGURACIÓN DE IMPORTACIONES
# Añadimos la carpeta src al PATH de Python.
# Esto permite importar módulos internos del proyecto
# como por ejemplo ML.my_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importamos la función que limpia y lematiza el texto
# (preprocesamiento antes de pasarlo al modelo)
from ML.my_utils import limpiar_y_lemmatizar

# Importamos funciones para trabajar con SQLite
from Db.database import crear_tabla, guardar_prediccion


# CREACIÓN DE LA API
# Inicializamos la aplicación FastAPI
# El título aparecerá en la documentación automática
app = FastAPI(title="API Riesgo Emocional")


# MODELO DE DATOS DE ENTRADA (PYDANTIC)
# Este modelo define cómo debe ser el JSON que envíe el usuario
# FastAPI validará automáticamente que el campo exista y sea string
# Se añade feedback opcional
class TextoRequest(BaseModel):
    texto: str
    feedback: str = None  # Opcional, puede enviar comentario del usuario


# RUTAS DEL PROYECTO
# Obtenemos la ruta base del proyecto dinámicamente
# Esto evita problemas si movemos el proyecto de carpeta
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Construimos las rutas completas hacia los archivos del modelo
model_path = os.path.join(BASE_DIR, "models", "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")


# CARGA DEL MODELO DE MACHINE LEARNING
# Cargamos el modelo entrenado previamente y el vectorizador
with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)


# CREAR TABLA EN SQLITE
# Si no existe, se crea la tabla predicciones automáticamente
crear_tabla()


# ENDPOINT DE PRUEBA
# Endpoint simple para comprobar que la API funciona
@app.get("/")
def home():
    return {"mensaje": "API funcionando correctamente"}


# ENDPOINT DE PREDICCIÓN
# Endpoint que recibe texto y devuelve una predicción del modelo
@app.post("/predict")
def predict(data: TextoRequest):

    # Extraemos el texto enviado por el usuario
    texto = data.texto

    # Limpiamos y lematizamos el texto
    texto_limpio = limpiar_y_lemmatizar(texto)

    # Transformamos el texto en un vector numérico
    vector = vectorizer.transform([texto_limpio])

    # Realizamos la predicción con el modelo
    pred = model.predict(vector)[0]

    # Obtenemos la probabilidad de la predicción
    prob = model.predict_proba(vector).max()

   
    # Guardamos la predicción y feedback del usuario
    guardar_prediccion(texto, pred, round(float(prob), 2), data.feedback)

    # Devolvemos el resultado en formato JSON, incluyendo feedback
    return {
        "texto": texto,
        "riesgo": pred,
        "confianza": round(float(prob), 2),
        "feedback_recibido": data.feedback
    }