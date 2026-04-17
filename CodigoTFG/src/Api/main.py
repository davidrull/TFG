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

# NUEVO: Importamos CORS para permitir conexión con el frontend
from fastapi.middleware.cors import CORSMiddleware


# CREACIÓN DE LA API
# Inicializamos la aplicación FastAPI
# El título aparecerá en la documentación automática
app = FastAPI(title="API Riesgo Emocional")

# NUEVO: Configuración CORS (necesario para frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# MODELO DE DATOS DE ENTRADA (PYDANTIC)
# Este modelo define cómo debe ser el JSON que envíe el usuario
# FastAPI validará automáticamente que el campo exista y sea string
class TextoRequest(BaseModel):
    texto: str


# NUEVO: Modelo para el feedback del usuario
class FeedbackRequest(BaseModel):
    texto: str
    feedback: str


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

    # MODIFICADO: guardamos SIN feedback (ahora se hace en otro endpoint)
    guardar_prediccion(texto, pred, round(float(prob), 2), None)

    # MODIFICADO: ya no devolvemos feedback aquí
    return {
        "texto": texto,
        "riesgo": pred,
        "confianza": round(float(prob), 2)
    }


# NUEVO ENDPOINT
# Endpoint para guardar el feedback del usuario
@app.post("/feedback")
def feedback(data: FeedbackRequest):

    # Guardamos solo el feedback asociado al texto
    guardar_prediccion(data.texto, "N/A", 0.0, data.feedback)

    return {"mensaje": "Feedback guardado correctamente"}