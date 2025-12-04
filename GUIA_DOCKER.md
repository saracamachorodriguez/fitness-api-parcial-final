# 🐳 Guía Completa de Docker para el Proyecto

## ✅ Estado Actual

Tus servicios están corriendo en Docker:
- **rutinas-service**: Puerto 8001
- **ejercicios-service**: Puerto 8002

---

## 📋 Comandos Básicos de Docker

### 1️⃣ Ver Contenedores en Ejecución

```cmd
docker-compose ps
```

**Salida esperada:**
```
NAME                 IMAGE                                 STATUS          PORTS
ejercicios-service   ejercicios-service                    Up 17 minutes   0.0.0.0:8002->8002/tcp
rutinas-service      rutinas-service                       Up 17 minutes   0.0.0.0:8001->8001/tcp
```

### 2️⃣ Ver Logs de los Servicios

**Ver logs en tiempo real (todos los servicios):**
```cmd
docker-compose logs -f
```

**Ver logs solo de rutinas:**
```cmd
docker-compose logs -f rutinas-service
```

**Ver logs solo de ejercicios:**
```cmd
docker-compose logs -f ejercicios-service
```

**Ver últimas 50 líneas:**
```cmd
docker-compose logs --tail=50
```

### 3️⃣ Detener los Servicios

**Detener pero mantener los contenedores:**
```cmd
docker-compose stop
```

**Detener y eliminar contenedores:**
```cmd
docker-compose down
```

**Detener y eliminar TODO (incluyendo volúmenes con datos):**
```cmd
docker-compose down -v
```

### 4️⃣ Iniciar los Servicios

**Iniciar en primer plano (ver logs):**
```cmd
docker-compose up
```

**Iniciar en segundo plano (modo detached):**
```cmd
docker-compose up -d
```

**Reconstruir imágenes y luego iniciar:**
```cmd
docker-compose up --build
```

**Forzar recreación de contenedores:**
```cmd
docker-compose up --force-recreate
```

### 5️⃣ Reiniciar Servicios

**Reiniciar todos:**
```cmd
docker-compose restart
```

**Reiniciar uno específico:**
```cmd
docker-compose restart rutinas-service
```

### 6️⃣ Ver Recursos Usados

**Ver uso de CPU, RAM, Red:**
```cmd
docker stats
```

### 7️⃣ Ejecutar Comandos Dentro de un Contenedor

**Abrir terminal en el contenedor de rutinas:**
```cmd
docker-compose exec rutinas-service /bin/sh
```

**Ejecutar tests dentro del contenedor:**
```cmd
docker-compose exec rutinas-service pytest -v
```

```cmd
docker-compose exec ejercicios-service pytest -v
```

**Ver archivos dentro del contenedor:**
```cmd
docker-compose exec rutinas-service ls -la
```

### 8️⃣ Ver Imágenes Docker

**Listar imágenes creadas:**
```cmd
docker images
```

**Eliminar imágenes no usadas:**
```cmd
docker image prune
```

### 9️⃣ Ver Volúmenes (Datos Persistentes)

**Listar volúmenes:**
```cmd
docker volume ls
```

**Ver detalles de un volumen:**
```cmd
docker volume inspect parcialfinalprogramacin_rutinas-data
```

**Eliminar volúmenes no usados:**
```cmd
docker volume prune
```

### 🔟 Limpiar Todo Docker

**Eliminar contenedores detenidos, redes no usadas, imágenes huérfanas:**
```cmd
docker system prune
```

**Limpieza completa (¡CUIDADO! Borra TODO):**
```cmd
docker system prune -a --volumes
```

---

## 🎯 Comandos para tu Presentación/Demo

### Mostrar que Docker está corriendo:
```cmd
docker-compose ps
```

### Ver logs en tiempo real:
```cmd
docker-compose logs -f
```

### Reiniciar servicios:
```cmd
docker-compose restart
```

### Reconstruir y lanzar:
```cmd
docker-compose up --build -d
```

### Ejecutar tests:
```cmd
docker-compose exec rutinas-service pytest -v
docker-compose exec ejercicios-service pytest -v
```

### Ver uso de recursos:
```cmd
docker stats --no-stream
```

---

## 📊 Arquitectura Docker de tu Proyecto

