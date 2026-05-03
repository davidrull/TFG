# Importamos librerías
import os
import pickle

# Obtenemos la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Rutas del modelo y vectorizador
model_path = os.path.join(BASE_DIR, "models", "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

# Cargamos el modelo
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Cargamos el vectorizador
with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)


# TEXTOS DE PRUEBA


pruebas = [
    "Estoy muy feliz y motivado",
    "Me siento fatal hoy",
    "No quiero hacer nada",
    "Todo está perfecto en mi vida",
    "Estoy muy ansioso y preocupado"
]

print("\n🔍 PRUEBAS DEL MODELO\n")


# REALIZAR PREDICCIONES


for texto in pruebas:

    # Convertimos el texto a vector
    vector = vectorizer.transform([texto])

    # Predicción del modelo
    pred = model.predict(vector)[0]

    # Probabilidad de la predicción
    prob = model.predict_proba(vector).max()

    # Mostramos resultados
    print("Texto:", texto)
    print("Predicción:", pred)
    print("Confianza:", round(prob, 2))
    print("-" * 40)