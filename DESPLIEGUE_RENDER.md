# 🚀 GUÍA DE DESPLIEGUE EN RENDER (GRATIS)

## 📋 Requisitos Previos

1. Cuenta en GitHub (gratis)
2. Cuenta en Render.com (gratis)
3. Tu código del proyecto

---

## 🔧 PASO 1: Preparar el Proyecto para Render

### ✅ Ya tienes estos archivos listos:
- ✅ `render.yaml` - Configuración de Render
- ✅ `.gitignore` - Archivos a ignorar en Git
- ✅ `requirements.txt` en cada servicio
- ✅ Código completo de ambos microservicios

---

## 📤 PASO 2: Subir Código a GitHub

### 2.1 Crear Repositorio en GitHub

1. Ve a https://github.com/new
2. **Repository name**: `fitness-api-parcial`
3. **Description**: `API REST de Fitness con Microservicios - Parcial Final`
4. Selecciona: **Public**
5. ❌ NO marques "Add a README file"
6. Click en **Create repository**

### 2.2 Subir tu Código

Abre CMD en tu carpeta del proyecto y ejecuta:

```cmd
cd "c:\Users\sarac\Desktop\Parcial FInal Programación"

git init
git add .
git commit -m "Initial commit - Fitness API con microservicios"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/fitness-api-parcial.git
git push -u origin main
```

**⚠️ Importante**: Reemplaza `TU_USUARIO` con tu nombre de usuario de GitHub.

Si te pide credenciales:
- Username: Tu usuario de GitHub
- Password: Usa un **Personal Access Token** (no tu contraseña)
  - Ve a GitHub → Settings → Developer settings → Personal access tokens → Generate new token
  - Permisos: `repo` (full control)

---

## ☁️ PASO 3: Desplegar en Render

### 3.1 Crear Cuenta en Render

1. Ve a https://render.com
2. Click en **Get Started**
3. Registrate con tu cuenta de GitHub
4. Autoriza a Render para acceder a tus repositorios

### 3.2 Conectar tu Repositorio

1. En el dashboard de Render, click en **New +**
2. Selecciona **Blueprint**
3. Click en **Connect a repository**
4. Busca y selecciona `fitness-api-parcial`
5. Click en **Connect**

### 3.3 Configurar el Blueprint

Render detectará automáticamente el archivo `render.yaml` y creará:
- ✅ **rutinas-service** (Web Service)
- ✅ **ejercicios-service** (Web Service)

1. Revisa que ambos servicios estén listados
2. Click en **Apply**
3. Espera a que los servicios se desplieguen (5-10 minutos)

---

## 🌐 PASO 4: Obtener las URLs

Una vez desplegados, verás algo como:

### 📍 URLs de tus Servicios:

**Rutinas Service:**
```
https://rutinas-service-XXXX.onrender.com
```

**Ejercicios Service:**
```
https://ejercicios-service-XXXX.onrender.com
```

### 🧪 Probar los Endpoints:

**Health Check Rutinas:**
```
https://rutinas-service-XXXX.onrender.com/health
```

**Health Check Ejercicios:**
```
https://ejercicios-service-XXXX.onrender.com/health
```

**Swagger Docs Rutinas:**
```
https://rutinas-service-XXXX.onrender.com/docs
```

**Swagger Docs Ejercicios:**
```
https://ejercicios-service-XXXX.onrender.com/docs
```

---

## 📸 PASO 5: Capturar Evidencia para tu Parcial

### Capturas Necesarias:

#### 1️⃣ Panel de Render (Dashboard)
- Muestra ambos servicios **desplegados** con estado verde
- URL visible

#### 2️⃣ Logs de Despliegue
- Click en cada servicio → Tab "Logs"
- Captura que muestra "Application startup complete"

#### 3️⃣ Health Check Funcionando
- Abre en navegador: `https://rutinas-service-XXXX.onrender.com/health`
- Abre en navegador: `https://ejercicios-service-XXXX.onrender.com/health`
- Captura la respuesta JSON

#### 4️⃣ Swagger UI en la Nube
- Abre: `https://rutinas-service-XXXX.onrender.com/docs`
- Abre: `https://ejercicios-service-XXXX.onrender.com/docs`
- Captura la interfaz de Swagger

