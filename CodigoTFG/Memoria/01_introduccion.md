Explica:

Qué es el análisis de sentimiento

Qué es la clasificación de texto

Por qué es importante detectar riesgo emocional

Limitaciones éticas (no sustituye a profesionales). 
Esta información es relevante porque permite ofrecer orientación y apoyo preventivo, aunque no sustituye en ningún caso el diagnóstico o la intervención de profesionales de la salud. Se trata de una herramienta de apoyo informativo, con limitaciones éticas que deben tenerse en cuenta.
Desde un punto de vista ético, este sistema presenta diversas limitaciones:
.En primer lugar, el modelo puede verse afectado por sesgos presentes en el dataset, lo que podría influir en la precisión de las predicciones.
.Pueden producirse falsos positivos o falsos negativos, lo que implica que el sistema no debe utilizarse como herramienta de diagnóstico, sino únicamente como apoyo informativo.
.Se debe considerar la privacidad de los datos introducidos por los usuarios, evitando el almacenamiento de información sensible sin consentimiento explícito.

Por todo ello, se recalca que la aplicación no sustituye la intervención de profesionales de la salud mental.

1.Preparacion del entorno :
.Se creó la estructura del proyecto en Visual Studio Code, organizando los módulos en carpetas diferenciadas para facilitar la    mantenibilidad y escalabilidad del sistema.
.Se instalaron las librerias necesarias ( pandas, spacy, scikit-learn)
.Se configuró y activo el venv.

2.Dataset y preprocesamiento de texto:
.dataset inicial con textos y niveles de riesgo
.funcion limpiar_y_lematizar para limpiar y lematizar textos 
.Se probo que la función funcionaba correctamente y limpiaba los textos. 

3.entrenamiento de modelo ML
.vectorizacion TF-IDF de los textos 
.entrenamiento de modelo MultinominalNB (clasificaion de riesgo emocional)
.evaluacion con classification_report(precision, recall, f1-score)
.guardado de model.pk1 y vectorizer.pkl1 para app

4.API

Explicación rápida de cada sección:

.Importaciones: FastAPI, pickle, os, sys.
.Agregar src al path: Para que Python encuentre tu carpeta ML.
.Importar limpiar_y_lemmatizar desde ML.
.Rutas absolutas: Evita problemas de rutas relativas y FileNotFoundError.
.Verificación de archivos: Te avisa si model.pkl o vectorizer.pkl no están.
.Cargar modelo y vectorizador.
.Crear instancia FastAPI.
.Endpoint / para comprobar que la API funciona.
.Endpoint /predict que recibe un texto y devuelve riesgo + confianza.

Ejecutar con Python directamente usando python src/api/main.py.

En los últimos años, el uso de aplicaciones basadas en inteligencia artificial ha crecido de forma notable, especialmente en ámbitos relacionados con el análisis de datos y el procesamiento del lenguaje natural (NLP). Dentro de este contexto, el análisis de sentimiento y la clasificación de texto se han convertido en herramientas clave para comprender la opinión, las emociones y los riesgos implícitos en los mensajes escritos por los usuarios.

El análisis de sentimiento consiste en identificar la actitud o emoción presente en un texto, mientras que la clasificación de texto permite asignar etiquetas o categorías predefinidas a un texto en función de su contenido. Aplicando estas técnicas al ámbito de la salud emocional, es posible detectar de manera temprana indicios de riesgo emocional, clasificando los textos en niveles como riesgo bajo, medio o alto. Esta información es relevante porque permite ofrecer orientación y apoyo preventivo, aunque no sustituye en ningún caso el diagnóstico o la intervención de profesionales de la salud. Se trata de una herramienta de apoyo informativo, con limitaciones éticas que deben tenerse en cuenta.

El presente proyecto consiste en el desarrollo de una aplicación capaz de analizar textos escritos por los usuarios y clasificar su nivel de riesgo emocional mediante un modelo de aprendizaje automático. La aplicación ofrece una respuesta rápida y accesible a través de una API REST desarrollada con FastAPI, que interactúa con un modelo entrenado en Python utilizando técnicas de Machine Learning y Natural Language Processing.

1.1 Preparación del entorno

Para garantizar un desarrollo ordenado y reproducible, se llevó a cabo la siguiente preparación del entorno:

