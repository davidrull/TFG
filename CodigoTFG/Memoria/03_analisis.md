El proyecto se divide en varias fases que integran procesamiento de lenguaje natural, aprendizaje automático y desarrollo de API web:

1.Preprocesamiento del texto:
Cada texto introducido por el usuario o presente en el dataset se limpia mediante la función limpiar_y_lemmatizar. Esta función convierte el texto a minúsculas, elimina stopwords y símbolos, y lematiza cada palabra. Esto permite que los textos sean uniformes y adecuados para la vectorización y el modelo. Se comprobó su funcionamiento aplicándola a varias muestras del dataset y verificando los resultados.

2.Extracción de características y entrenamiento del modelo:
Los textos limpios se transforman en vectores numéricos mediante TF-IDF, limitando a 500 características principales. A partir de estos vectores, se entrena un modelo de Multinomial Naive Bayes para clasificar el nivel de riesgo emocional en tres categorías: bajo, medio o alto. La evaluación del modelo se realiza con classification_report, mostrando métricas de precisión, recall y F1-score, lo que permite medir la fiabilidad del modelo antes de su uso en producción.

3.Despliegue mediante API REST:
Se implementa una API con FastAPI, que permite recibir textos y devolver la predicción del riesgo emocional junto con la probabilidad asociada. La API también incluye un endpoint de prueba (/) para verificar que el servicio funciona correctamente. La carga del modelo y vectorizador se hace desde archivos pickle previamente guardados, garantizando consistencia entre el entorno de entrenamiento y la API.

4.Interacción con el usuario y almacenamiento:
La aplicación permite que el usuario introduzca un texto libre, reciba la clasificación y visualize la probabilidad de cada nivel de riesgo. Además, todas las predicciones y el feedback del usuario se almacenan en una base de datos SQLite, lo que permite análisis posteriores y posibles mejoras del modelo mediante reentrenamiento con nuevos datos.

5.Resultados y verificación:
Cada módulo se prueba de forma independiente:

.La función de preprocesamiento se verificó aplicándola al dataset.
.El modelo se evaluó con métricas estándar de clasificación.
.La API se probó localmente con Uvicorn, asegurando que devuelve resultados correctos ante distintas entradas.

Este análisis demuestra que el flujo completo, desde la entrada del texto hasta la predicción y almacenamiento, está diseñado para ofrecer resultados rápidos, claros y reutilizables, manteniendo una separación clara entre preprocesamiento, modelado y servicio web. 
         
         
          Usuario
             │
             ▼
       Interfaz Web
    (HTML / JavaScript)
             │
             ▼
         API REST
         (FastAPI)
             │
             ▼
     Preprocesamiento NLP
      limpiar_y_lemmatizar
     minúsculas, lematización
     eliminación de stopwords
             │
             ▼
       Modelo de ML
  (TF-IDF + MultinomialNB)
     Predicción de riesgo:
      Bajo / Medio / Alto
             │
             ▼
          Resultado
  Nivel de riesgo + probabilidad
             │
             ▼
      Base de datos SQLite
        Texto original
         Predicción
       Feedback usuario

Explicación del diagrama:

.Usuario: introduce un texto libre describiendo cómo se siente o una situación personal.
.Interfaz Web: recoge el texto y envía la solicitud a la API REST.
.API REST (FastAPI): recibe la petición, verifica que el modelo y el vectorizador están cargados, y llama al preprocesamiento.
.Preprocesamiento NLP: se limpian los textos usando tu función limpiar_y_lemmatizar. Esto incluye pasar a minúsculas, lematizar y eliminar stopwords y símbolos.
.Modelo de ML: transforma el texto en vectores TF-IDF y clasifica el riesgo emocional usando Multinomial Naive Bayes.
.Resultado: la API devuelve el nivel de riesgo y la probabilidad de cada categoría al usuario.
.Base de datos SQLite: guarda el texto original, la predicción y el feedback del usuario para futuros análisis y mejoras del modelo.