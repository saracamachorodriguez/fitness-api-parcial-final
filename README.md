# Sistema de Registro de Rutinas de Ejercicio

## Descripción
API REST con arquitectura de microservicios para registrar rutinas, ejercicios y tiempos de entrenamiento.

## Arquitectura
- **Microservicio de Rutinas**: Gestiona las rutinas de entrenamiento
- **Microservicio de Ejercicios**: Gestiona ejercicios individuales y tiempos de ejecución

## Tecnologías
- Python 3.11+
- FastAPI
- SQLite (base de datos local)
- Docker & Docker Compose
- Pytest (pruebas unitarias)

## Estructura del Proyecto
```
.
├── rutinas-service/          # Microservicio de rutinas
├── ejercicios-service/       # Microservicio de ejercicios
├── docker-compose.yml        # Orquestación de servicios
└── README.md
```

## Instalación Local

### Prerrequisitos
- Python 3.11+
- Docker y Docker Compose

### Opción 1: Ejecutar con Docker
```bash
docker-compose up --build
```

### Opción 2: Ejecutar localmente
```bash
# Servicio de Rutinas
cd rutinas-service
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8001

# Servicio de Ejercicios
cd ejercicios-service
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8002
```

## Endpoints

### Microservicio de Rutinas (Puerto 8001)
- `GET /api/rutinas` - Listar todas las rutinas
- `GET /api/rutinas/{id}` - Obtener una rutina específica
- `POST /api/rutinas` - Crear nueva rutina
- `PUT /api/rutinas/{id}` - Actualizar rutina
- `DELETE /api/rutinas/{id}` - Eliminar rutina
- `GET /health` - Health check

### Microservicio de Ejercicios (Puerto 8002)
- `GET /api/ejercicios` - Listar todos los ejercicios
- `GET /api/ejercicios/{id}` - Obtener un ejercicio específico
- `POST /api/ejercicios` - Crear nuevo ejercicio
- `PUT /api/ejercicios/{id}` - Actualizar ejercicio
- `DELETE /api/ejercicios/{id}` - Eliminar ejercicio
- `GET /api/ejercicios/rutina/{rutina_id}` - Obtener ejercicios de una rutina
- `GET /health` - Health check

## Documentación Interactiva
- Rutinas: http://localhost:8001/docs
- Ejercicios: http://localhost:8002/docs

## Pruebas Unitarias
```bash
# Servicio de Rutinas
cd rutinas-service
pytest

# Servicio de Ejercicios
cd ejercicios-service
pytest
```

## Despliegue en la Nube

### Opción 1: Render
1. Crear cuenta en Render.com
2. Crear dos Web Services (uno para cada microservicio)
3. Conectar con el repositorio de GitHub
4. Configurar:
   - Build Command: `pip install -r requirements.txt`
   - Start Command para rutinas: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Start Command para ejercicios: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Opción 2: Railway
1. Crear cuenta en Railway.app
2. Crear nuevo proyecto y agregar dos servicios
3. Configurar variables de entorno si es necesario
4. Railway detectará automáticamente Python y FastAPI

### Opción 3: Azure/AWS/GCP
Ver documentación específica en `DEPLOYMENT.md`

## Modelos de Datos

### Rutina
```json
{
  "id": 1,
  "nombre": "Rutina de Fuerza",
  "descripcion": "Entrenamiento enfocado en fuerza muscular",
  "duracion_estimada": 60,
  "nivel": "Intermedio",
  "fecha_creacion": "2025-12-04T10:00:00"
}
```

### Ejercicio
```json
{
  "id": 1,
  "rutina_id": 1,
  "nombre": "Press de banca",
  "series": 4,
  "repeticiones": 10,
  "tiempo_descanso": 90,
  "tiempo_ejecucion": 15,
  "categoria": "Fuerza"
}
```

## Autor
Sara C. - Parcial Final Programación