.Creación de la estructura de proyecto dentro de Visual Studio Code, organizando carpetas para la API (src/api), la base de datos (src/Db) y las utilidades de procesamiento de texto (src/ML).
.Configuración y activación de un entorno virtual (venv) para gestionar dependencias de Python.
.Instalación de librerías necesarias: pandas, scikit-learn, spaCy, fastapi, uvicorn y otras dependencias auxiliares.

Esta preparación asegura que todas las dependencias se encuentren aisladas y que el proyecto pueda ejecutarse de forma consistente en cualquier equipo.

1.2 Dataset y preprocesamiento de texto

El dataset inicial consta de textos etiquetados según niveles de riesgo emocional (bajo, medio, alto). Para preparar los datos:

Se implementó la función limpiar_y_lemmatizar en src/ML/my_utils.py, encargada de:

.Eliminar caracteres no deseados y stopwords.
.Convertir todo a minúsculas.
.Aplicar lematización para normalizar las palabras.

Se realizaron pruebas de la función para asegurar que limpiara correctamente los textos y estuviera lista para ser procesada por el modelo de ML (con este comando en powershell python src/ML/test_preprocessing.py).

1.3 Entrenamiento del modelo de Machine Learning

Para la clasificación de riesgo emocional se siguieron los siguientes pasos:

.Vectorización TF-IDF de los textos, convirtiendo el texto en vectores numéricos para que el modelo pueda procesarlos.
.Entrenamiento de un modelo Multinomial Naive Bayes, adecuado para clasificación de texto.
 (Se ha seleccionado el algoritmo Multinomial Naive Bayes debido a su buen rendimiento en tareas de clasificación de texto y su bajo coste computacional. Este modelo es especialmente adecuado para representaciones basadas en frecuencias como TF-IDF.
 Además, se ha priorizado la simplicidad y rapidez de entrenamiento frente a modelos más complejos como la regresión logística o redes neuronales, ya que el objetivo del proyecto es construir un sistema funcional y eficiente dentro del alcance del módulo.)
.Evaluación del modelo con classification_report, incluyendo métricas de precisión, recall y F1-score.
.Guardado del modelo (model.pkl) y del vectorizador (vectorizer.pkl) mediante Pickle, para su posterior uso en la API.

.La Función:
def limpiar_y_lemmatizar(texto):
    doc = nlp(texto.lower())  # Convertimos a minúsculas y procesamos con spaCy
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

.Convierte el texto a minúsculas.
.Aplica lemmatización para normalizar las palabras.
.Elimina stopwords (palabras sin significado relevante) y símbolos/no alfabéticos.
.Devuelve un texto limpio listo para vectorizar con TF-IDF.

se realizaron pruebas del ML(con este comando en powershell python src/ML/train_model.py).


1.4 Desarrollo de la API

.La API está desarrollada en FastAPI y organizada en src/api/main.py.

Explicación de cada sección:

.Importaciones: FastAPI, pickle, os y sys.
.Agregar src al path: para que Python encuentre la carpeta ML y sus utilidades.
.Importar limpiar_y_lemmatizar desde ML.
.Rutas absolutas: evitan problemas de rutas relativas y FileNotFoundError.
.Verificación de archivos: comprueba si model.pkl y vectorizer.pkl existen.
.Cargar modelo y vectorizador.
.Instancia de FastAPI.
.Endpoint /: para comprobar que la API funciona.
.Endpoint /predict: recibe un texto y devuelve el nivel de riesgo y la confianza asociada.

La API se puede ejecutar con el comando:

.python src/api/main.py

o usando Uvicorn para desarrollo con recarga automática:

uvicorn src.api.main:app --reload

1.5 Funcionalidades de la aplicación

La aplicación ofrece al usuario las siguientes funcionalidades:

.Introducción de texto: el usuario escribe un texto describiendo cómo se siente o una situación personal.
.Análisis automático del texto: el sistema limpia y procesa el texto, transformándolo en vectores para el modelo.
.Clasificación del riesgo emocional: el modelo devuelve uno de los tres niveles de riesgo: bajo, medio o alto.
.Visualización del resultado: se muestra el resultado junto con la probabilidad de cada categoría.
.Feedback del usuario: el usuario puede indicar si considera correcta la predicción.
.Registro de predicciones: todas las predicciones y el feedback se almacenan en una base de datos SQLite para análisis posterior y mejora del modelo.

Se adjuntan pantallazos de las pruebas realizadas del funcionamiento del preprocesamiento, del funcionamiento del ML y de el mismo funcionamiento de la API. 