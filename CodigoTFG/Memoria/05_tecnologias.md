Tecnologías utilizadas:

Para el desarrollo de la aplicación se emplearon tecnologías modernas, ampliamente documentadas y compatibles con Python, que permiten cubrir todas las fases del proyecto: preprocesamiento, aprendizaje automático, API y almacenamiento de datos.

1.Lenguaje de programación:

.Python,elegido por su facilidad de uso, ecosistema de librerías y soporte para Machine Learning y NLP.
.Permite integrar de manera sencilla las distintas partes del proyecto (ML, API y base de datos).

2.Procesamiento de lenguaje natural (NLP):

.SpaCy,Para tokenización, lematización y eliminación de stopwords en español.
.my_utils.py (Archivo personalizado con la función limpiar_y_lemmatizar, reutilizable en todo el proyecto).

3.Aprendizaje automático:

.scikit-learn:
.TF-IDF Vectorizer: transforma textos en vectores numéricos.
.MultinomialNB: modelo de clasificación supervisada para detectar riesgo emocional.
.train_test_split y classification_report: para evaluar la precisión del modelo.
.pickle (Para guardar y cargar el modelo entrenado y el vectorizador).

4.API REST

FastAPI:
.Framework ligero y moderno para crear APIs REST(Facilita el envío de textos desde la interfaz web al modelo ML).
.Uvicorn(Servidor ASGI para ejecutar la API de forma rápida y eficiente).

5.Base de datos

SQLite:
.Base de datos relacional ligera para almacenar predicciones y feedback del usuario(No requiere instalación de servidores adicionales, ideal para proyectos locales).

6.Frontend:

.HTML / CSS / JavaScript(Interfaz sencilla para que el usuario introduzca textos y reciba los resultados).

7.Entorno de desarrollo:

.Visual Studio Code(Organización del proyecto y edición de código).
.Entorno virtual (venv) (Para aislar las dependencias del proyecto y garantizar compatibilidad).
