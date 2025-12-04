# Guía de Despliegue en la Nube

Este documento detalla los pasos para desplegar el sistema de registro de rutinas de ejercicio en diferentes plataformas cloud.

## Tabla de Contenidos
1. [Despliegue en Render](#despliegue-en-render)
2. [Despliegue en Railway](#despliegue-en-railway)
3. [Despliegue en Azure](#despliegue-en-azure)
4. [Despliegue en AWS](#despliegue-en-aws)
5. [Verificación del Despliegue](#verificación-del-despliegue)

---

## Despliegue en Render

### Opción 1: Despliegue usando Docker (Recomendado)

1. **Preparar el repositorio**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/tu-usuario/tu-repo.git
   git push -u origin main
   ```

2. **Crear cuenta en Render**
   - Ir a https://render.com
   - Registrarse con GitHub

3. **Crear Web Service para Rutinas**
   - Click en "New +" → "Web Service"
   - Conectar con tu repositorio
   - Configuración:
     - **Name**: `rutinas-service`
     - **Region**: Oregon (US West) o la más cercana
     - **Root Directory**: `rutinas-service`
     - **Environment**: `Docker`
     - **Plan**: Free
     - **Docker Command**: (dejar vacío, usa el CMD del Dockerfile)

4. **Crear Web Service para Ejercicios**
   - Repetir el proceso anterior con:
     - **Name**: `ejercicios-service`
     - **Root Directory**: `ejercicios-service`

5. **Variables de entorno** (opcional)
   - En cada servicio, ir a "Environment"
   - Agregar: `DB_PATH=/data/database.db`

6. **Acceder a las URLs**
   - Render asignará URLs como:
     - `https://rutinas-service.onrender.com`
     - `https://ejercicios-service.onrender.com`

### Opción 2: Despliegue sin Docker

1. **Configuración del servicio de Rutinas**
   - **Environment**: `Python 3.11`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

2. **Configuración del servicio de Ejercicios**
   - Misma configuración que Rutinas

### Notas sobre Render
- ⚠️ El plan gratuito hiberna los servicios después de 15 minutos de inactividad
- ⚠️ La primera solicitud después de hibernar puede tardar 30-50 segundos
- ✅ SSL/HTTPS incluido automáticamente
- ✅ Deploys automáticos desde GitHub

---

## Despliegue en Railway

### Configuración Rápida

1. **Crear cuenta en Railway**
   - Ir a https://railway.app
   - Registrarse con GitHub

2. **Crear nuevo proyecto**
   - Click en "New Project"
   - Seleccionar "Deploy from GitHub repo"
   - Elegir tu repositorio

3. **Configurar Servicio de Rutinas**
   - Railway detectará automáticamente Python
   - Configurar:
     - **Root Directory**: `rutinas-service`
     - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

4. **Configurar Servicio de Ejercicios**
   - Click en "+ New Service"
   - Seleccionar el mismo repositorio
   - Configurar:
     - **Root Directory**: `ejercicios-service`
     - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

5. **Generar dominios públicos**
   - En cada servicio: Settings → Generate Domain

6. **URLs resultantes**
   - `https://rutinas-service-production.up.railway.app`
   - `https://ejercicios-service-production.up.railway.app`

### Ventajas de Railway
- ✅ No hiberna servicios (plan gratuito con $5 de crédito/mes)
- ✅ Deploys más rápidos
- ✅ Mejor para desarrollo

---

## Despliegue en Azure

### Opción 1: Azure Container Instances (Más Simple)

1. **Instalar Azure CLI**
   ```bash
   # Windows (PowerShell)
   winget install Microsoft.AzureCLI
   
   # Verificar instalación
   az --version
   ```

2. **Iniciar sesión**
   ```bash
   az login
   ```

3. **Crear grupo de recursos**
   ```bash
   az group create --name fitness-app-rg --location eastus
   ```

4. **Crear Azure Container Registry (ACR)**
   ```bash
   az acr create --resource-group fitness-app-rg --name fitnessappregistry --sku Basic
   az acr login --name fitnessappregistry
   ```

5. **Construir y subir imágenes Docker**
   ```bash
   # Rutinas
   cd rutinas-service
   docker build -t fitnessappregistry.azurecr.io/rutinas-service:latest .
   docker push fitnessappregistry.azurecr.io/rutinas-service:latest
   
   # Ejercicios
   cd ../ejercicios-service
   docker build -t fitnessappregistry.azurecr.io/ejercicios-service:latest .
   docker push fitnessappregistry.azurecr.io/ejercicios-service:latest
   ```

6. **Desplegar contenedores**
   ```bash
   # Obtener credenciales del ACR
   $ACR_USERNAME = az acr credential show --name fitnessappregistry --query username -o tsv
   $ACR_PASSWORD = az acr credential show --name fitnessappregistry --query "passwords[0].value" -o tsv
   
   # Desplegar servicio de rutinas
   az container create --resource-group fitness-app-rg --name rutinas-service --image fitnessappregistry.azurecr.io/rutinas-service:latest --dns-name-label rutinas-fitness --ports 8001 --registry-login-server fitnessappregistry.azurecr.io --registry-username $ACR_USERNAME --registry-password $ACR_PASSWORD
   
   # Desplegar servicio de ejercicios
   az container create --resource-group fitness-app-rg --name ejercicios-service --image fitnessappregistry.azurecr.io/ejercicios-service:latest --dns-name-label ejercicios-fitness --ports 8002 --registry-login-server fitnessappregistry.azurecr.io --registry-username $ACR_USERNAME --registry-password $ACR_PASSWORD
   ```

7. **Obtener URLs**
   ```bash
   az container show --resource-group fitness-app-rg --name rutinas-service --query ipAddress.fqdn
   az container show --resource-group fitness-app-rg --name ejercicios-service --query ipAddress.fqdn
   ```

### Opción 2: Azure App Service

1. **Crear App Service Plans**
   ```bash
   az appservice plan create --name fitness-app-plan --resource-group fitness-app-rg --sku F1 --is-linux
   ```

2. **Crear Web Apps**
   ```bash
   az webapp create --resource-group fitness-app-rg --plan fitness-app-plan --name rutinas-fitness-app --deployment-container-image-name fitnessappregistry.azurecr.io/rutinas-service:latest
   
   az webapp create --resource-group fitness-app-rg --plan fitness-app-plan --name ejercicios-fitness-app --deployment-container-image-name fitnessappregistry.azurecr.io/ejercicios-service:latest
   ```

3. **Configurar credenciales del registro**
   ```bash
   az webapp config container set --name rutinas-fitness-app --resource-group fitness-app-rg --docker-registry-server-url https://fitnessappregistry.azurecr.io --docker-registry-server-user $ACR_USERNAME --docker-registry-server-password $ACR_PASSWORD
   ```

---

## Despliegue en AWS

### Usando AWS Elastic Container Service (ECS)

1. **Instalar AWS CLI**
   ```bash
   # Windows (PowerShell)
   winget install Amazon.AWSCLI
   
   # Configurar
   aws configure
   ```

2. **Crear repositorio ECR**
   ```bash
   aws ecr create-repository --repository-name rutinas-service
   aws ecr create-repository --repository-name ejercicios-service
   ```

3. **Autenticar Docker con ECR**
   ```bash
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <tu-account-id>.dkr.ecr.us-east-1.amazonaws.com
   ```

4. **Construir y subir imágenes**
   ```bash
   # Rutinas
   docker build -t rutinas-service ./rutinas-service
   docker tag rutinas-service:latest <tu-account-id>.dkr.ecr.us-east-1.amazonaws.com/rutinas-service:latest
   docker push <tu-account-id>.dkr.ecr.us-east-1.amazonaws.com/rutinas-service:latest
   
   # Ejercicios
   docker build -t ejercicios-service ./ejercicios-service
   docker tag ejercicios-service:latest <tu-account-id>.dkr.ecr.us-east-1.amazonaws.com/ejercicios-service:latest
   docker push <tu-account-id>.dkr.ecr.us-east-1.amazonaws.com/ejercicios-service:latest
   ```

5. **Crear cluster ECS**
   ```bash
   aws ecs create-cluster --cluster-name fitness-app-cluster
   ```

6. **Crear task definitions y services**
   - Usar la consola de AWS o archivos JSON de configuración
   - Configurar load balancers para acceso público

---

## Verificación del Despliegue

### 1. Health Checks

Verificar que ambos servicios estén funcionando:

```bash
# Rutinas
curl https://tu-url-rutinas/health

# Ejercicios
curl https://tu-url-ejercicios/health
```

Respuesta esperada:
```json
{
  "status": "healthy",
  "service": "rutinas-service" / "ejercicios-service",
  "timestamp": "2025-12-04T..."
}
```

### 2. Documentación Interactiva

Acceder a la documentación Swagger:
- `https://tu-url-rutinas/docs`
- `https://tu-url-ejercicios/docs`

### 3. Pruebas Funcionales

**Crear una rutina:**
```bash
curl -X POST https://tu-url-rutinas/api/rutinas \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Rutina de Prueba",
    "descripcion": "Test de despliegue",
    "duracion_estimada": 45,
    "nivel": "Intermedio"
  }'
```

**Crear un ejercicio:**
```bash
curl -X POST https://tu-url-ejercicios/api/ejercicios \
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

**Listar rutinas:**
```bash
curl https://tu-url-rutinas/api/rutinas
```

### 4. Monitoreo

**Render:**
- Ver logs en tiempo real desde el dashboard
- Métricas de CPU y memoria disponibles

**Railway:**
- Logs integrados en el dashboard
- Métricas de uso de recursos

**Azure:**
```bash
az container logs --resource-group fitness-app-rg --name rutinas-service
az container logs --resource-group fitness-app-rg --name ejercicios-service
```

---

## Resolución de Problemas

### Servicio no responde
1. Verificar que el puerto esté correctamente configurado
2. Revisar logs del contenedor
3. Confirmar que la variable `PORT` esté disponible

### Error de base de datos
1. Verificar permisos de escritura en el directorio
2. Considerar usar PostgreSQL o MongoDB para producción
3. Verificar que la ruta `DB_PATH` sea válida

### Timeouts
1. Aumentar el timeout en el balanceador de carga
2. Verificar recursos del contenedor (RAM, CPU)
3. Considerar upgrade del plan si es necesario

---

## Recomendaciones de Producción

1. **Base de datos**: Migrar de SQLite a PostgreSQL/MySQL
2. **Autenticación**: Implementar JWT o OAuth2
3. **Rate Limiting**: Agregar límites de peticiones
4. **Logging**: Integrar con servicios de logging centralizados
5. **Monitoreo**: Configurar alertas y métricas
6. **Backup**: Implementar estrategia de respaldo de datos
7. **CI/CD**: Configurar pipeline de integración continua
8. **HTTPS**: Asegurar que todos los endpoints usen SSL/TLS
9. **CORS**: Configurar políticas CORS apropiadas
10. **Documentación**: Mantener docs actualizadas

---

## Costos Estimados

| Plataforma | Plan Gratuito | Plan Básico |
|------------|---------------|-------------|
| Render | ✅ Gratis (con limitaciones) | $7/mes por servicio |
| Railway | $5 crédito/mes | $10/mes |
| Azure | $200 crédito inicial | ~$20-30/mes |
| AWS | 12 meses gratis | ~$20-40/mes |

---

## URLs de Documentación

- **Render**: https://render.com/docs
- **Railway**: https://docs.railway.app
- **Azure**: https://docs.microsoft.com/azure
- **AWS**: https://docs.aws.amazon.com

---

## Soporte

Para problemas específicos del proyecto, contactar al autor o abrir un issue en GitHub.
