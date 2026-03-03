Qué es el preprocesamiento

Por qué se lematiza

Qué son stopwords

Por qué se eliminan símbolos

train model :
train_test_split → separa tus datos en entrenamiento y prueba.

TfidfVectorizer → convierte texto en números para que el modelo pueda aprender.

LogisticRegression → modelo sencillo para clasificación multiclase.

classification_report y accuracy_score → evalúan cómo de bien predice el modelo.

joblib → permite guardar el modelo entrenado en un archivo .pkl.

limpiar_y_lemmatizar → limpia y lematiza tus textos en español.

Se aplicó preprocesamiento a todos los textos del dataset usando la función limpiar_y_lemmatizar. Esto convierte los textos a minúsculas, elimina palabras vacías y signos de puntuación, y aplica lematización. Como resultado, cada texto se transforma en una secuencia de palabras clave relevantes para identificar el nivel de riesgo emocional.

train model :
from my_utils import limpiar_y_lemmatizar → asegurarte de que tu archivo my_utils.py existe y contiene la función correcta.

TfidfVectorizer(max_features=500) → convierte textos en vectores de números.

MultinomialNB() → modelo simple y efectivo para texto.

classification_report → imprime precision, recall y F1-score por clase.

Se guardan vectorizador y modelo en models/ para luego usarlo en la app web.