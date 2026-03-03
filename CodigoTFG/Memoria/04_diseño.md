# Limpieza de textos

from utils import limpiar_y_lemmatizar

# Aplicar limpieza a cada texto del dataset
df['texto_limpio'] = df['texto'].apply(limpiar_y_lemmatizar)

# Verificar resultados
print(df[['texto', 'texto_limpio']].head())

El código aplica la función de limpieza a cada texto, creando una nueva columna texto_limpio. Esto permite mantener los textos originales para referencia, mientras que la columna limpia se usa para el entrenamiento del modelo.

La precisión baja y los warnings (UndefinedMetricWarning) aparecen porque:

Tu dataset es muy pequeño (solo 34 ejemplos por clase)

El modelo no predice ninguna muestra para algunas clases en el conjunto de prueba

⚠️ Esto es normal con datasets muy reducidos. Para un TFG, puedes explicar que:

“Se entrenó un modelo de prueba con un dataset pequeño para validar la funcionalidad del pipeline. En producción sería necesario un dataset mayor para obtener métricas más fiables.”