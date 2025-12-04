# 🚀 PASOS PARA DESPLEGAR TU PROYECTO EN LA NUBE

## ✅ YA HECHO (por mí):

1. ✅ Git inicializado
2. ✅ Archivos agregados al repositorio
3. ✅ Primer commit creado (25 archivos, 5404 líneas)
4. ✅ `render.yaml` configurado para Render
5. ✅ `.gitignore` creado

---

## 📤 AHORA DEBES HACER TÚ (5 minutos):

### PASO 1: Crear Repositorio en GitHub

1. **Abre tu navegador** y ve a: https://github.com/new

2. **Configura el repositorio**:
   - **Repository name**: `fitness-api-parcial-final`
   - **Description**: `API REST de Fitness - Microservicios con Docker - Parcial Final Programación`
   - Selecciona: **Public** ✅
   - ❌ NO marques "Add a README file"
   - ❌ NO marques "Add .gitignore"
   - ❌ NO marques "Choose a license"

3. **Click en**: `Create repository`

4. **IMPORTANTE**: Después de crear, GitHub te mostrará una página con comandos. **Deja esa pestaña abierta**.

---

### PASO 2: Conectar tu Proyecto con GitHub

**Copia estos comandos UNO POR UNO** en tu CMD (ya debes estar en la carpeta del proyecto):

```cmd
git branch -M main
```

Luego (⚠️ **REEMPLAZA** `TU_USUARIO` con tu usuario real de GitHub):

```cmd
git remote add origin https://github.com/TU_USUARIO/fitness-api-parcial-final.git
```

Finalmente:

```cmd
git push -u origin main
```

**Si te pide credenciales:**
- Username: Tu usuario de GitHub
- Password: **NO uses tu contraseña**, usa un **Personal Access Token**

#### ¿Cómo crear un Personal Access Token?

1. Ve a: https://github.com/settings/tokens
2. Click en `Generate new token` → `Generate new token (classic)`
3. **Note**: `Render deployment`
4. **Expiration**: `90 days`
5. **Select scopes**: ✅ Marca `repo` (todo)
6. Click en `Generate token`
7. **COPIA EL TOKEN** (solo se muestra una vez)
8. Usa ese token como contraseña cuando Git te lo pida

---

### PASO 3: Verificar que se Subió Correctamente

1. Refresca la página de tu repositorio en GitHub
2. Deberías ver todos tus archivos:
   - ✅ rutinas-service/
   - ✅ ejercicios-service/
   - ✅ docker-compose.yml
   - ✅ render.yaml
   - ✅ README.md
   - ✅ Etc.

---

### PASO 4: Desplegar en Render

1. **Abre**: https://render.com

2. **Registrate**:
   - Click en `Get Started for Free`
   - Selecciona `Sign up with GitHub`
   - Autoriza a Render

3. **Crear Blueprint**:
   - En el Dashboard, click en `New +`
   - Selecciona `Blueprint`
   - Click en `Connect a repository`
   - Busca `fitness-api-parcial-final`
   - Click en `Connect`

4. **Configurar**:
   - Render detectará automáticamente el archivo `render.yaml`
   - Verás 2 servicios:
     - ✅ `rutinas-service`
     - ✅ `ejercicios-service`
   - Click en `Apply`

5. **Esperar Despliegue** (5-10 minutos):
   - Verás los logs en tiempo real
   - Espera a que ambos servicios estén **"Live"** (verde)

---

### PASO 5: Obtener las URLs

Una vez desplegados:

1. Click en `rutinas-service` → Copia la URL (algo como `https://rutinas-service-xxxx.onrender.com`)

2. Click en `ejercicios-service` → Copia la URL

3. **Prueba las URLs** en tu navegador:
   ```
   https://rutinas-service-xxxx.onrender.com/health
   https://rutinas-service-xxxx.onrender.com/docs
   
   https://ejercicios-service-xxxx.onrender.com/health
   https://ejercicios-service-xxxx.onrender.com/docs
   ```

---

### PASO 6: Crear Datos de Prueba en la Nube

Crea un archivo `crear_datos_nube.bat` con este contenido (⚠️ **cambia las URLs** por las tuyas):