#### 5️⃣ Repositorio GitHub
- Captura tu repositorio mostrando el código

#### 6️⃣ Test de Endpoint con Postman
- Cambia las URLs en Postman a las de Render
- Ejecuta un GET y un POST
- Captura las respuestas exitosas

---

## 🔄 PASO 6: Crear Datos de Prueba en la Nube

### Actualizar el Script para URLs de Render

Crea `crear_datos_nube.bat`:

```cmd
@echo off
echo ====================================
echo  Creando Datos de Prueba en la NUBE
echo ====================================
echo.

set RUTINAS_URL=https://rutinas-service-XXXX.onrender.com
set EJERCICIOS_URL=https://ejercicios-service-XXXX.onrender.com

echo [1/7] Creando Rutina: Fuerza Total...
curl -X POST "%RUTINAS_URL%/rutinas/" -H "Content-Type: application/json" -d "{\"nombre\":\"Fuerza Total\",\"descripcion\":\"Rutina de fuerza completa\",\"nivel\":\"Intermedio\",\"duracion_estimada\":60}"
echo.

echo [2/7] Creando Rutina: HIIT Explosivo...
curl -X POST "%RUTINAS_URL%/rutinas/" -H "Content-Type: application/json" -d "{\"nombre\":\"HIIT Explosivo\",\"descripcion\":\"Alta intensidad\",\"nivel\":\"Avanzado\",\"duracion_estimada\":30}"
echo.

echo [3/7] Creando Rutina: Principiante...
curl -X POST "%RUTINAS_URL%/rutinas/" -H "Content-Type: application/json" -d "{\"nombre\":\"Rutina Principiante\",\"descripcion\":\"Para empezar\",\"nivel\":\"Principiante\",\"duracion_estimada\":45}"
echo.

echo [4/7] Creando Ejercicio: Sentadillas (Rutina 1)...
curl -X POST "%EJERCICIOS_URL%/ejercicios/" -H "Content-Type: application/json" -d "{\"nombre\":\"Sentadillas\",\"descripcion\":\"Ejercicio de piernas\",\"categoria\":\"Fuerza\",\"series\":4,\"repeticiones\":12,\"tiempo_ejecucion\":180,\"tiempo_descanso\":90,\"rutina_id\":1}"
echo.

echo [5/7] Creando Ejercicio: Press de Banca (Rutina 1)...
curl -X POST "%EJERCICIOS_URL%/ejercicios/" -H "Content-Type: application/json" -d "{\"nombre\":\"Press de Banca\",\"descripcion\":\"Pecho\",\"categoria\":\"Fuerza\",\"series\":4,\"repeticiones\":10,\"tiempo_ejecucion\":150,\"tiempo_descanso\":90,\"rutina_id\":1}"
echo.

echo [6/7] Creando Ejercicio: Burpees (Rutina 2)...
curl -X POST "%EJERCICIOS_URL%/ejercicios/" -H "Content-Type: application/json" -d "{\"nombre\":\"Burpees\",\"descripcion\":\"Cardio intenso\",\"categoria\":\"HIIT\",\"series\":5,\"repeticiones\":15,\"tiempo_ejecucion\":120,\"tiempo_descanso\":60,\"rutina_id\":2}"
echo.

echo [7/7] Verificando Rutina 1 con tiempo total...
curl "%EJERCICIOS_URL%/ejercicios/rutina/1/tiempo-total"
echo.

echo.
echo =====================================
echo  DATOS CREADOS EN LA NUBE CON EXITO
echo =====================================
pause
```

**⚠️ Reemplaza** `XXXX` con el ID real de tus servicios de Render.

---

## 🔍 PASO 7: Verificación Final

### Checklist de Evidencia:

- [ ] Panel de Render mostrando servicios activos
- [ ] URLs públicas funcionando
- [ ] `/health` respondiendo correctamente
- [ ] `/docs` (Swagger) accesible
- [ ] Repositorio GitHub público con código
- [ ] Tests con Postman usando URLs de nube
- [ ] Datos de prueba creados en la nube
- [ ] Capturas de pantalla de todo lo anterior

---

## 🎯 URLs Importantes para tu Documentación

### Repositorio GitHub:
```
https://github.com/TU_USUARIO/fitness-api-parcial
```

