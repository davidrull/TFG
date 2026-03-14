Arquitectura general:

La aplicación se divide en tres capas principales:

1.Interfaz de usuario (Frontend):
.Página web sencilla en HTML/CSS/JS.
.Permite al usuario introducir un texto y enviar la petición al servidor.

2.API REST (Backend):
.Desarrollada con FastAPI.
.Recibe el texto, llama al preprocesamiento y al modelo ML, y devuelve la predicción de riesgo emocional junto con la probabilidad.
.Endpoints principales:
 -- / → para comprobar que la API funciona.
 -- /predict → recibe texto y devuelve nivel de riesgo.

3.Procesamiento de datos y Machine Learning:
.Preprocesamiento: Limpieza y lematización de los textos usando limpiar_y_lemmatizar con spaCy.
.Vectorización: TF-IDF para convertir textos en vectores numéricos.
.Modelo: MultinomialNB entrenado para clasificar riesgo emocional (bajo, medio, alto).
.Persistencia: El modelo y vectorizador se guardan en archivos .pkl para ser cargados por la API.

4.Base de datos
.SQLite para almacenar:
.Textos procesados.
.Predicción de riesgo emocional.
.Feedback del usuario sobre la predicción.

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
│  │  ├─ database.py   # Conexión y almacenamiento en SQLite
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
Interfaz Web (HTML/JS)
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

Explicación:

.El usuario introduce un texto.
.La API REST recibe la petición y llama a la función de limpieza.
.El texto se convierte en vectores y se predice el nivel de riesgo con el modelo ML.
.El resultado se envía al usuario y se almacena en la base de datos junto con el feedback.