# 🚀 Comandos Curl para Probar Rápidamente

Si prefieres probar desde la terminal en lugar de Postman, aquí están todos los comandos.

## ✅ Health Checks

### Verificar Servicio de Rutinas
```cmd
curl http://localhost:8001/health
```

### Verificar Servicio de Ejercicios
```cmd
curl http://localhost:8002/health
```

---

## 📋 RUTINAS

### 1. Crear Rutina de Fuerza
```cmd
curl -X POST http://localhost:8001/api/rutinas -H "Content-Type: application/json" -d "{\"nombre\":\"Rutina de Fuerza\",\"descripcion\":\"Entrenamiento para aumentar masa muscular\",\"duracion_estimada\":60,\"nivel\":\"Intermedio\"}"
```

### 2. Crear Rutina de Cardio
```cmd
curl -X POST http://localhost:8001/api/rutinas -H "Content-Type: application/json" -d "{\"nombre\":\"Rutina HIIT\",\"descripcion\":\"Cardio de alta intensidad\",\"duracion_estimada\":30,\"nivel\":\"Avanzado\"}"
```

### 3. Listar Todas las Rutinas
```cmd
curl http://localhost:8001/api/rutinas
```

### 4. Obtener Rutina por ID
```cmd
curl http://localhost:8001/api/rutinas/1
```

### 5. Actualizar Rutina
```cmd
curl -X PUT http://localhost:8001/api/rutinas/1 -H "Content-Type: application/json" -d "{\"duracion_estimada\":75}"
```

### 6. Eliminar Rutina
```cmd
curl -X DELETE http://localhost:8001/api/rutinas/1
```

---

## 🏋️ EJERCICIOS

### 1. Crear Ejercicio - Press de Banca
```cmd
curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":1,\"nombre\":\"Press de banca\",\"series\":4,\"repeticiones\":10,\"tiempo_descanso\":90,\"tiempo_ejecucion\":15,\"categoria\":\"Fuerza\"}"
```

### 2. Crear Ejercicio - Sentadillas
```cmd
curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":1,\"nombre\":\"Sentadillas\",\"series\":5,\"repeticiones\":8,\"tiempo_descanso\":120,\"tiempo_ejecucion\":20,\"categoria\":\"Fuerza\"}"
```

### 3. Crear Ejercicio - Peso Muerto
```cmd
curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":1,\"nombre\":\"Peso muerto\",\"series\":4,\"repeticiones\":8,\"tiempo_descanso\":120,\"tiempo_ejecucion\":20,\"categoria\":\"Fuerza\"}"
```

### 4. Crear Ejercicio - Burpees (para rutina 2)
```cmd
curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":2,\"nombre\":\"Burpees\",\"series\":6,\"repeticiones\":15,\"tiempo_descanso\":30,\"tiempo_ejecucion\":45,\"categoria\":\"HIIT\"}"
```

### 5. Listar Todos los Ejercicios
```cmd
curl http://localhost:8002/api/ejercicios
```

### 6. Filtrar Ejercicios por Categoría
```cmd
curl "http://localhost:8002/api/ejercicios?categoria=Fuerza"
```

### 7. Obtener Ejercicio por ID
```cmd
curl http://localhost:8002/api/ejercicios/1
```

### 8. Obtener Ejercicios de una Rutina
```cmd
curl http://localhost:8002/api/ejercicios/rutina/1
```

### 9. Calcular Tiempo Total de Rutina
```cmd
curl http://localhost:8002/api/ejercicios/rutina/1/tiempo-total
```

### 10. Actualizar Ejercicio
```cmd
curl -X PUT http://localhost:8002/api/ejercicios/1 -H "Content-Type: application/json" -d "{\"series\":5,\"repeticiones\":12}"
```

### 11. Eliminar Ejercicio
```cmd
curl -X DELETE http://localhost:8002/api/ejercicios/1
```

---

## 🎯 Script Completo de Demo

