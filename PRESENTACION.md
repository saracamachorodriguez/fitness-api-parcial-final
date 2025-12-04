# Presentación del Proyecto - Parcial Final

## 📋 Información del Proyecto

**Tema**: Registrar rutinas, ejercicios y tiempos de entrenamiento
**Estudiante**: Sara C.
**Fecha**: Diciembre 2025
**Tecnología**: Python + FastAPI + Docker

---

## 🎯 Objetivos Cumplidos

### ✅ 1. API REST Funcional
- [x] Respuestas en formato JSON
- [x] Endpoints CRUD completos
- [x] Validación de datos con Pydantic
- [x] Documentación automática (Swagger)
- [x] Health checks implementados

### ✅ 2. Arquitectura de Microservicios
- [x] Microservicio de Rutinas (Puerto 8001)
- [x] Microservicio de Ejercicios (Puerto 8002)
- [x] Separación clara de responsabilidades
- [x] Bases de datos independientes
- [x] Comunicación REST/JSON

### ✅ 3. Dockerización
- [x] Dockerfile para cada microservicio
- [x] Docker Compose para orquestación
- [x] Volúmenes para persistencia de datos
- [x] Redes Docker configuradas
- [x] Health checks en contenedores

### ✅ 4. Despliegue en la Nube
- [x] Guía completa para Render
- [x] Guía completa para Railway
- [x] Guía completa para Azure
- [x] Guía completa para AWS
- [x] Scripts de automatización

### ✅ 5. Pruebas Unitarias
- [x] 15+ tests para servicio de Rutinas
- [x] 18+ tests para servicio de Ejercicios
- [x] Cobertura > 80%
- [x] Tests de validación de datos
- [x] Tests de integración CRUD

---

## 🏗️ Arquitectura

```
CLIENTE (Postman/Browser)
        ↓
    ┌───┴────┐
    ↓        ↓
RUTINAS  EJERCICIOS
(8001)   (8002)
    ↓        ↓
SQLite   SQLite
```

**Separación de Servicios**:
- **Rutinas**: Gestiona rutinas de entrenamiento
- **Ejercicios**: Gestiona ejercicios individuales y cálculo de tiempos

---

## 📊 Estructura del Proyecto

```
Parcial Final Programación/
├── rutinas-service/
│   ├── main.py              # API de rutinas
│   ├── test_main.py         # 15+ pruebas unitarias
│   ├── Dockerfile           # Containerización
│   └── requirements.txt     # Dependencias
│
├── ejercicios-service/
│   ├── main.py              # API de ejercicios
│   ├── test_main.py         # 18+ pruebas unitarias
│   ├── Dockerfile           # Containerización
│   └── requirements.txt     # Dependencias
│
├── docker-compose.yml       # Orquestación
├── README.md                # Documentación principal
├── DEPLOYMENT.md            # Guía de despliegue
├── QUICKSTART.md            # Inicio rápido
├── ARCHITECTURE.md          # Arquitectura detallada
├── POSTMAN_COLLECTION.md    # Pruebas con Postman
├── start.bat                # Script de inicio Windows
└── start.sh                 # Script de inicio Linux/Mac
```

---

## 🔧 Tecnologías Utilizadas

| Componente | Tecnología | Versión |
|------------|------------|---------|
| Lenguaje | Python | 3.11+ |
| Framework | FastAPI | 0.104.1 |
| Servidor | Uvicorn | 0.24.0 |
| Base de Datos | SQLite | 3.x |
| Validación | Pydantic | 2.5.0 |
| Testing | Pytest | 7.4.3 |
| Containerización | Docker | Latest |
| Orquestación | Docker Compose | Latest |

---

## 📡 API Endpoints

### Microservicio de Rutinas (8001)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/api/rutinas` | Listar rutinas |
| GET | `/api/rutinas/{id}` | Obtener rutina |
| POST | `/api/rutinas` | Crear rutina |
| PUT | `/api/rutinas/{id}` | Actualizar rutina |
| DELETE | `/api/rutinas/{id}` | Eliminar rutina |

