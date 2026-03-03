import spacy

# Cargar modelo de español (una sola vez)
nlp = spacy.load("es_core_news_sm")

def limpiar_y_lemmatizar(texto):
    """
    Recibe un texto y devuelve la versión limpia:
    - minúsculas
    - lematizado
    - sin stopwords ni símbolos
    """
    doc = nlp(texto.lower())  # Convertimos a minúsculas y procesamos con spaCy
     # Filtramos tokens: solo palabras alfabéticas, no stopwords
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens) # Devolvemos un texto limpio listo para vectorizar

# he creado la funcion de preprocesamiento para lematizar y limpiar los textos en español
# esto se puede reutilizar luego 