Copia y pega estos comandos en secuencia para una demo completa:

```cmd
REM 1. Verificar servicios
curl http://localhost:8001/health
curl http://localhost:8002/health

REM 2. Crear rutina
curl -X POST http://localhost:8001/api/rutinas -H "Content-Type: application/json" -d "{\"nombre\":\"Rutina Full Body\",\"descripcion\":\"Entrenamiento completo\",\"duracion_estimada\":60,\"nivel\":\"Intermedio\"}"

REM 3. Crear ejercicios
curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":1,\"nombre\":\"Press de banca\",\"series\":4,\"repeticiones\":10,\"tiempo_descanso\":90,\"tiempo_ejecucion\":15,\"categoria\":\"Fuerza\"}"

curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":1,\"nombre\":\"Sentadillas\",\"series\":4,\"repeticiones\":12,\"tiempo_descanso\":90,\"tiempo_ejecucion\":20,\"categoria\":\"Fuerza\"}"

curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":1,\"nombre\":\"Dominadas\",\"series\":3,\"repeticiones\":8,\"tiempo_descanso\":120,\"tiempo_ejecucion\":12,\"categoria\":\"Fuerza\"}"

REM 4. Listar datos
curl http://localhost:8001/api/rutinas
curl http://localhost:8002/api/ejercicios/rutina/1

REM 5. Calcular tiempo total
curl http://localhost:8002/api/ejercicios/rutina/1/tiempo-total
```

---

## 📊 Respuestas Esperadas

### Health Check
```json
{
  "status": "healthy",
  "service": "rutinas-service",
  "timestamp": "2025-12-04T..."
}
```

### Crear Rutina
```json
{
  "id": 1,
  "nombre": "Rutina de Fuerza",
  "descripcion": "Entrenamiento para aumentar masa muscular",
  "duracion_estimada": 60,
  "nivel": "Intermedio",
  "fecha_creacion": "2025-12-04T..."
}
```

### Listar Rutinas
```json
[
  {
    "id": 1,
    "nombre": "Rutina de Fuerza",
    "descripcion": "Entrenamiento para aumentar masa muscular",
    "duracion_estimada": 60,
    "nivel": "Intermedio",
    "fecha_creacion": "2025-12-04T..."
  }
]
```

### Crear Ejercicio
```json
{
  "id": 1,
  "rutina_id": 1,
  "nombre": "Press de banca",
  "series": 4,
  "repeticiones": 10,
  "tiempo_descanso": 90,
  "tiempo_ejecucion": 15,
  "categoria": "Fuerza",
  "fecha_creacion": "2025-12-04T..."
}
```

### Calcular Tiempo Total
```json
{
  "rutina_id": 1,
  "total_ejercicios": 3,
  "tiempo_total_ejecucion": 188,
  "tiempo_total_descanso": 780,
  "tiempo_total_estimado": 968
}
```

**968 segundos = 16 minutos y 8 segundos**

---

## 💡 Tips

1. **Formatear JSON**: Para ver el JSON formateado, instala `jq`:
```cmd
curl http://localhost:8001/api/rutinas | jq
```

2. **Guardar respuesta**: Guarda la respuesta en un archivo:
```cmd
curl http://localhost:8001/api/rutinas > rutinas.json
```

3. **Ver headers**: Para ver los headers de respuesta:
```cmd
curl -i http://localhost:8001/health
```

4. **Modo verbose**: Para debug completo:
```cmd
curl -v http://localhost:8001/health
```

---

## 🎬 Videos Recomendados para Demo

Graba tu pantalla ejecutando estos comandos en orden:

1. ✅ Health checks
2. ➕ Crear 1 rutina
3. ➕ Crear 3 ejercicios
4. 📋 Listar rutinas y ejercicios
5. ⏱️ Calcular tiempo total
6. ✏️ Actualizar un ejercicio
7. 🗑️ Eliminar un ejercicio

**¡Muestra cómo funciona tu API!** 🚀
