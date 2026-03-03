from sklearn.feature_extraction.text import TfidfVectorizer

def crear_vectorizer():
    """
    Crea un vectorizador TF-IDF para convertir textos a números.
    """
    vectorizer = TfidfVectorizer(max_features=500)  # Limita a 500 palabras más importantes
    return vectorizer

    # max_features=500 → para que no haya demasiadas columnas y el modelo sea rápido.
    # Esto es reutilizable luego para entrenar y predecir.