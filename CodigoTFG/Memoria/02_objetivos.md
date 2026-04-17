Objetivo general:

Desarrollar una aplicación capaz de detectar el riesgo emocional en textos escritos por usuarios mediante técnicas de procesamiento del lenguaje natural (NLP) y aprendizaje automático, accesible a través de una API web y con almacenamiento de predicciones para su análisis posterior.


Objetivos específicos:

1.Preparación del entorno de desarrollo:
Se creó la estructura de carpetas del proyecto en Visual Studio Code, organizando los distintos módulos del sistema.
Se configuró y activó un entorno virtual (venv) para gestionar las dependencias del proyecto.
Se instalaron las librerías necesarias, como pandas, scikit-learn, spaCy, FastAPI y Uvicorn.

2.Preprocesamiento de datos:
Se cargó un dataset inicial compuesto por textos etiquetados según su nivel de riesgo emocional.
Se implementó la función limpiar_y_lemmatizar para normalizar los textos, aplicando conversión a minúsculas, eliminación de stopwords y lematización.
Se realizaron pruebas para validar el correcto funcionamiento del preprocesamiento.

3.Entrenamiento del modelo de Machine Learning:
Se transformaron los textos en vectores numéricos mediante TF-IDF.
Se entrenó un modelo de clasificación Multinomial Naive Bayes para detectar el nivel de riesgo emocional (bajo, medio, alto).
Se evaluó el modelo utilizando métricas como precisión, recall y F1-score.
Se guardaron el modelo y el vectorizador en archivos (model.pkl y vectorizer.pkl) para su posterior uso en la aplicación.

4.Desarrollo de la API REST con FastAPI:
Se crearon endpoints para comprobar el estado de la API y realizar predicciones de riesgo emocional.
Se integraron el preprocesamiento y el modelo entrenado dentro de la API.
Se configuraron rutas absolutas y manejo de errores para garantizar el correcto funcionamiento del sistema.

5.Implementación de funcionalidades de la aplicación:
Se permitió al usuario introducir texto a través de una interfaz web.
Se implementó el análisis automático del texto y su clasificación según el nivel de riesgo emocional.
Se mostró el resultado junto con la probabilidad asociada a cada predicción.
Se registraron las predicciones y el feedback del usuario en una base de datos SQLite.
Cada predicción enviada por el usuario se almacena automáticamente en SQLite.
Se guardan: texto original, nivel de riesgo predicho, confianza de la predicción y feedback del usuario (si lo proporciona).
Esto permite analizar el rendimiento del modelo con datos reales y planificar mejoras futuras.

6.Mejora de la visualización de resultados:
Se ha mejorado la interfaz de usuario mediante la incorporación de elementos visuales dinámicos, como una codificación por colores y una barra de progreso, con el objetivo de facilitar la interpretación del nivel de riesgo emocional y mejorar la experiencia del usuario.

7.Automatización del sistema:
Se implementó un sistema de automatización mediante un archivo .bat que permite la ejecución completa de la aplicación con un único comando. Este script inicia el entorno virtual, lanza la API REST desarrollada con FastAPI y pone en marcha un servidor HTTP local en Python para servir la interfaz web.
Esta automatización elimina la necesidad de ejecutar manualmente múltiples procesos y reduce la dependencia de herramientas del entorno de desarrollo, mejorando la usabilidad y la experiencia de ejecución del sistema.

8.Pruebas y validación del sistema:
Se realizaron pruebas del preprocesamiento con textos de ejemplo.
Se verificó el rendimiento del modelo utilizando un conjunto de datos de prueba.
Se comprobó el correcto funcionamiento de la API mediante testeo de los endpoints.
Se realizaron pruebas de integración completa del sistema, validando el flujo end-to-end. Se comprobó que la interfaz web funciona correctamente mediante el servidor HTTP local en Python, que las peticiones se envían a la API y que el modelo devuelve y muestra las predicciones de forma correcta.