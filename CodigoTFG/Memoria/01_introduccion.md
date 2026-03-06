Explica:

Qué es el análisis de sentimiento

Qué es la clasificación de texto

Por qué es importante detectar riesgo emocional

Limitaciones éticas (no sustituye a profesionales)

1.Preparacion del entorno :
cree estructura de proyecto dentro de visual studio 
instale librerias ( pandas, spacy, scikit-learn)
configure y active venv 

2.Dataset y preprocesamiento de texto:
dataset inicial con textos y niveles de riesgo
funcion limpiar_y_lematizar para limpiar y lematizar textos 
probe que la funcion funciona correctamente y limpia los textos 

3.entrenamiento de modelo ML
vectorizacion TF-IDF de los textos 
entrenamiento de modelo MultinominalNB (clasificaion de riesgo emocional)
evaluacion con classification_report(precision, recall, f1-score)
guardado de model.pk1 y vectorizer.pkl1 para app


