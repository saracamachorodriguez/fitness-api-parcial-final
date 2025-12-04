# 🚀 PASOS PARA DESPLEGAR EN RENDER

## ✅ COMPLETADO:
- ✅ Código en GitHub: https://github.com/saracamachorodriguez/fitness-api-parcial-final

---

## 🌐 AHORA: Desplegar en Render (5 minutos)

### PASO 1: Crear Cuenta en Render

1. **Abre tu navegador** y ve a: **https://render.com**

2. Click en: **"Get Started for Free"**

3. Selecciona: **"Sign up with GitHub"** (botón morado)

4. **Autoriza a Render** para acceder a tus repositorios

5. En la página de autorización de GitHub:
   - Marca: ✅ `saracamachorodriguez/fitness-api-parcial-final`
   - Click: **"Authorize Render"**

---

### PASO 2: Crear Blueprint desde tu Repositorio

1. En el **Dashboard de Render**, click en: **"New +"** (botón azul arriba a la derecha)

2. Selecciona: **"Blueprint"**

3. Click en: **"Connect a repository"**

4. Busca y selecciona: **`fitness-api-parcial-final`**

5. Click en: **"Connect"**

6. Render detectará automáticamente el archivo `render.yaml` y mostrará:
   ```
   📦 Services to create:
   ✅ rutinas-service (Web Service)
   ✅ ejercicios-service (Web Service)
   ```

7. Click en: **"Apply"** (botón azul)

---

### PASO 3: Esperar el Despliegue (5-10 minutos)

Render comenzará a:
1. 🔨 **Build** - Instalar dependencias
2. 🚀 **Deploy** - Lanzar los servicios
3. ✅ **Live** - Servicios activos

Verás los logs en tiempo real. Espera a que ambos servicios muestren:
- Estado: **"Live"** (verde)
- Health check: ✅

---

### PASO 4: Obtener las URLs de tus Servicios

Una vez desplegados:

1. **Click en** `rutinas-service`
2. **Copia la URL** (algo como: `https://rutinas-service-xxxx.onrender.com`)

3. **Click en** `ejercicios-service`
4. **Copia la URL** (algo como: `https://ejercicios-service-xxxx.onrender.com`)

---

### PASO 5: Probar los Servicios en la Nube

Abre estas URLs en tu navegador (reemplaza `xxxx` con tu ID real):

**Health Checks:**
```
https://rutinas-service-xxxx.onrender.com/health
https://ejercicios-service-xxxx.onrender.com/health
```

**Documentación Swagger:**
```
https://rutinas-service-xxxx.onrender.com/docs
https://ejercicios-service-xxxx.onrender.com/docs
```

---

## 📸 EVIDENCIA PARA TU PARCIAL

### Capturas que necesitas tomar:

#### 1. Dashboard de Render
- Captura mostrando ambos servicios con estado **"Live"** (verde)
- URLs visibles

#### 2. Logs de Despliegue
- Click en cada servicio → Tab **"Logs"**
- Captura mostrando: `Application startup complete`

#### 3. Health Check Funcionando
- Captura del navegador mostrando:
  ```json
  {"status":"healthy"}
  ```
  Para ambos servicios

#### 4. Swagger UI en la Nube
- Captura de `/docs` mostrando todos los endpoints
- Para ambos servicios

#### 5. Repositorio GitHub
- Captura de: https://github.com/saracamachorodriguez/fitness-api-parcial-final

#### 6. Test con Postman
- Importa tu colección de Postman
- Cambia las URLs a las de Render
- Ejecuta algunos requests
- Captura las respuestas exitosas

---

## 🎯 CHECKLIST FINAL

- [ ] Cuenta en Render creada
- [ ] Blueprint aplicado
- [ ] Ambos servicios desplegados (estado "Live")
- [ ] `/health` funcionando en ambos servicios
- [ ] `/docs` accesible en ambos servicios
- [ ] 6 capturas de pantalla tomadas
- [ ] URLs documentadas para entregar

---

## 📝 URLs para tu Entrega Final

Cuando termines, anota estas URLs:

```
📦 REPOSITORIO GITHUB:
https://github.com/saracamachorodriguez/fitness-api-parcial-final

🌐 SERVICIO RUTINAS:
URL: https://rutinas-service-xxxx.onrender.com
Docs: https://rutinas-service-xxxx.onrender.com/docs
Health: https://rutinas-service-xxxx.onrender.com/health

🌐 SERVICIO EJERCICIOS:
URL: https://ejercicios-service-xxxx.onrender.com
Docs: https://ejercicios-service-xxxx.onrender.com/docs
Health: https://ejercicios-service-xxxx.onrender.com/health
```

---

## ⚠️ NOTA IMPORTANTE

**Los servicios gratuitos de Render se duermen después de 15 minutos de inactividad.**

Para tu presentación/evaluación:
- Abre las URLs **2-3 minutos antes**
- La primera petición puede tardar 30-60 segundos (cold start)
- Después funcionan normalmente

---

## 🎉 ¡EMPIEZA AHORA!

**Ve a:** https://render.com

Cuando termines el despliegue, **mándame las URLs** y verifico que todo esté funcionando correctamente.

---

## 🚨 ¿Problemas?

Si algo falla:
1. Revisa los **Logs** en Render
2. Verifica que `render.yaml` esté en la raíz del repo
3. Confirma que ambas carpetas `rutinas-service` y `ejercicios-service` tengan `requirements.txt`

**¡Avísame cuando tengas las URLs!** 🚀