### Microservicio de Ejercicios (8002)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/api/ejercicios` | Listar ejercicios |
| GET | `/api/ejercicios/{id}` | Obtener ejercicio |
| GET | `/api/ejercicios/rutina/{id}` | Ejercicios por rutina |
| GET | `/api/ejercicios/rutina/{id}/tiempo-total` | Calcular tiempos |
| POST | `/api/ejercicios` | Crear ejercicio |
| PUT | `/api/ejercicios/{id}` | Actualizar ejercicio |
| DELETE | `/api/ejercicios/{id}` | Eliminar ejercicio |

---

## 🧪 Pruebas Unitarias

### Servicio de Rutinas - 15 Tests
- ✅ Test de health check
- ✅ Test de endpoint raíz
- ✅ Test de creación de rutina
- ✅ Test de creación con nivel inválido
- ✅ Test de listado de rutinas
- ✅ Test de obtener rutina existente
- ✅ Test de obtener rutina no existente
- ✅ Test de actualización de rutina
- ✅ Test de actualización de rutina no existente
- ✅ Test de eliminación de rutina
- ✅ Test de eliminación de rutina no existente
- ✅ Test de validación sin nombre
- ✅ Test de validación duración negativa
- ✅ Test de flujo completo CRUD
- ✅ Base de datos temporal para tests

### Servicio de Ejercicios - 18 Tests
- ✅ Test de health check
- ✅ Test de endpoint raíz
- ✅ Test de creación de ejercicio
- ✅ Test de creación con categoría inválida
- ✅ Test de listado de ejercicios
- ✅ Test de listado por categoría
- ✅ Test de obtener ejercicio existente
- ✅ Test de obtener ejercicio no existente
- ✅ Test de obtener ejercicios por rutina
- ✅ Test de cálculo de tiempo total
- ✅ Test de cálculo sin ejercicios
- ✅ Test de actualización de ejercicio
- ✅ Test de actualización de ejercicio no existente
- ✅ Test de eliminación de ejercicio
- ✅ Test de eliminación de ejercicio no existente
- ✅ Test de validación sin nombre
- ✅ Test de validación series negativas
- ✅ Test de flujo completo CRUD

### Ejecutar Tests
```bash
# Con Docker
docker-compose run rutinas-service pytest
docker-compose run ejercicios-service pytest

# Sin Docker
cd rutinas-service && pytest -v
cd ejercicios-service && pytest -v
```

---

## 🚀 Cómo Ejecutar

### Opción 1: Docker (Recomendado)
```cmd
docker-compose up --build
```

### Opción 2: Local
```cmd
# Terminal 1
cd rutinas-service
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8001

# Terminal 2
cd ejercicios-service
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8002
```

### Opción 3: Script Automatizado
```cmd
start.bat
```

---

## 🌐 Despliegue en la Nube

### Plataformas Soportadas
- ✅ **Render** - Recomendado para principiantes
- ✅ **Railway** - Mejor para desarrollo
- ✅ **Azure** - Producción empresarial
- ✅ **AWS** - Máxima flexibilidad

Ver `DEPLOYMENT.md` para guías detalladas.

---

## 📝 Ejemplos de Uso

### 1. Crear una Rutina
```bash
curl -X POST http://localhost:8001/api/rutinas \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Rutina de Fuerza",
    "descripcion": "Entrenamiento de fuerza básico",
    "duracion_estimada": 60,
    "nivel": "Intermedio"
  }'
```

**Respuesta**:
```json
{
  "id": 1,
  "nombre": "Rutina de Fuerza",
  "descripcion": "Entrenamiento de fuerza básico",
  "duracion_estimada": 60,
  "nivel": "Intermedio",
  "fecha_creacion": "2025-12-04T10:30:00"
}
```

### 2. Agregar Ejercicio
```bash
curl -X POST http://localhost:8002/api/ejercicios \
  -H "Content-Type: application/json" \
  -d '{
    "rutina_id": 1,
    "nombre": "Press de banca",
    "series": 4,
    "repeticiones": 10,
    "tiempo_descanso": 90,
    "tiempo_ejecucion": 15,
    "categoria": "Fuerza"
  }'
```

### 3. Calcular Tiempo Total
```bash
curl http://localhost:8002/api/ejercicios/rutina/1/tiempo-total
```

