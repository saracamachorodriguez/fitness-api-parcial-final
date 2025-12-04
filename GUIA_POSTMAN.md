# 📮 Guía Paso a Paso: Probar Endpoints en Postman

## ✅ Servicios Iniciados

Tus servicios ya están corriendo en:
- **Rutinas**: http://localhost:8001
- **Ejercicios**: http://localhost:8002

---

## 📥 Método 1: Importar Colección Completa (Más Rápido)

### Paso 1: Copiar la Colección JSON

Abre Postman y sigue estos pasos:

1. Click en **"Import"** (esquina superior izquierda)
2. Selecciona la pestaña **"Raw text"**
3. Copia y pega este JSON completo:

```json
{
  "info": {
    "name": "Sistema Rutinas - Sara C",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "variable": [
    {
      "key": "rutinas_url",
      "value": "http://localhost:8001"
    },
    {
      "key": "ejercicios_url",
      "value": "http://localhost:8002"
    }
  ],
  "item": [
    {
      "name": "1️⃣ RUTINAS SERVICE",
      "item": [
        {
          "name": "✅ Health Check",
          "request": {
            "method": "GET",
            "header": [],
            "url": "{{rutinas_url}}/health"
          }
        },
        {
          "name": "📋 Listar Rutinas",
          "request": {
            "method": "GET",
            "header": [],
            "url": "{{rutinas_url}}/api/rutinas"
          }
        },
        {
          "name": "🔍 Obtener Rutina por ID",
          "request": {
            "method": "GET",
            "header": [],
            "url": "{{rutinas_url}}/api/rutinas/1"
          }
        },
        {
          "name": "➕ Crear Rutina Fuerza",
          "request": {
            "method": "POST",
            "header": [{"key": "Content-Type", "value": "application/json"}],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"nombre\": \"Rutina de Fuerza\",\n  \"descripcion\": \"Entrenamiento para aumentar masa muscular\",\n  \"duracion_estimada\": 60,\n  \"nivel\": \"Intermedio\"\n}"
            },
            "url": "{{rutinas_url}}/api/rutinas"
          }
        },
        {
          "name": "➕ Crear Rutina Cardio",
          "request": {
            "method": "POST",
            "header": [{"key": "Content-Type", "value": "application/json"}],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"nombre\": \"Rutina HIIT\",\n  \"descripcion\": \"Cardio de alta intensidad\",\n  \"duracion_estimada\": 30,\n  \"nivel\": \"Avanzado\"\n}"
            },
            "url": "{{rutinas_url}}/api/rutinas"
          }
        },
        {
          "name": "✏️ Actualizar Rutina",
          "request": {
            "method": "PUT",
            "header": [{"key": "Content-Type", "value": "application/json"}],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"duracion_estimada\": 75\n}"
            },
            "url": "{{rutinas_url}}/api/rutinas/1"
          }
        },
        {
          "name": "🗑️ Eliminar Rutina",
          "request": {
            "method": "DELETE",
            "header": [],
            "url": "{{rutinas_url}}/api/rutinas/1"
          }
        }
      ]
    },
    {
      "name": "2️⃣ EJERCICIOS SERVICE",
      "item": [
        {
          "name": "✅ Health Check",
          "request": {
            "method": "GET",
            "header": [],
            "url": "{{ejercicios_url}}/health"
          }
        },
        {
          "name": "📋 Listar Ejercicios",
          "request": {
            "method": "GET",
            "header": [],
            "url": "{{ejercicios_url}}/api/ejercicios"
          }
        },
        {
          "name": "🔍 Filtrar por Categoría",
          "request": {
            "method": "GET",
            "header": [],
            "url": "{{ejercicios_url}}/api/ejercicios?categoria=Fuerza"
          }
        },
        {
          "name": "🔍 Ejercicios de Rutina",
          "request": {
            "method": "GET",
            "header": [],
            "url": "{{ejercicios_url}}/api/ejercicios/rutina/1"
          }
        },
        {
          "name": "⏱️ Tiempo Total de Rutina",
          "request": {
            "method": "GET",
            "header": [],
            "url": "{{ejercicios_url}}/api/ejercicios/rutina/1/tiempo-total"
          }
        },
        {
          "name": "➕ Crear Ejercicio - Press Banca",
          "request": {
            "method": "POST",
            "header": [{"key": "Content-Type", "value": "application/json"}],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"rutina_id\": 1,\n  \"nombre\": \"Press de banca\",\n  \"series\": 4,\n  \"repeticiones\": 10,\n  \"tiempo_descanso\": 90,\n  \"tiempo_ejecucion\": 15,\n  \"categoria\": \"Fuerza\"\n}"
            },
            "url": "{{ejercicios_url}}/api/ejercicios"
          }
        },
        {
          "name": "➕ Crear Ejercicio - Sentadillas",
          "request": {
            "method": "POST",
            "header": [{"key": "Content-Type", "value": "application/json"}],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"rutina_id\": 1,\n  \"nombre\": \"Sentadillas\",\n  \"series\": 5,\n  \"repeticiones\": 8,\n  \"tiempo_descanso\": 120,\n  \"tiempo_ejecucion\": 20,\n  \"categoria\": \"Fuerza\"\n}"
            },
            "url": "{{ejercicios_url}}/api/ejercicios"
          }
        },
        {
          "name": "➕ Crear Ejercicio - Burpees",
          "request": {
            "method": "POST",
            "header": [{"key": "Content-Type", "value": "application/json"}],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"rutina_id\": 2,\n  \"nombre\": \"Burpees\",\n  \"series\": 6,\n  \"repeticiones\": 15,\n  \"tiempo_descanso\": 30,\n  \"tiempo_ejecucion\": 45,\n  \"categoria\": \"HIIT\"\n}"
            },
            "url": "{{ejercicios_url}}/api/ejercicios"
          }
        },
        {
          "name": "✏️ Actualizar Ejercicio",
          "request": {
            "method": "PUT",
            "header": [{"key": "Content-Type", "value": "application/json"}],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"series\": 5,\n  \"repeticiones\": 12\n}"
            },
            "url": "{{ejercicios_url}}/api/ejercicios/1"
          }
        },
        {
          "name": "🗑️ Eliminar Ejercicio",
          "request": {
            "method": "DELETE",
            "header": [],
            "url": "{{ejercicios_url}}/api/ejercicios/1"
          }
        }
      ]
    }
  ]
}
```

