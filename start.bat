@echo off
REM Script de inicio para Windows
REM Sistema de Registro de Rutinas de Ejercicio

echo ==================================================
echo   Sistema de Registro de Rutinas de Ejercicio
echo ==================================================
echo.

REM Verificar si Docker está instalado
docker --version >nul 2>&1
if errorlevel 1 (
    echo [X] Docker no esta instalado o no esta en el PATH
    echo Por favor instala Docker Desktop desde: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)

REM Verificar si Docker está corriendo
docker info >nul 2>&1
if errorlevel 1 (
    echo [X] Docker no esta corriendo
    echo Por favor inicia Docker Desktop y vuelve a ejecutar este script
    pause
    exit /b 1
)

echo [OK] Docker esta instalado y corriendo
echo.

REM Detener contenedores existentes
echo Limpiando contenedores anteriores...
docker-compose down >nul 2>&1

echo.
echo Construyendo e iniciando servicios...
echo.

REM Iniciar servicios
docker-compose up --build -d

REM Esperar a que los servicios estén listos
echo.
echo Esperando a que los servicios esten listos...
timeout /t 10 /nobreak >nul

echo.
echo ==================================================
echo   Servicios Desplegados Exitosamente
echo ==================================================
echo.
echo Microservicio de Rutinas:
echo    API: http://localhost:8001
echo    Docs: http://localhost:8001/docs
echo    Health: http://localhost:8001/health
echo.
echo Microservicio de Ejercicios:
echo    API: http://localhost:8002
echo    Docs: http://localhost:8002/docs
echo    Health: http://localhost:8002/health
echo.
echo ==================================================
echo.
echo Comandos utiles:
echo    Ver logs:     docker-compose logs -f
echo    Detener:      docker-compose down
echo    Reiniciar:    docker-compose restart
echo    Ver estado:   docker-compose ps
echo.
echo ==================================================
echo Listo para usar!
echo ==================================================
echo.

REM Abrir navegador con la documentación
start http://localhost:8001/docs
start http://localhost:8002/docs

pause