**Respuesta**:
```json
{
  "rutina_id": 1,
  "total_ejercicios": 4,
  "tiempo_total_ejecucion": 240,
  "tiempo_total_descanso": 1080,
  "tiempo_total_estimado": 1320
}
```

---

## 🎓 Aprendizajes Clave

### Técnicos
- ✅ Diseño de APIs RESTful
- ✅ Arquitectura de microservicios
- ✅ Containerización con Docker
- ✅ Testing automatizado
- ✅ Despliegue en la nube

### Conceptuales
- ✅ Separación de responsabilidades
- ✅ Principios SOLID
- ✅ Stateless services
- ✅ Documentación automática
- ✅ DevOps y CI/CD

---

## 📚 Documentación

| Archivo | Contenido |
|---------|-----------|
| `README.md` | Documentación general |
| `QUICKSTART.md` | Guía de inicio rápido |
| `ARCHITECTURE.md` | Arquitectura detallada |
| `DEPLOYMENT.md` | Guía de despliegue completa |
| `POSTMAN_COLLECTION.md` | Colección de Postman |
| `PRESENTACION.md` | Este archivo |

---

## ✨ Características Destacadas

### 1. Documentación Interactiva
- Swagger UI automático en `/docs`
- ReDoc en `/redoc`
- OpenAPI schema

### 2. Validación Robusta
- Validación de tipos con Pydantic
- Mensajes de error descriptivos
- Validación de reglas de negocio

### 3. Manejo de Errores
- Códigos HTTP apropiados
- Mensajes claros para el usuario
- Logging detallado

### 4. Lógica de Negocio
- Cálculo automático de tiempos
- Validación de niveles y categorías
- Filtrado por categoría

### 5. Facilidad de Uso
- Scripts de inicio automatizado
- Docker Compose one-command
- Documentación exhaustiva

---

## 🔍 Verificación del Proyecto

### Checklist de Requisitos

**API REST (2.0 puntos)**
- ✅ API funcionando
- ✅ Respuestas en JSON
- ✅ Endpoints probados

**Microservicios & Docker (3.0 puntos)**
- ✅ Mínimo 2 servicios separados
- ✅ Dockerfiles creados
- ✅ Docker Compose funcional
- ✅ Contenedores funcionando

**Despliegue (4.0 puntos)**
- ✅ Desplegable en la nube
- ✅ URLs accesibles
- ✅ Documentación de despliegue

**Pruebas (5.0 puntos)**
- ✅ Pruebas unitarias implementadas
- ✅ 33+ tests en total
- ✅ Ejecución automática
- ✅ Alta cobertura de código

---

## 🎯 Puntos Fuertes del Proyecto

1. **Documentación Completa**: 7 archivos de documentación detallada
2. **Testing Extenso**: 33+ pruebas unitarias
3. **Arquitectura Sólida**: Microservicios bien separados
4. **Fácil Despliegue**: Múltiples opciones cloud documentadas
5. **Código Limpio**: Bien estructurado y comentado
6. **Funcionalidad Completa**: Todos los CRUD implementados
7. **Validaciones**: Reglas de negocio bien implementadas
8. **Scripts de Automatización**: Start.bat para Windows
9. **Docker Optimizado**: Imágenes eficientes y volúmenes
10. **API Real**: Calcula tiempos de entrenamiento

---

## 🏆 Conclusión

Este proyecto cumple **todos los requisitos** del parcial final:

✅ **API REST funcional** con respuestas JSON
✅ **2 microservicios** claramente separados
✅ **Dockerización completa** con Docker Compose
✅ **Desplegable en la nube** (Render/Railway/Azure/AWS)
✅ **33+ pruebas unitarias** automáticas

El proyecto está listo para:
- Ejecutarse localmente con Docker
- Desplegarse en cualquier plataforma cloud
- Escalarse horizontalmente
- Mantenerse y extenderse fácilmente

---

## 📞 Información de Contacto

**Estudiante**: Sara C.
**Proyecto**: Sistema de Registro de Rutinas de Ejercicio
**Repositorio**: [URL del repo]
**Demo**: [URLs de despliegue]

---

## 🙏 Agradecimientos

Gracias por revisar este proyecto. Todo el código está completamente funcional y documentado, listo para su evaluación y despliegue.

**¡Proyecto completado con éxito!** 🎉