4. Click en **"Import"**
5. ¡Listo! Verás una colección llamada **"Sistema Rutinas - Sara C"**

---

## 🎯 Método 2: Crear Requests Manualmente

Si prefieres crear las peticiones una por una:

### 🔵 PASO A: Crear una Rutina

1. **Crear nuevo request**
   - Click en "New" → "HTTP Request"
   - O presiona `Ctrl + N`

2. **Configurar el request**
   - Método: `POST`
   - URL: `http://localhost:8001/api/rutinas`

3. **Agregar el Body**
   - Selecciona la pestaña **"Body"**
   - Marca **"raw"**
   - Selecciona **"JSON"** en el dropdown

4. **Copiar este JSON**:
```json
{
  "nombre": "Rutina de Fuerza",
  "descripcion": "Entrenamiento para aumentar masa muscular",
  "duracion_estimada": 60,
  "nivel": "Intermedio"
}
```

5. **Click en "Send"**

**✅ Respuesta esperada** (Status 201):
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

---

### 🟢 PASO B: Listar Rutinas

1. **Nuevo request**
   - Método: `GET`
   - URL: `http://localhost:8001/api/rutinas`

2. **Click en "Send"**

**✅ Respuesta esperada**:
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

---

### 🟣 PASO C: Crear Ejercicios

1. **Nuevo request**
   - Método: `POST`
   - URL: `http://localhost:8002/api/ejercicios`

2. **Body (JSON)**:
```json
{
  "rutina_id": 1,
  "nombre": "Press de banca",
  "series": 4,
  "repeticiones": 10,
  "tiempo_descanso": 90,
  "tiempo_ejecucion": 15,
  "categoria": "Fuerza"
}
```

3. **Click en "Send"**

**Repite para más ejercicios**:

**Ejercicio 2 - Sentadillas**:
```json
{
  "rutina_id": 1,
  "nombre": "Sentadillas",
  "series": 5,
  "repeticiones": 8,
  "tiempo_descanso": 120,
  "tiempo_ejecucion": 20,
  "categoria": "Fuerza"
}
```

**Ejercicio 3 - Peso muerto**:
```json
{
  "rutina_id": 1,
  "nombre": "Peso muerto",
  "series": 4,
  "repeticiones": 8,
  "tiempo_descanso": 120,
  "tiempo_ejecucion": 20,
  "categoria": "Fuerza"
}
```

---

### 🟡 PASO D: Calcular Tiempo Total

1. **Nuevo request**
   - Método: `GET`
   - URL: `http://localhost:8002/api/ejercicios/rutina/1/tiempo-total`

2. **Click en "Send"**

**✅ Respuesta esperada**:
```json
{
  "rutina_id": 1,
  "total_ejercicios": 3,
  "tiempo_total_ejecucion": 240,
  "tiempo_total_descanso": 720,
  "tiempo_total_estimado": 960
}
```

📊 **Esto significa**: 960 segundos = 16 minutos de tiempo estimado

---

## 🎬 Flujo Completo de Prueba (Orden Recomendado)

### 1️⃣ Verificar que los servicios funcionen
```
GET http://localhost:8001/health
GET http://localhost:8002/health
```

