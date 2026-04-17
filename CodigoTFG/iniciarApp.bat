@echo off
:: Evita que se muestren los comandos en la consola para una salida más limpia

cd /d %~dp0
:: Se mueve automáticamente a la carpeta donde está el archivo .bat

echo Iniciando entorno virtual...
:: Mensaje informativo para el usuario

call venv\Scripts\activate
:: Activa el entorno virtual del proyecto (venv)

echo Iniciando API FastAPI...
:: Mensaje informativo

start cmd /k "python -m uvicorn src.api.main:app --reload"
:: Inicia la API en una nueva ventana de consola
:: Se usa /k para que no se cierre la ventana

timeout /t 3 >nul
:: Espera 3 segundos para asegurarse de que la API arranca correctamente

echo Abriendo interfaz web...
:: Mensaje informativo

start http://127.0.0.1:5500/CodigoTFG/Frontend/index.html
:: Abre el frontend SOLO cuando la API ya está en marcha