```
┌─────────────────────────────────────────┐
│         Docker Compose                  │
│  (Orquesta todos los servicios)        │
└─────────────────────────────────────────┘
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
┌──────────────┐    ┌──────────────┐
│  Contenedor  │    │  Contenedor  │
│   Rutinas    │    │  Ejercicios  │
│  (Puerto     │    │  (Puerto     │
│   8001)      │    │   8002)      │
└──────┬───────┘    └──────┬───────┘
       │                   │
       ▼                   ▼
┌──────────────┐    ┌──────────────┐
│   Volumen    │    │   Volumen    │
│  rutinas.db  │    │ejercicios.db │
└──────────────┘    └──────────────┘
```

---

## 🔍 Verificar que Todo Funciona

### 1. Ver que los contenedores están UP:
```cmd
docker-compose ps
```

### 2. Ver los últimos logs:
```cmd
docker-compose logs --tail=20
```

### 3. Probar health checks:
```cmd
curl http://localhost:8001/health
curl http://localhost:8002/health
```

### 4. Ver recursos:
```cmd
docker stats --no-stream
```

---

## 🛠️ Solución de Problemas

### Problema: "Port already in use"
**Solución:**
```cmd
docker-compose down
netstat -ano | findstr :8001
netstat -ano | findstr :8002
REM Mata el proceso si es necesario
taskkill /PID <numero_proceso> /F
docker-compose up -d
```

### Problema: Los contenedores se detienen
**Solución:**
```cmd
docker-compose logs rutinas-service
docker-compose logs ejercicios-service
REM Ver el error y corregir
docker-compose up --build
```

### Problema: Cambios en código no se reflejan
**Solución:**
```cmd
docker-compose down
docker-compose up --build
```

### Problema: Base de datos corrupta
**Solución:**
```cmd
docker-compose down -v
docker-compose up -d
REM Volver a crear datos con crear_datos_prueba.bat
```

### Problema: Sin espacio en disco
**Solución:**
```cmd
docker system prune -a
```

---

## 📸 Capturas para tu Presentación

1. **docker-compose ps** → Muestra servicios corriendo
2. **docker-compose logs** → Muestra logs de actividad
3. **docker stats** → Muestra uso de recursos
4. **docker images** → Muestra imágenes creadas
5. **docker volume ls** → Muestra volúmenes de datos

---

## 🎓 Ventajas de Docker en tu Proyecto

✅ **Portabilidad**: Funciona igual en cualquier sistema
✅ **Aislamiento**: Cada servicio en su propio contenedor
✅ **Escalabilidad**: Fácil crear múltiples instancias
✅ **Reproducibilidad**: Mismo entorno en dev y producción
✅ **Gestión simple**: Un comando para todo (docker-compose)

---

## 🚀 Workflow de Desarrollo

### Desarrollo Local:
```cmd
# 1. Iniciar servicios
docker-compose up -d

# 2. Ver logs mientras desarrollas
docker-compose logs -f

# 3. Si cambias código, reconstruir
docker-compose up --build -d

# 4. Ejecutar tests
docker-compose exec rutinas-service pytest -v
docker-compose exec ejercicios-service pytest -v

# 5. Al terminar
docker-compose down
```

### Para Demo/Presentación:
```cmd
# Iniciar todo limpio
docker-compose down -v
docker-compose up --build -d

# Crear datos de prueba
crear_datos_prueba.bat

# Mostrar estado
docker-compose ps
docker stats --no-stream

# Probar endpoints en Postman
```

---

## 📦 Archivos Docker en tu Proyecto

### `docker-compose.yml`
Orquesta ambos servicios, define puertos, volúmenes y redes.

### `rutinas-service/Dockerfile`
Define cómo construir la imagen del servicio de rutinas.

### `ejercicios-service/Dockerfile`
Define cómo construir la imagen del servicio de ejercicios.

### `.dockerignore`
Archivos que Docker debe ignorar (venv, .git, etc.)

---

## 🎯 Comandos Más Usados (Resumen)

```cmd
# Iniciar
docker-compose up -d

# Ver estado
docker-compose ps

# Ver logs
docker-compose logs -f

# Reiniciar
docker-compose restart

# Detener
docker-compose down

# Reconstruir
docker-compose up --build -d

# Tests
docker-compose exec rutinas-service pytest -v

# Limpiar
docker-compose down -v
```

---

## ✅ Checklist Docker para Evaluación

- [x] Docker Compose configurado
- [x] 2 servicios independientes
- [x] Puertos mapeados (8001, 8002)
- [x] Volúmenes para persistencia
- [x] Red compartida entre servicios
- [x] Health checks configurados
- [x] Imágenes optimizadas con .dockerignore
- [x] Documentación completa

---

**¡Tu proyecto cumple todos los requisitos de dockerización!** 🎉