### 2️⃣ Crear rutinas
```
POST http://localhost:8001/api/rutinas
(Crear 2-3 rutinas diferentes)
```

### 3️⃣ Listar rutinas creadas
```
GET http://localhost:8001/api/rutinas
```

### 4️⃣ Agregar ejercicios a las rutinas
```
POST http://localhost:8002/api/ejercicios
(Crear 3-4 ejercicios por rutina)
```

### 5️⃣ Ver ejercicios de una rutina
```
GET http://localhost:8002/api/ejercicios/rutina/1
```

### 6️⃣ Calcular tiempo total
```
GET http://localhost:8002/api/ejercicios/rutina/1/tiempo-total
```

### 7️⃣ Actualizar datos
```
PUT http://localhost:8001/api/rutinas/1
PUT http://localhost:8002/api/ejercicios/1
```

### 8️⃣ Eliminar (opcional)
```
DELETE http://localhost:8002/api/ejercicios/1
DELETE http://localhost:8001/api/rutinas/1
```

---

## 📋 Lista de Todos los Endpoints

### Microservicio Rutinas (Puerto 8001)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/health` | ✅ Health check |
| GET | `/api/rutinas` | 📋 Listar rutinas |
| GET | `/api/rutinas/{id}` | 🔍 Obtener rutina |
| POST | `/api/rutinas` | ➕ Crear rutina |
| PUT | `/api/rutinas/{id}` | ✏️ Actualizar rutina |
| DELETE | `/api/rutinas/{id}` | 🗑️ Eliminar rutina |

### Microservicio Ejercicios (Puerto 8002)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/health` | ✅ Health check |
| GET | `/api/ejercicios` | 📋 Listar ejercicios |
| GET | `/api/ejercicios?categoria=X` | 🔍 Filtrar por categoría |
| GET | `/api/ejercicios/{id}` | 🔍 Obtener ejercicio |
| GET | `/api/ejercicios/rutina/{id}` | 📦 Ejercicios de rutina |
| GET | `/api/ejercicios/rutina/{id}/tiempo-total` | ⏱️ Calcular tiempos |
| POST | `/api/ejercicios` | ➕ Crear ejercicio |
| PUT | `/api/ejercicios/{id}` | ✏️ Actualizar ejercicio |
| DELETE | `/api/ejercicios/{id}` | 🗑️ Eliminar ejercicio |

---

## 📝 Valores Válidos

### Niveles de Rutina
- `Principiante`
- `Intermedio`
- `Avanzado`

### Categorías de Ejercicio
- `Fuerza`
- `Cardio`
- `Flexibilidad`
- `Resistencia`
- `HIIT`
- `Funcional`

---

## 🐛 Solución de Problemas

### ❌ Error: "Could not get response"
**Solución**: Verifica que los servicios estén corriendo
```cmd
docker-compose ps
```

### ❌ Error 404: "Not Found"
**Solución**: Revisa que la URL sea correcta:
- ✅ Correcto: `http://localhost:8001/api/rutinas`
- ❌ Incorrecto: `http://localhost:8001/rutinas`

### ❌ Error 422: "Validation Error"
**Solución**: Revisa que el JSON tenga todos los campos requeridos y valores válidos

### ❌ Error 400: "Nivel inválido" o "Categoría inválida"
**Solución**: Usa solo los valores válidos listados arriba

---

## 🎯 Tips para Postman

1. **Guarda tus requests**: Crea una colección para organizarlos
2. **Usa variables**: Define `{{rutinas_url}}` y `{{ejercicios_url}}`
3. **Revisa la respuesta**: Status Code y Body
4. **Copia el ID**: Usa los IDs devueltos para los siguientes requests
5. **Documenta**: Agrega descripciones a tus requests

---

## 🌐 Alternativa: Usar Swagger UI

Si prefieres una interfaz visual más simple:

1. **Abre tu navegador**
2. **Ve a**:
   - Rutinas: http://localhost:8001/docs
   - Ejercicios: http://localhost:8002/docs
3. **Prueba directamente** desde la interfaz Swagger

---

## ✅ Verificación Final

Ejecuta este flujo para verificar que todo funcione:

1. ✅ Health checks en ambos servicios
2. ✅ Crear 1 rutina → Obtener ID
3. ✅ Crear 2-3 ejercicios con ese rutina_id
4. ✅ Listar ejercicios de la rutina
5. ✅ Calcular tiempo total
6. ✅ Actualizar un ejercicio
7. ✅ Ver el cambio reflejado

**¡Si todo esto funciona, tu API está 100% operativa!** 🎉

---

## 📸 Capturas Recomendadas para Documentar

1. Screenshot del health check
2. Screenshot creando una rutina
3. Screenshot del listado de rutinas
4. Screenshot creando ejercicios
5. Screenshot del cálculo de tiempo total

Guarda estas capturas para tu presentación/entrega.
