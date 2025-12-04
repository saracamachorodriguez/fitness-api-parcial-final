# Arquitectura del Sistema

## Visión General

El sistema está diseñado con una arquitectura de **microservicios** que separa las responsabilidades en dos servicios independientes y escalables.

```
┌─────────────────────────────────────────────────────────┐
│                      CLIENTE                             │
│         (Navegador, Postman, App Móvil)                 │
└────────────────┬────────────────────────────────────────┘
                 │
                 │ HTTP/REST/JSON
                 │
    ┌────────────┴────────────┐
    │                         │
    ▼                         ▼
┌───────────────┐       ┌───────────────┐
│   RUTINAS     │       │  EJERCICIOS   │
│   SERVICE     │       │   SERVICE     │
│  (Port 8001)  │       │  (Port 8002)  │
└───────┬───────┘       └───────┬───────┘
        │                       │
        ▼                       ▼
  ┌──────────┐           ┌──────────┐
  │ SQLite   │           │ SQLite   │
  │ rutinas  │           │ejercicios│
  └──────────┘           └──────────┘
```

## Componentes

### 1. Microservicio de Rutinas

**Responsabilidad**: Gestionar las rutinas de entrenamiento

**Tecnologías**:
- FastAPI (Framework web)
- SQLite (Base de datos)
- Pydantic (Validación de datos)
- Uvicorn (Servidor ASGI)

**Base de datos**:
```sql
CREATE TABLE rutinas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    duracion_estimada INTEGER NOT NULL,
    nivel TEXT NOT NULL,
    fecha_creacion TEXT NOT NULL
);
```

**Endpoints**:
- `GET /api/rutinas` - Listar rutinas
- `POST /api/rutinas` - Crear rutina
- `GET /api/rutinas/{id}` - Obtener rutina
- `PUT /api/rutinas/{id}` - Actualizar rutina
- `DELETE /api/rutinas/{id}` - Eliminar rutina

### 2. Microservicio de Ejercicios

**Responsabilidad**: Gestionar ejercicios individuales y calcular tiempos

**Tecnologías**:
- FastAPI
- SQLite
- Pydantic
- Uvicorn

**Base de datos**:
```sql
CREATE TABLE ejercicios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rutina_id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    series INTEGER NOT NULL,
    repeticiones INTEGER NOT NULL,
    tiempo_descanso INTEGER NOT NULL,
    tiempo_ejecucion INTEGER NOT NULL,
    categoria TEXT NOT NULL,
    fecha_creacion TEXT NOT NULL
);
```

**Endpoints**:
- `GET /api/ejercicios` - Listar ejercicios
- `POST /api/ejercicios` - Crear ejercicio
- `GET /api/ejercicios/{id}` - Obtener ejercicio
- `GET /api/ejercicios/rutina/{rutina_id}` - Ejercicios por rutina
- `GET /api/ejercicios/rutina/{rutina_id}/tiempo-total` - Calcular tiempos
- `PUT /api/ejercicios/{id}` - Actualizar ejercicio
- `DELETE /api/ejercicios/{id}` - Eliminar ejercicio

## Principios de Diseño

### 1. Separación de Responsabilidades (SoC)
Cada microservicio tiene una responsabilidad única y bien definida.

### 2. Comunicación REST/JSON
Los servicios exponen APIs REST que devuelven datos en formato JSON.

### 3. Independencia de Servicios
- Cada servicio tiene su propia base de datos
- Pueden desplegarse, escalarse y actualizarse independientemente
- Fallos en un servicio no afectan al otro

### 4. Stateless
Los servicios no mantienen estado de sesión, lo que facilita el escalamiento horizontal.

### 5. Documentación Automática
Cada servicio genera automáticamente documentación interactiva (Swagger/OpenAPI).

## Flujo de Datos

### Crear una Rutina Completa

```
1. Cliente → POST /api/rutinas
   ↓
2. Rutinas Service crea rutina → devuelve {id: 1}
   ↓
3. Cliente → POST /api/ejercicios (con rutina_id: 1)
   ↓
4. Ejercicios Service crea ejercicio
   ↓
5. Cliente → GET /api/ejercicios/rutina/1/tiempo-total
   ↓
6. Ejercicios Service calcula y devuelve tiempos
```

### Ejemplo de Flujo Completo

```json
// Paso 1: Crear rutina
POST /api/rutinas
{
  "nombre": "Rutina Full Body",
  "descripcion": "Entrenamiento de cuerpo completo",
  "duracion_estimada": 60,
  "nivel": "Intermedio"
}
→ Respuesta: {"id": 1, ...}

// Paso 2: Agregar ejercicios
POST /api/ejercicios
{
  "rutina_id": 1,
  "nombre": "Press de banca",
  "series": 4,
  "repeticiones": 10,
  "tiempo_descanso": 90,
  "tiempo_ejecucion": 15,
  "categoria": "Fuerza"
}

POST /api/ejercicios
{
  "rutina_id": 1,
  "nombre": "Sentadillas",
  "series": 4,
  "repeticiones": 12,
  "tiempo_descanso": 90,
  "tiempo_ejecucion": 20,
  "categoria": "Fuerza"
}

// Paso 3: Consultar ejercicios de la rutina
GET /api/ejercicios/rutina/1
→ Devuelve lista de ejercicios

// Paso 4: Calcular tiempo total
GET /api/ejercicios/rutina/1/tiempo-total
→ {
  "rutina_id": 1,
  "total_ejercicios": 2,
  "tiempo_total_ejecucion": 140,
  "tiempo_total_descanso": 540,
  "tiempo_total_estimado": 680
}
```

