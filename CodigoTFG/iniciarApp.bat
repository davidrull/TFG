@echo off
:: Evita que se muestren los comandos en la consola para una salida más limpia

cd /d %~dp0
:: Se mueve automáticamente a la carpeta donde está el archivo .bat
:: Esto permite que funcione desde cualquier ubicación

echo Iniciando entorno virtual...
:: Mensaje informativo para el usuario

:: (NO usamos activate porque en Windows puede dar problemas de PATH)
:: En su lugar usamos directamente el Python del entorno virtual

echo Iniciando API FastAPI...
:: Mensaje informativo

start cmd /k "venv\Scripts\python -m uvicorn src.Api.main:app --reload"
:: Inicia la API REST con Uvicorn usando el Python del entorno virtual
:: Esto asegura que usa las dependencias del venv correctamente
:: /k mantiene la consola abierta para ver logs de la API

timeout /t 3 >nul
:: Espera 3 segundos para asegurarse de que la API ha arrancado correctamente

echo Abriendo interfaz web...
:: Mensaje informativo

start http://127.0.0.1:5500/CodigoTFG/Frontend/index.html
:: Abre automáticamente la interfaz de usuario en el navegador
:: (Frontend del proyecto ejecutado con Live Server)