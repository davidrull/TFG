# Importamos librerías necesarias
import os
import pickle
from sklearn.metrics import classification_report, accuracy_score

# Obtenemos la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Rutas del modelo y vectorizador
model_path = os.path.join(BASE_DIR, "models", "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

# Cargamos el modelo entrenado
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Cargamos el vectorizador TF-IDF
with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)


# DATOS DE PRUEBA

# Textos de ejemplo para evaluar el modelo
texts = [
    "Estoy muy feliz hoy",
    "Me siento muy triste y sin ganas",
    "Todo me va bien",
    "Estoy preocupado por el futuro",
    "No tengo fuerzas para seguir"
]

# Etiquetas reales (simuladas para evaluación)
y_true = ["bajo", "alto", "bajo", "medio", "alto"]


# PREPROCESAMIENTO Y PREDICCIÓN


# Convertimos textos a formato numérico
X_test = vectorizer.transform(texts)

# Realizamos predicciones
y_pred = model.predict(X_test)


# EVALUACIÓN DEL MODELO


print("\n📊 EVALUACIÓN DEL MODELO\n")

# Exactitud del modelo
accuracy = accuracy_score(y_true, y_pred)
print("Accuracy:", accuracy)

# Informe completo de métricas
print("\nClassification Report:\n")
print(classification_report(y_true, y_pred))