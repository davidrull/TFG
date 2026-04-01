Objetivo general:

Desarrollar una aplicación capaz de detectar el riesgo emocional en textos escritos por usuarios mediante técnicas de procesamiento del lenguaje natural (NLP) y aprendizaje automático, accesible a través de una API web y con almacenamiento de predicciones para su análisis posterior.


Objetivos específicos:

Preparación del entorno de desarrollo:
Se creó la estructura de carpetas del proyecto en Visual Studio Code, organizando los distintos módulos del sistema.
Se configuró y activó un entorno virtual (venv) para gestionar las dependencias del proyecto.
Se instalaron las librerías necesarias, como pandas, scikit-learn, spaCy, FastAPI y Uvicorn.

Preprocesamiento de datos:
Se cargó un dataset inicial compuesto por textos etiquetados según su nivel de riesgo emocional.
Se implementó la función limpiar_y_lemmatizar para normalizar los textos, aplicando conversión a minúsculas, eliminación de stopwords y lematización.
Se realizaron pruebas para validar el correcto funcionamiento del preprocesamiento.

Entrenamiento del modelo de Machine Learning:
Se transformaron los textos en vectores numéricos mediante TF-IDF.
Se entrenó un modelo de clasificación Multinomial Naive Bayes para detectar el nivel de riesgo emocional (bajo, medio, alto).
Se evaluó el modelo utilizando métricas como precisión, recall y F1-score.
Se guardaron el modelo y el vectorizador en archivos (model.pkl y vectorizer.pkl) para su posterior uso en la aplicación.

Desarrollo de la API REST con FastAPI:
Se crearon endpoints para comprobar el estado de la API y realizar predicciones de riesgo emocional.
Se integraron el preprocesamiento y el modelo entrenado dentro de la API.
Se configuraron rutas absolutas y manejo de errores para garantizar el correcto funcionamiento del sistema.

Implementación de funcionalidades de la aplicación:
Se permitió al usuario introducir texto a través de una interfaz web.
Se implementó el análisis automático del texto y su clasificación según el nivel de riesgo emocional.
Se mostró el resultado junto con la probabilidad asociada a cada predicción.
Se registraron las predicciones y el feedback del usuario en una base de datos SQLite.

Pruebas y validación del sistema:
Se realizaron pruebas del preprocesamiento con textos de ejemplo.
Se verificó el rendimiento del modelo utilizando un conjunto de datos de prueba.
Se comprobó el correcto funcionamiento de la API mediante testeo de los endpoints.