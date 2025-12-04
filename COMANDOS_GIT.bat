@echo off
echo ====================================
echo   SUBIENDO CODIGO A GITHUB
echo ====================================
echo.

echo [1/3] Configurando rama principal...
git branch -M main

echo.
echo [2/3] Conectando con GitHub...
git remote add origin https://github.com/saberinnato/fitness-api-parcial-final.git

echo.
echo [3/3] Subiendo codigo...
git push -u origin main

echo.
echo ====================================
echo   CODIGO SUBIDO CON EXITO
echo ====================================
echo.
echo Ahora ve a: https://github.com/saberinnato/fitness-api-parcial-final
echo.
pause