### Servicios Desplegados:
```
Rutinas:    https://rutinas-service-XXXX.onrender.com
Ejercicios: https://ejercicios-service-XXXX.onrender.com
```

### Documentación API (Swagger):
```
Rutinas Docs:    https://rutinas-service-XXXX.onrender.com/docs
Ejercicios Docs: https://ejercicios-service-XXXX.onrender.com/docs
```

---

## ⚠️ Consideraciones de Render (Plan Gratuito)

### Limitaciones:
- ⏰ Los servicios se duermen después de 15 minutos de inactividad
- 🐌 Primera petición después de inactividad puede tardar 30-60 segundos
- 💾 Bases de datos SQLite se resetean al reiniciar (usa archivos persistentes)
- ⏱️ 750 horas/mes gratis (suficiente para 2 servicios)

### Solución para el "Cold Start":
En tu presentación, **abre las URLs 1-2 minutos antes** para que los servicios "despierten".

---

## 🚨 Solución de Problemas

### Problema: Build Failed
**Solución:**
1. Ve a Logs en Render
2. Verifica que `requirements.txt` exista en cada carpeta
3. Asegúrate que `render.yaml` esté en la raíz del repo

### Problema: Service Won't Start
**Solución:**
1. Revisa que el `startCommand` sea correcto
2. Verifica que el puerto use `$PORT` (variable de Render)
3. Checa los logs para ver el error específico

### Problema: 502 Bad Gateway
**Solución:**
- El servicio está iniciando (espera 1-2 minutos)
- O está dormido (haz una petición y espera 30-60 segundos)

### Problema: Base de Datos Vacía
**Solución:**
- Ejecuta `crear_datos_nube.bat` para poblar la BD
- Recuerda que en plan gratuito, la BD se resetea al reiniciar

---

## 🎓 Información para tu Presentación

### Qué Mostrar:

1. **Arquitectura Desplegada**:
   - 2 microservicios independientes en Render
   - Cada uno con su propia URL pública

2. **GitHub**:
   - Código versionado y público
   - Estructura clara del proyecto

3. **Funcionalidad en la Nube**:
   - Health checks funcionando
   - Swagger UI accesible
   - CRUD completo operando

4. **Escalabilidad**:
   - Explica que cada servicio puede escalar independientemente
   - Render permite agregar más instancias si es necesario

### Puntos Clave:

✅ **API REST funcional en la nube**
✅ **Microservicios independientes**
✅ **Documentación automática (Swagger)**
✅ **Código en control de versiones (GitHub)**
✅ **URLs públicas accesibles**
✅ **Arquitectura escalable**

---

## 📊 Diagrama de Despliegue

```
┌─────────────────────────────────────────┐
│          INTERNET                       │
└─────────────────┬───────────────────────┘
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
┌──────────────────┐  ┌──────────────────┐
│  RENDER CLOUD    │  │  RENDER CLOUD    │
│                  │  │                  │
│ rutinas-service  │  │ejercicios-service│
│ :XXXX.onrender   │  │ :YYYY.onrender   │
│                  │  │                  │
│  • FastAPI       │  │  • FastAPI       │
│  • SQLite        │  │  • SQLite        │
│  • Uvicorn       │  │  • Uvicorn       │
└──────────────────┘  └──────────────────┘
        │                   │
        └─────────┬─────────┘
                  │
                  ▼
        ┌─────────────────┐
        │  GitHub Repo    │
        │  (Source Code)  │
        └─────────────────┘
```

---

## ✅ Checklist Final

Antes de entregar tu parcial, verifica:

- [ ] Código subido a GitHub (público)
- [ ] Ambos servicios desplegados en Render
- [ ] URLs funcionando correctamente
- [ ] Health checks respondiendo
- [ ] Swagger accesible
- [ ] Datos de prueba creados en la nube
- [ ] Capturas de pantalla tomadas
- [ ] Tests en Postman con URLs de nube
- [ ] Documentación completa en README.md

---

## 🎉 ¡Listo para Entregar!

Con esto tu proyecto cumple **TODOS** los requisitos del parcial:

✅ API REST funcional
✅ 2+ Microservicios
✅ Docker (local)
✅ Despliegue en la nube
✅ Pruebas unitarias
✅ Documentación completa
✅ URLs públicas accesibles

**Puntaje esperado: 5.0** 🌟