## Escalabilidad

### Horizontal
Cada servicio puede escalarse independientemente:

```
┌─────────────┐
│ Load        │
│ Balancer    │
└──────┬──────┘
       │
   ┌───┴────┐
   │        │
   ▼        ▼
┌────┐   ┌────┐
│R-1 │   │R-2 │  (Múltiples instancias del servicio de rutinas)
└────┘   └────┘

   ┌───┴────┐
   │        │
   ▼        ▼
┌────┐   ┌────┐   ┌────┐
│E-1 │   │E-2 │   │E-3 │  (Múltiples instancias de ejercicios)
└────┘   └────┘   └────┘
```

### Vertical
Aumentar recursos (CPU, RAM) de los contenedores según la carga.

## Seguridad

### Implementado
- ✅ Validación de entrada con Pydantic
- ✅ Manejo de errores HTTP apropiado
- ✅ CORS configurado
- ✅ Documentación de API

### Recomendado para Producción
- 🔒 Autenticación JWT/OAuth2
- 🔒 Rate limiting
- 🔒 HTTPS/TLS
- 🔒 Sanitización de SQL (ORM)
- 🔒 Variables de entorno para secretos

## Monitoreo y Observabilidad

### Health Checks
Cada servicio expone `/health` para verificar su estado:

```json
GET /health
→ {
  "status": "healthy",
  "service": "rutinas-service",
  "timestamp": "2025-12-04T10:30:00"
}
```

### Logs
Los logs se pueden consultar con:
```bash
docker-compose logs -f [servicio]
```

### Métricas Recomendadas
- Tasa de solicitudes por segundo
- Latencia promedio
- Tasa de errores
- Uso de CPU/RAM
- Uptime

## Dockerización

### Ventajas
- ✅ Entorno consistente en desarrollo y producción
- ✅ Fácil despliegue
- ✅ Aislamiento de dependencias
- ✅ Portabilidad

### Estructura
```
proyecto/
├── rutinas-service/
│   ├── Dockerfile          # Imagen del servicio
│   ├── requirements.txt    # Dependencias Python
│   └── main.py            # Código de la aplicación
├── ejercicios-service/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── main.py
└── docker-compose.yml     # Orquestación de servicios
```

### Volúmenes
Los datos se persisten en volúmenes Docker:
- `rutinas-data`: Base de datos de rutinas
- `ejercicios-data`: Base de datos de ejercicios

## Testing

### Estrategia de Pruebas

1. **Pruebas Unitarias** (pytest)
   - Cada endpoint tiene tests
   - Cobertura > 80%
   - Base de datos temporal para tests

2. **Pruebas de Integración**
   - Flujos completos CRUD
   - Validación de reglas de negocio

3. **Pruebas E2E** (opcional)
   - Pruebas de extremo a extremo con ambos servicios

### Ejecutar Tests
```bash
# Servicio de rutinas
cd rutinas-service
pytest -v

# Servicio de ejercicios
cd ejercicios-service
pytest -v
```

## CI/CD

### Pipeline Recomendado

```
┌─────────┐    ┌──────┐    ┌───────┐    ┌─────────┐
│  Code   │ →  │ Test │ →  │ Build │ →  │ Deploy  │
│ Commit  │    │      │    │ Image │    │ to Cloud│
└─────────┘    └──────┘    └───────┘    └─────────┘
```

### GitHub Actions (Ejemplo)
```yaml
name: CI/CD
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Tests
        run: |
          cd rutinas-service && pytest
          cd ../ejercicios-service && pytest
  
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Render
        run: # deploy commands
```

## Mejoras Futuras

### Corto Plazo
1. Implementar autenticación de usuarios
2. Agregar paginación en listados
3. Implementar búsqueda y filtros avanzados
4. Agregar validación de integridad referencial entre servicios

### Mediano Plazo
1. Migrar a PostgreSQL/MySQL
2. Implementar caché con Redis
3. Agregar API Gateway (Kong, Traefik)
4. Implementar circuit breakers
5. Agregar métricas con Prometheus

### Largo Plazo
1. Service mesh (Istio, Linkerd)
2. Event-driven architecture (RabbitMQ, Kafka)
3. GraphQL API
4. App móvil nativa
5. Machine Learning para recomendaciones

## Comparación con Monolito

| Aspecto | Monolito | Microservicios |
|---------|----------|----------------|
| Despliegue | Todo junto | Independiente |
| Escalabilidad | Vertical | Horizontal |
| Tecnología | Una sola | Múltiples posibles |
| Complejidad | Menor | Mayor |
| Mantenimiento | Más simple | Requiere orquestación |
| Resiliencia | Fallo total | Fallo parcial |

## Conclusiones

Esta arquitectura de microservicios ofrece:

✅ **Modularidad**: Servicios independientes y cohesivos
✅ **Escalabilidad**: Escala según demanda de cada servicio
✅ **Mantenibilidad**: Código organizado y fácil de mantener
✅ **Resiliencia**: Fallos aislados no afectan todo el sistema
✅ **Flexibilidad**: Fácil agregar nuevos servicios
✅ **Despliegue**: CI/CD automatizable

Para más información, consulta:
- `README.md` - Visión general
- `DEPLOYMENT.md` - Guía de despliegue
- `QUICKSTART.md` - Inicio rápido
