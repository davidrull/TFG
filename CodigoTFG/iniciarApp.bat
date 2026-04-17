@echo off
:: Evita que se muestren los comandos en la consola para una salida más limpia

cd /d %~dp0
:: Se mueve automáticamente a la carpeta donde está el archivo .bat
:: Esto permite que funcione desde cualquier ubicación del proyecto

echo Iniciando API FastAPI...
:: Mensaje informativo

start  cmd /k "venv\Scripts\python -m uvicorn src.Api.main:app --reload"
:: Inicia la API REST con FastAPI usando el entorno virtual (venv)
:: /k mantiene la consola abierta para ver los logs del servidor

timeout /t 3 >nul
:: Espera 3 segundos para dar tiempo a que la API arranque correctamente

echo Iniciando servidor del frontend...
:: Mensaje informativo

start cmd /k "cd Frontend && python -m http.server 5500"
:: Inicia un servidor HTTP local en la carpeta Frontend
:: Esto sustituye a Live Server y evita depender de VS Code

timeout /t 2 >nul
:: Pequeña espera para asegurar que el frontend está activo

echo Abriendo interfaz web...
:: Mensaje informativo

start http://127.0.0.1:5500/index.html
:: Abre automáticamente la interfaz en el navegador
:: Ahora el frontend está servido por Python y no por Live Server