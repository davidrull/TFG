El proyecto se divide en varias fases que integran procesamiento de lenguaje natural, aprendizaje automático y desarrollo de API web:

1.Preprocesamiento del texto:
Cada texto introducido por el usuario o presente en el dataset se limpia mediante la función limpiar_y_lemmatizar. Esta función convierte el texto a minúsculas, elimina stopwords y símbolos, y lematiza cada palabra. Esto permite que los textos sean uniformes y adecuados para la vectorización y el modelo. Se comprobó su funcionamiento aplicándola a varias muestras del dataset y verificando los resultados.

2.Extracción de características y entrenamiento del modelo:
Los textos limpios se transforman en vectores numéricos mediante TF-IDF, limitando a 500 características principales. A partir de estos vectores, se entrenó un modelo de Multinomial Naive Bayes para clasificar el nivel de riesgo emocional en tres categorías: bajo, medio o alto. 
La elección de TF-IDF y MultinomialNB se fundamenta en su eficacia demostrada en tareas de clasificación de texto, su eficiencia computacional y su capacidad de manejar correctamente las distribuciones de palabras en diferentes clases. La evaluación del modelo se realizó con classification_report, mostrando métricas de precisión, recall y F1-score, lo que permite medir la fiabilidad del modelo antes de su uso en producción.

3.Despliegue mediante API REST:
Se implementó una API REST utilizando FastAPI, que permite recibir textos y devolver la predicción del riesgo emocional junto con la probabilidad asociada. La API incluye un endpoint de prueba (/) para verificar el funcionamiento del servicio. La carga del modelo y vectorizador se realiza desde archivos pickle previamente guardados, garantizando consistencia entre el entorno de entrenamiento y la API.

4.Interacción con el usuario y almacenamiento:
La aplicación permite que el usuario introduzca un texto libre, reciba la clasificación y visualice la probabilidad de cada nivel de riesgo. Todas las predicciones se registran automáticamente en una base de datos SQLite, incluyendo:
.Texto original introducido por el usuario.
.Nivel de riesgo predicho por el modelo.
.Confianza de la predicción (probabilidad máxima).
.Feedback opcional proporcionado por el usuario.
Esta información permite analizar los resultados, evaluar la precisión del modelo en situaciones reales y planificar posibles mejoras o reentrenamientos. 
.La interfaz de usuario ha sido mejorada mediante la incorporación de elementos visuales dinámicos, como una codificación por colores y una barra de progreso que representa la confianza del modelo. Estas mejoras permiten una interpretación más intuitiva de los resultados sin necesidad de interpretar valores numéricos.
Desde el punto de vista ético, se mantiene la privacidad de los textos introducidos y se recalca que esta herramienta no sustituye la intervención de profesionales de la salud, sino que proporciona información orientativa.

5.Resultados y verificación:
Cada módulo se probó de forma independiente:
.La función de preprocesamiento se verificó aplicándola al dataset.
.El modelo se evaluó con métricas estándar de clasificación.
.La API se probó localmente con Uvicorn, asegurando que devuelve resultados correctos ante distintas entradas.

Este análisis demuestra que el flujo completo, desde la entrada del texto hasta la predicción y almacenamiento, está diseñado para ofrecer resultados rápidos, claros y reutilizables, manteniendo una separación clara entre preprocesamiento, modelado y servicio web. En futuras versiones, se podrían incluir gráficos o visualizaciones de estadísticas para facilitar la interpretación de los resultados.

Para la ejecución del sistema completo se ha implementado un script de automatización (.bat) que inicia tanto la API REST como el servidor HTTP local en Python para la interfaz web. Esto permite que el flujo completo del sistema esté operativo con un único comando, sin necesidad de configuración manual por parte del usuario.
Este enfoque permite considerar la aplicación como un sistema integrado end-to-end, en el que todos los componentes (interfaz, API, modelo y base de datos) funcionan de forma coordinada.

La incorporación de elementos visuales en la capa de presentación contribuye a mejorar la interpretabilidad del sistema, facilitando la comprensión del resultado por parte del usuario final y reforzando la utilidad práctica de la aplicación.

Diagrama del flujo de datos:

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
(limpiar_y_lemmatizar: minúsculas, lematización, eliminación de stopwords)
   │
   ▼
Modelo de ML
(TF-IDF + MultinomialNB)
Predicción de riesgo: Bajo / Medio / Alto
   │
   ▼
Resultado
Nivel de riesgo + probabilidad
   │
   ▼
Base de datos SQLite
Texto original, Predicción, Feedback usuario

Explicación del diagrama:
.Usuario: introduce un texto libre describiendo cómo se siente o una situación personal.
.Interfaz Web: recoge el texto y envía la solicitud a la API REST.
.API REST (FastAPI): recibe la petición, verifica que el modelo y el vectorizador están cargados, y llama al preprocesamiento.
.Preprocesamiento NLP: se limpian los textos usando la función limpiar_y_lemmatizar.
.Modelo de ML: transforma el texto en vectores TF-IDF y clasifica el riesgo emocional usando Multinomial Naive Bayes.
.Resultado: la API devuelve el nivel de riesgo y la probabilidad de cada categoría al usuario.
.Base de datos SQLite: guarda el texto original, la predicción y el feedback del usuario para futuros análisis y mejoras del modelo.