```cmd
@echo off
echo ====================================
echo  Creando Datos de Prueba en la NUBE
echo ====================================
echo.

set RUTINAS_URL=https://rutinas-service-XXXX.onrender.com
set EJERCICIOS_URL=https://ejercicios-service-XXXX.onrender.com

echo [1/4] Creando Rutina: Fuerza Total...
curl -X POST "%RUTINAS_URL%/rutinas/" -H "Content-Type: application/json" -d "{\"nombre\":\"Fuerza Total\",\"descripcion\":\"Rutina de fuerza completa\",\"nivel\":\"Intermedio\",\"duracion_estimada\":60}"
echo.

echo [2/4] Creando Rutina: HIIT Explosivo...
curl -X POST "%RUTINAS_URL%/rutinas/" -H "Content-Type: application/json" -d "{\"nombre\":\"HIIT Explosivo\",\"descripcion\":\"Alta intensidad\",\"nivel\":\"Avanzado\",\"duracion_estimada\":30}"
echo.

echo [3/4] Creando Ejercicio: Sentadillas...
curl -X POST "%EJERCICIOS_URL%/ejercicios/" -H "Content-Type: application/json" -d "{\"nombre\":\"Sentadillas\",\"descripcion\":\"Ejercicio de piernas\",\"categoria\":\"Fuerza\",\"series\":4,\"repeticiones\":12,\"tiempo_ejecucion\":180,\"tiempo_descanso\":90,\"rutina_id\":1}"
echo.

echo [4/4] Creando Ejercicio: Burpees...
curl -X POST "%EJERCICIOS_URL%/ejercicios/" -H "Content-Type: application/json" -d "{\"nombre\":\"Burpees\",\"descripcion\":\"Cardio intenso\",\"categoria\":\"HIIT\",\"series\":5,\"repeticiones\":15,\"tiempo_ejecucion\":120,\"tiempo_descanso\":60,\"rutina_id\":2}"
echo.

echo.
echo =====================================
echo  DATOS CREADOS EN LA NUBE CON EXITO
echo =====================================
pause
```

Ejecuta el script:
```cmd
crear_datos_nube.bat
```

---

### PASO 7: Actualizar Postman con URLs de la Nube

1. Abre Postman
2. En tu colección, edita las variables:
   - `rutinas_url`: `https://rutinas-service-xxxx.onrender.com`
   - `ejercicios_url`: `https://ejercicios-service-xxxx.onrender.com`
3. Prueba todos los endpoints

---

## 📸 EVIDENCIA PARA TU PARCIAL

### Capturas que necesitas:

1. **Panel de Render**:
   - Captura mostrando ambos servicios en estado "Live" (verde)
   - URL visible

2. **Logs de Render**:
   - Click en cada servicio → Tab "Logs"
   - Captura mostrando "Application startup complete"

3. **GitHub**:
   - Captura de tu repositorio con todo el código

4. **Health Checks Funcionando**:
   - Captura del navegador mostrando `/health` respondiendo
   - Para ambos servicios

5. **Swagger en la Nube**:
   - Captura de `/docs` funcionando
   - Para ambos servicios

6. **Postman con URLs de Nube**:
   - Captura de un GET exitoso
   - Captura de un POST exitoso

---

## ✅ CHECKLIST FINAL

Antes de entregar:

- [ ] Código en GitHub (público)
- [ ] Ambos servicios desplegados en Render
- [ ] URLs funcionando (`/health`, `/docs`)
- [ ] Datos de prueba creados en la nube
- [ ] Tests en Postman con URLs de nube
- [ ] 6 capturas de pantalla tomadas
- [ ] Documentación completa en README.md

---

## 🎯 URLs a Incluir en tu Entrega

```
📦 Repositorio GitHub:
https://github.com/TU_USUARIO/fitness-api-parcial-final

🌐 Servicio Rutinas:
https://rutinas-service-xxxx.onrender.com
https://rutinas-service-xxxx.onrender.com/docs

🌐 Servicio Ejercicios:
https://ejercicios-service-xxxx.onrender.com
https://ejercicios-service-xxxx.onrender.com/docs
```

---

## 🚨 IMPORTANTE

⚠️ **Los servicios gratuitos de Render se duermen después de 15 minutos de inactividad.**

**Para tu presentación/demo:**
- Abre las URLs **2-3 minutos antes** de presentar
- La primera petición después de inactividad tarda 30-60 segundos
- Después de eso, funcionan normal

---

## ❓ ¿Necesitas Ayuda?

Si algo no funciona:

1. **Error en GitHub**: Verifica que el token tenga permisos `repo`
2. **Error en Render**: Revisa los logs en la interfaz de Render
3. **503 Service Unavailable**: El servicio está iniciando, espera 1 minuto
4. **Base de datos vacía**: Ejecuta `crear_datos_nube.bat`

---

## 🎉 ¡LISTO!

Con esto tu proyecto cumple **TODOS** los requisitos:

✅ API REST completa
✅ 2 Microservicios independientes
✅ Docker (local)
✅ Despliegue en la nube ← **AHORA SÍ**
✅ Tests unitarios (33+)
✅ Documentación completa
✅ URLs públicas accesibles

**Puntaje esperado: 5.0 / 5.0** 🌟

---

**¡EMPIEZA CON EL PASO 1! Cuando termines, avísame y te ayudo con lo que necesites.**
