Arquitectura General:

La aplicación se organiza en cuatro capas principales, siguiendo un diseño modular que facilita el mantenimiento y la escalabilidad:

1.Interfaz de usuario (Frontend):
.Página web sencilla desarrollada con HTML, CSS y JavaScript.
.Permite al usuario introducir un texto libre y enviar la petición al servidor para su análisis.
.La interfaz incluye visualización del resultado del análisis y la probabilidad de cada categoría de riesgo emocional.
Se ha incorporado una mejora en la representación de los resultados mediante elementos visuales dinámicos, incluyendo una codificación por colores y una barra de progreso que representa la confianza del modelo. Estas mejoras permiten una interpretación más intuitiva del resultado sin necesidad de interpretar valores numéricos.
.La interfaz se ejecuta mediante Live Server desde Visual Studio Code, permitiendo servir el frontend de forma local en el navegador.

2.API REST (Backend):
.Implementada con FastAPI.
.Funciona como intermediario entre la interfaz de usuario y el módulo de Machine Learning.
Endpoints principales:
. /- Endpoint de prueba para verificar el correcto funcionamiento de la API.
. /predict- Recibe un texto, lo procesa y devuelve la predicción del nivel de riesgo emocional y su probabilidad asociada.
Justificación: Se eligió FastAPI por su eficiencia, documentación automática y facilidad para integrar modelos de Machine Learning.

3.Procesamiento de datos y Machine Learning:
.Preprocesamiento: Limpieza y lematización de los textos utilizando la función limpiar_y_lemmatizar implementada con spaCy. 
 Esto incluye:
.Conversión a minúsculas.
.Eliminación de stopwords y símbolos no alfabéticos.
.Lematización para normalizar palabras.
.Vectorización: TF-IDF para transformar los textos limpios en vectores numéricos. Se limita a 500 características principales para mejorar la eficiencia del modelo.
.Modelo: Multinomial Naive Bayes entrenado para clasificar el riesgo emocional en tres niveles: bajo, medio y alto.
.Persistencia: Modelo y vectorizador se guardan en archivos .pkl para su carga en la API.

4.Base de datos:
.Sistema de almacenamiento SQLite utilizado para:
.Guardar los textos introducidos por el usuario.
.Registrar las predicciones realizadas por el modelo.
.Almacenar el feedback del usuario sobre la predicción.
 Esto permite análisis posteriores y reentrenamiento del modelo para mejorar su rendimiento.
.Se garantiza la privacidad de los datos y se recuerda que el sistema no sustituye la intervención de profesionales de la salud, funcionando como herramienta orientativa.
.La base de datos SQLite contiene la tabla predicciones con los siguientes campos:
 .id: clave primaria autoincremental
 .texto: texto introducido por el usuario
 .riesgo: nivel de riesgo predicho
 .confianza: probabilidad de la predicción
 .feedback: comentario opcional del usuario
.La base de datos se crea automáticamente si no existe al iniciar la API.
.Cada inserción se realiza desde el endpoint /predict tras generar la predicción, integrando de manera directa la interacción del usuario con el almacenamiento y análisis de datos.

Diagrama Entidad-Relación (ER) de la tabla predicciones:

+-------------------+
|   predicciones    |
+-------------------+
| id (PK)           |
| texto             |
| riesgo            |
| confianza         |
| feedback          |
+-------------------+

Explicación:

predicciones es la única tabla del sistema, con todos los registros de textos y predicciones del usuario.
id es la clave primaria que identifica de forma única cada registro.
Los demás campos (texto, riesgo, confianza, feedback) almacenan la información del análisis de riesgo emocional y del feedback proporcionado por el usuario.
No existen relaciones con otras tablas en esta versión del proyecto, por lo que la entidad es independiente.

.Estructura de carpetas:

El proyecto sigue una estructura modular para facilitar mantenimiento y escalabilidad:

CodigoTFG/
├─ Data/
│  ├─ dataset_inicial.csv
│  ├─ Memoria
├─ models/
│  ├─ model.pkl
│  ├─ vectorizer.pkl
├─ src/
│  ├─ API/
│  │  ├─ __init__.py
│  │  ├─ main.py    # API REST
│  ├─ DB/
│  │  ├─ __init__.py
│  │  ├─ database.py   # Gestión de SQLite: predicciones y feedback del usuario
│  ├─ ML/
│  │  ├─ __init__.py
│  │  ├─ evaluate_model.py
│  │  ├─ my_utils.py      # Función limpiar_y_lemmatizar
│  │  ├─ predict_test.py  
│  │  ├─ test_preprocessing.py  # Pruebas de limpieza
│  │  ├─ train_model.py  # Entrenamiento y guardado de modelo
│  │  ├─ vectorizer.py
├─ venv/


.Diagrama de diseño:

   Usuario
      │
      ▼
Interfaz Web (HTML/JS servida con Live Server)
      │
      ▼
 API REST (FastAPI)
    │
    ├── Preprocesamiento NLP (limpieza y lematización)
    │
    ├── Modelo ML (TF-IDF + MultinomialNB)
      │
      ▼
Resultado y probabilidad
      │
      ▼
Base de datos SQLite (predicciones + feedback)

.El sistema se compone de dos servicios independientes: una API REST desarrollada con FastAPI que ejecuta el modelo de Machine Learning, y una interfaz web que actúa como cliente, enviando solicitudes HTTP a la API y mostrando los resultados al usuario.

Explicación:

.El usuario introduce un texto libre describiendo su situación o emociones.
.La API REST recibe la solicitud y llama a la función de preprocesamiento.
.El texto se convierte en vectores TF-IDF y se clasifica con el modelo ML.
.El resultado, junto con la probabilidad de cada categoría, se envía al usuario y se almacena en la base de datos.
.El feedback del usuario permite mejorar el sistema mediante reentrenamiento futuro.

La capa de presentación incluye elementos visuales dinámicos (colores y barra de progreso) que mejoran la interpretabilidad de los resultados.

.El sistema se ejecuta de forma manual, iniciando la API con Uvicorn y la interfaz web mediante Live Server en Visual Studio Code.

.La aplicación se accede directamente desde el navegador a través de Live Server, sin necesidad de accesos directos externos.


