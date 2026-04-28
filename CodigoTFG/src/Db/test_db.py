import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect("src/DB/db.sqlite")
cursor = conn.cursor()

# Obtener últimos registros
cursor.execute("""
SELECT id, texto, riesgo, confianza 
FROM predicciones 
ORDER BY id DESC 
LIMIT 5
""")

filas = cursor.fetchall()

print("\n📊 ÚLTIMAS PREDICCIONES GUARDADAS\n")
print("-" * 70)
print(f"{'ID':<5} | {'RIESGO':<8} | {'CONFIANZA':<10} | TEXTO")
print("-" * 70)

for fila in filas:
    id_, texto, riesgo, confianza = fila
    
    # recortar texto para que no se rompa la tabla
    texto_corto = texto[:40] + "..." if len(texto) > 40 else texto
    
    # colores simbólicos (emoji para defensa)
    if riesgo.lower() == "alto":
        emoji = "🔴"
    elif riesgo.lower() == "medio":
        emoji = "🟠"
    else:
        emoji = "🟢"

    print(f"{id_:<5} | {emoji} {riesgo:<6} | {confianza:<10.2f} | {texto_corto}")

print("-" * 70)

conn.close()