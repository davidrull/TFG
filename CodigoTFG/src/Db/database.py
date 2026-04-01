import sqlite3  # Librería estándar de Python para trabajar con SQLite
import os        # Para manejar rutas de archivos de forma dinámica


# 1.Definimos la ruta de la base de datos

# BASE_DIR será la carpeta "src" (una carpeta arriba de "DB")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Guardaremos la base de datos como db.sqlite dentro de src/DB
DB_PATH = os.path.join(BASE_DIR, "DB", "db.sqlite")


# 2.Función para conectar con la base de datos

def conectar():
    
    # Crea la conexión con la BBDD SQLite y devuelve un objeto conexión.
    
    conn = sqlite3.connect(DB_PATH)
    return conn


# 3.Función para crear la tabla de predicciones

def crear_tabla():
    """
    Crea la tabla 'predicciones' si no existe.
    Columnas:
        - id: clave primaria autoincremental
        - texto: el texto introducido por el usuario
        - riesgo: predicción del modelo (bajo/medio/alto)
        - confianza: probabilidad de la predicción
        - feedback: retroalimentación del usuario
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predicciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL,
            riesgo TEXT NOT NULL,
            confianza REAL NOT NULL,
            feedback TEXT
        )
    """)
    conn.commit()  # Guardar cambios
    conn.close()   # Cerrar conexión


# 4.Función para guardar una predicción

def guardar_prediccion(texto, riesgo, confianza, feedback=None):
    """
    Inserta una nueva predicción en la base de datos.
    
    Parámetros:
        texto (str)       : Texto del usuario
        riesgo (str)      : Predicción del modelo (bajo/medio/alto)
        confianza (float) : Probabilidad asociada a la predicción
        feedback (str)    : Comentario opcional del usuario
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO predicciones (texto, riesgo, confianza, feedback)
        VALUES (?, ?, ?, ?)
    """, (texto, riesgo, confianza, feedback))
    conn.commit()  # Guardar cambios
    conn.close()   # Cerrar conexión