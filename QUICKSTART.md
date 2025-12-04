# Guía de Inicio Rápido

Esta guía te ayudará a poner en marcha el proyecto en menos de 5 minutos.

## Opción 1: Usando Docker (Recomendado)

### Prerrequisitos
- [Docker Desktop](https://www.docker.com/products/docker-desktop) instalado

### Pasos

1. **Clonar o navegar al proyecto**
   ```cmd
   cd "c:\Users\sarac\Desktop\Parcial FInal Programación"
   ```

2. **Iniciar los servicios**
   ```cmd
   docker-compose up --build
   ```

3. **Verificar que estén funcionando**
   - Rutinas: http://localhost:8001/docs
   - Ejercicios: http://localhost:8002/docs

¡Listo! Ya tienes ambos microservicios corriendo.

---

## Opción 2: Sin Docker (Desarrollo Local)

### Prerrequisitos
- Python 3.11 o superior
- pip (gestor de paquetes de Python)

### Pasos

1. **Navegar al proyecto**
   ```cmd
   cd "c:\Users\sarac\Desktop\Parcial FInal Programación"
   ```

2. **Configurar servicio de Rutinas**
   ```cmd
   cd rutinas-service
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python -m uvicorn main:app --reload --port 8001
   ```

3. **En otra terminal, configurar servicio de Ejercicios**
   ```cmd
   cd "c:\Users\sarac\Desktop\Parcial FInal Programación\ejercicios-service"
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python -m uvicorn main:app --reload --port 8002
   ```

4. **Verificar**
   - Rutinas: http://localhost:8001/docs
   - Ejercicios: http://localhost:8002/docs

---

## Ejecutar Pruebas Unitarias

### Con Docker
```cmd
# Rutinas
docker-compose run rutinas-service pytest

# Ejercicios
docker-compose run ejercicios-service pytest
```

### Sin Docker
```cmd
# Rutinas
cd rutinas-service
venv\Scripts\activate
pytest

# Ejercicios
cd ..\ejercicios-service
venv\Scripts\activate
pytest
```

---

## Probar la API

### Usando la Documentación Interactiva (Swagger)

1. Abre tu navegador en:
   - http://localhost:8001/docs (Rutinas)
   - http://localhost:8002/docs (Ejercicios)

2. Prueba los endpoints directamente desde la interfaz

### Usando curl (desde CMD o PowerShell)

**Crear una rutina:**
```cmd
curl -X POST http://localhost:8001/api/rutinas -H "Content-Type: application/json" -d "{\"nombre\":\"Mi Primera Rutina\",\"descripcion\":\"Rutina de prueba\",\"duracion_estimada\":45,\"nivel\":\"Principiante\"}"
```

**Listar rutinas:**
```cmd
curl http://localhost:8001/api/rutinas
```

**Crear un ejercicio:**
```cmd
curl -X POST http://localhost:8002/api/ejercicios -H "Content-Type: application/json" -d "{\"rutina_id\":1,\"nombre\":\"Flexiones\",\"series\":3,\"repeticiones\":15,\"tiempo_descanso\":60,\"tiempo_ejecucion\":10,\"categoria\":\"Fuerza\"}"
```

**Listar ejercicios:**
```cmd
curl http://localhost:8002/api/ejercicios
```

---

## Endpoints Principales

### Microservicio de Rutinas (Puerto 8001)
- `GET /api/rutinas` - Listar todas las rutinas
- `POST /api/rutinas` - Crear nueva rutina
- `GET /api/rutinas/{id}` - Obtener rutina por ID
- `PUT /api/rutinas/{id}` - Actualizar rutina
- `DELETE /api/rutinas/{id}` - Eliminar rutina

### Microservicio de Ejercicios (Puerto 8002)
- `GET /api/ejercicios` - Listar todos los ejercicios
- `POST /api/ejercicios` - Crear nuevo ejercicio
- `GET /api/ejercicios/{id}` - Obtener ejercicio por ID
- `GET /api/ejercicios/rutina/{rutina_id}` - Ejercicios de una rutina
- `GET /api/ejercicios/rutina/{rutina_id}/tiempo-total` - Calcular tiempo total
- `PUT /api/ejercicios/{id}` - Actualizar ejercicio
- `DELETE /api/ejercicios/{id}` - Eliminar ejercicio

---

## Detener los Servicios

### Con Docker
```cmd
docker-compose down
```

### Sin Docker
Presiona `Ctrl+C` en cada terminal donde estén corriendo los servicios.

---

## Problemas Comunes

### "Puerto ya en uso"
Si ves un error diciendo que el puerto 8001 o 8002 ya está en uso:

**Windows:**
```cmd
netstat -ano | findstr :8001
taskkill /PID <número_de_proceso> /F
```

### "Módulo no encontrado"
Si Python no encuentra los módulos:
```cmd
pip install -r requirements.txt
```

### Docker no arranca
1. Asegúrate de que Docker Desktop esté ejecutándose
2. Verifica que tengas suficiente espacio en disco
3. Reinicia Docker Desktop

---

## Siguientes Pasos

1. ✅ Explora la API usando Swagger UI
2. ✅ Ejecuta las pruebas unitarias
3. ✅ Revisa el código fuente en los archivos `main.py`
4. ✅ Lee `DEPLOYMENT.md` para desplegar en la nube
5. ✅ Importa la colección de Postman (`POSTMAN_COLLECTION.md`)

---

## Recursos Adicionales

- **Documentación de FastAPI**: https://fastapi.tiangolo.com/
- **Documentación de Docker**: https://docs.docker.com/
- **Documentación de Pytest**: https://docs.pytest.org/

---

## Soporte

Si tienes problemas, revisa:
1. Que Python 3.11+ esté instalado: `python --version`
2. Que Docker esté corriendo (si usas Docker)
3. Que los puertos 8001 y 8002 estén libres
4. Los logs en la consola para mensajes de error

¡Feliz desarrollo! 🚀
