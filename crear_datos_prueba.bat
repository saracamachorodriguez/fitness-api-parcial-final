@echo off
REM Script para crear datos de prueba en la API
REM Sistema de Rutinas de Ejercicio

echo ========================================
echo  Creando Datos de Prueba
echo ========================================
echo.

echo [1/8] Creando Rutina de Fuerza...
curl -X POST http://localhost:8001/api/rutinas -H "Content-Type: application/json" -d "{\"nombre\":\"Rutina de Fuerza\",\"descripcion\":\"Entrenamiento para aumentar masa muscular y fuerza\",\"duracion_estimada\":60,\"nivel\":\"Intermedio\"}"
echo.
echo.

echo [2/8] Creando Rutina HIIT...
curl -X POST http://localhost:8001/api/rutinas -H "Content-Type: application/json" -d "{\"nombre\":\"Rutina HIIT\",\"descripcion\":\"Cardio de alta intensidad por intervalos\",\"duracion_estimada\":30,\"nivel\":\"Avanzado\"}"
echo.
echo.

echo [3/8] Creando Rutina para Principiantes...
curl -X POST http://localhost:8001/api/rutinas -H "Content-Type: application/json" -d "{\"nombre\":\"Rutina Principiante\",\"descripcion\":\"Entrenamiento basico para empezar\",\"duracion_estimada\":40,\"nivel\":\"Principiante\"}"
echo.
echo.

timeout /t 2 /nobreak >nul

echo [4/8] Agregando ejercicios a Rutina de Fuerza (ID 1)...
curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":1,\"nombre\":\"Press de banca\",\"series\":4,\"repeticiones\":10,\"tiempo_descanso\":90,\"tiempo_ejecucion\":15,\"categoria\":\"Fuerza\"}"
echo.

curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":1,\"nombre\":\"Sentadillas\",\"series\":5,\"repeticiones\":8,\"tiempo_descanso\":120,\"tiempo_ejecucion\":20,\"categoria\":\"Fuerza\"}"
echo.

curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":1,\"nombre\":\"Peso muerto\",\"series\":4,\"repeticiones\":8,\"tiempo_descanso\":120,\"tiempo_ejecucion\":20,\"categoria\":\"Fuerza\"}"
echo.

curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":1,\"nombre\":\"Dominadas\",\"series\":3,\"repeticiones\":12,\"tiempo_descanso\":90,\"tiempo_ejecucion\":12,\"categoria\":\"Fuerza\"}"
echo.
echo.

timeout /t 2 /nobreak >nul

echo [5/8] Agregando ejercicios a Rutina HIIT (ID 2)...
curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":2,\"nombre\":\"Burpees\",\"series\":6,\"repeticiones\":15,\"tiempo_descanso\":30,\"tiempo_ejecucion\":45,\"categoria\":\"HIIT\"}"
echo.

curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":2,\"nombre\":\"Mountain climbers\",\"series\":5,\"repeticiones\":20,\"tiempo_descanso\":30,\"tiempo_ejecucion\":40,\"categoria\":\"HIIT\"}"
echo.

curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":2,\"nombre\":\"Jump squats\",\"series\":5,\"repeticiones\":15,\"tiempo_descanso\":30,\"tiempo_ejecucion\":35,\"categoria\":\"HIIT\"}"
echo.
echo.

timeout /t 2 /nobreak >nul

echo [6/8] Agregando ejercicios a Rutina Principiante (ID 3)...
curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":3,\"nombre\":\"Flexiones de rodillas\",\"series\":3,\"repeticiones\":10,\"tiempo_descanso\":60,\"tiempo_ejecucion\":12,\"categoria\":\"Fuerza\"}"
echo.

curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":3,\"nombre\":\"Plancha\",\"series\":3,\"repeticiones\":1,\"tiempo_descanso\":60,\"tiempo_ejecucion\":30,\"categoria\":\"Funcional\"}"
echo.

curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":3,\"nombre\":\"Caminata\",\"series\":1,\"repeticiones\":1,\"tiempo_descanso\":0,\"tiempo_ejecucion\":600,\"categoria\":\"Cardio\"}"
echo.
echo.

timeout /t 2 /nobreak >nul

echo [7/8] Verificando rutinas creadas...
curl http://localhost:8001/api/rutinas
echo.
echo.

echo [8/8] Calculando tiempo total de cada rutina...
echo.
echo --- Rutina 1: Fuerza ---
curl http://localhost:8002/api/ejercicios/rutina/1/tiempo-total
echo.
echo.

echo --- Rutina 2: HIIT ---
curl http://localhost:8002/api/ejercicios/rutina/2/tiempo-total
echo.
echo.

echo --- Rutina 3: Principiante ---
curl http://localhost:8002/api/ejercicios/rutina/3/tiempo-total
echo.
echo.

echo ========================================
echo  DATOS DE PRUEBA CREADOS EXITOSAMENTE!
echo ========================================
echo.
echo Resumen:
echo - 3 Rutinas creadas
echo - 10 Ejercicios agregados
echo.
echo Puedes verlos en:
echo - Rutinas: http://localhost:8001/docs
echo - Ejercicios: http://localhost:8002/docs
echo.
echo O en Postman con los requests:
echo - Listar Rutinas
echo - Listar Ejercicios
echo.
pause
