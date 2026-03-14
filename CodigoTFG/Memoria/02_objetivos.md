Objetivo general:

Desarrollar una aplicación capaz de detectar el riesgo emocional en textos escritos por usuarios mediante técnicas de procesamiento del lenguaje natural (NLP) y aprendizaje automático, accesible a través de una API web y con almacenamiento de predicciones para su análisis posterior.

Objetivos específicos:

.Preparación del entorno de desarrollo
.Crear la estructura de carpetas del proyecto en Visual Studio.
.Configurar y activar un entorno virtual (venv) para gestionar dependencias.
.Instalar librerías necesarias: pandas, scikit-learn, spacy, fastapi, uvicorn.

Preprocesamiento de datos:
.Cargar un dataset inicial con textos y niveles de riesgo emocional.
.Implementar la función limpiar_y_lemmatizar para normalizar los textos (minúsculas, eliminación de stopwords, lematización).
.Probar y validar que la función de limpieza funciona correctamente.

Entrenamiento del modelo de Machine Learning:
.Transformar los textos limpios en vectores mediante TF-IDF.
.Entrenar un modelo de clasificación MultinomialNB para detectar riesgo emocional (bajo, medio, alto).
.Evaluar el modelo usando métricas de precisión, recall y F1-score.
.Guardar el modelo y el vectorizador en archivos (model.pkl y vectorizer.pkl) para su uso en la aplicación.

Desarrollo de la API REST con FastAPI:
.Crear endpoints para comprobar el estado de la API y predecir el riesgo emocional de un texto.
.Integrar la función de preprocesamiento y el modelo entrenado dentro de la API.
.Configurar rutas absolutas y manejo de errores para asegurar la carga correcta de los archivos.

Implementación de funcionalidades de la aplicación:
.Permitir al usuario introducir un texto en un formulario web.
.Analizar automáticamente el texto y clasificar su riesgo emocional.
.Visualizar el resultado junto con la probabilidad de cada categoría.
.Registrar las predicciones y el feedback del usuario en una base de datos SQLite.

Pruebas y validación del sistema:
.Probar la función de preprocesamiento con textos de ejemplo.
.Verificar la precisión del modelo de ML con el conjunto de prueba.
.Testear la API asegurando que los endpoints devuelven los resultados esperados.