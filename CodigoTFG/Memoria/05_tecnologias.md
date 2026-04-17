Tecnologías utilizadas:

Para el desarrollo de la aplicación se emplearon tecnologías modernas, ampliamente documentadas y compatibles con Python, que permiten cubrir todas las fases del proyecto: preprocesamiento de texto, aprendizaje automático, desarrollo de la API y almacenamiento de datos.

1.Lenguaje de programación:
.Python: Elegido por su facilidad de uso, amplio ecosistema de librerías y soporte nativo para Machine Learning y procesamiento de lenguaje natural (NLP).
.Permite integrar de manera eficiente las distintas partes del proyecto: preprocesamiento, modelo de ML, API y base de datos.

2.Procesamiento de lenguaje natural (NLP):
.spaCy: Librería utilizada para tokenización, lematización y eliminación de stopwords en español, garantizando la normalización de los textos.
.my_utils.py: Archivo personalizado con la función limpiar_y_lemmatizar, que encapsula todo el preprocesamiento y puede reutilizarse en entrenamiento y predicción.

3.Aprendizaje automático:
.scikit-learn:
.TfidfVectorizer: Convierte textos limpios en vectores numéricos, necesarios para el modelo.
.MultinomialNB: Modelo de clasificación supervisada adecuado para datos de texto categorizados en riesgo bajo, medio o alto.
.train_test_split y classification_report: Herramientas para evaluar la precisión y fiabilidad del modelo.
.pickle: Se utilizó para guardar y cargar el modelo entrenado y el vectorizador, asegurando consistencia entre entrenamiento y API.

4.API REST:
.FastAPI: Framework ligero y moderno para crear APIs REST, que permite exponer el modelo ML a través de endpoints de manera eficiente.
.Uvicorn: Servidor ASGI para ejecutar la API, ofreciendo rapidez y soporte para recarga automática durante el desarrollo.

5.Base de datos:
.SQLite: Base de datos relacional ligera, utilizada para almacenar textos procesados, predicciones y feedback del usuario.
Ventajas: no requiere instalación de servidores adicionales y es ideal para proyectos locales y pruebas de prototipo.

6.Frontend:
HTML / CSS / JavaScript: Interfaz desarrollada para permitir la interacción del usuario con el sistema. El usuario introduce textos que son enviados a la API para su análisis, y los resultados se muestran de forma visual.
Se ha mejorado la experiencia de usuario mediante la incorporación de elementos visuales dinámicos, como codificación por colores y una barra de progreso que representa la confianza del modelo. Estas mejoras facilitan la interpretación del resultado sin necesidad de interpretar valores numéricos, aumentando la usabilidad del sistema.

7.Entorno de desarrollo:
.Visual Studio Code: Editor de código utilizado para organizar la estructura del proyecto y facilitar la edición del código.
.Entorno virtual (venv): Se emplea para aislar las dependencias del proyecto y garantizar compatibilidad entre distintos entornos de desarrollo.
.Automatización (.bat): se ha utilizado un script de Windows para automatizar la ejecución del sistema, permitiendo iniciar el entorno virtual, la API y la interfaz web de forma automática.
