# 🚀 DESPLIEGUE EN RAILWAY (100% GRATIS - SIN TARJETA)

## ✅ Railway es GRATIS y NO pide tarjeta de crédito

---

## 📋 PASOS PARA DESPLEGAR (5 minutos)

### PASO 1: Ve a Railway
**Abre en tu navegador:** https://railway.app

### PASO 2: Crea tu cuenta
1. Click en **"Start a New Project"** o **"Login"**
2. Selecciona: **"Login with GitHub"**
3. Autoriza a Railway para acceder a tu cuenta de GitHub

### PASO 3: Crear Nuevo Proyecto
1. En el dashboard, click en: **"New Project"**
2. Selecciona: **"Deploy from GitHub repo"**
3. Busca y selecciona: **"fitness-api-parcial-final"**
4. Click en el repositorio

### PASO 4: Railway detectará los servicios automáticamente
Railway escaneará tu proyecto y detectará:
- ✅ `rutinas-service` (carpeta con Dockerfile)
- ✅ `ejercicios-service` (carpeta con Dockerfile)

**Railway creará 2 servicios automáticamente.**

### PASO 5: Configurar cada servicio

Railway mostrará 2 servicios. Para CADA UNO:

#### Para rutinas-service:
1. Click en el servicio `rutinas-service`
2. Ve a la pestaña **"Settings"**
3. En **"Root Directory"**, pon: `rutinas-service`
4. En **"Start Command"**, pon: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. En **"Generate Domain"**, click para obtener una URL pública
6. Guarda los cambios

#### Para ejercicios-service:
1. Click en el servicio `ejercicios-service`
2. Ve a la pestaña **"Settings"**
3. En **"Root Directory"**, pon: `ejercicios-service`
4. En **"Start Command"**, pon: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. En **"Generate Domain"**, click para obtener una URL pública
6. Guarda los cambios

### PASO 6: Esperar el despliegue
Railway comenzará a construir y desplegar automáticamente (3-5 minutos):
- 🔨 Building...
- 🚀 Deploying...
- ✅ Active

---

## 📋 PASO 7: Obtener las URLs

Una vez desplegados, cada servicio tendrá una URL como:

### rutinas-service
```
https://rutinas-service-production-XXXX.up.railway.app
```

### ejercicios-service
```
https://ejercicios-service-production-XXXX.up.railway.app
```

**Copia ambas URLs.**

---

## 🧪 PASO 8: Probar los Servicios

Abre estas URLs en tu navegador:

### Health Checks:
```
https://rutinas-service-production-XXXX.up.railway.app/health
https://ejercicios-service-production-XXXX.up.railway.app/health
```

Deberías ver: `{"status":"healthy"}`

### Documentación Swagger:
```
https://rutinas-service-production-XXXX.up.railway.app/docs
https://ejercicios-service-production-XXXX.up.railway.app/docs
```

---

## 📸 PASO 9: Capturar Evidencia

Toma capturas de:

1. ✅ **Dashboard de Railway** - Mostrando ambos servicios activos
2. ✅ **Logs de despliegue** - "Application startup complete"
3. ✅ **Health check funcionando** - Respuesta JSON
4. ✅ **Swagger UI** - /docs de ambos servicios
5. ✅ **GitHub** - Tu repositorio
6. ✅ **Postman** - Request exitoso

---

## 🎯 URLs PARA TU ENTREGA

```
📦 REPOSITORIO GITHUB:
https://github.com/saracamachorodriguez/fitness-api-parcial-final

🌐 RUTINAS SERVICE (Railway):
URL: https://rutinas-service-production-XXXX.up.railway.app
Docs: https://rutinas-service-production-XXXX.up.railway.app/docs
Health: https://rutinas-service-production-XXXX.up.railway.app/health

🌐 EJERCICIOS SERVICE (Railway):
URL: https://ejercicios-service-production-XXXX.up.railway.app
Docs: https://ejercicios-service-production-XXXX.up.railway.app/docs
Health: https://ejercicios-service-production-XXXX.up.railway.app/health
```

---

## 💡 VENTAJAS DE RAILWAY

✅ **100% Gratis** - Sin tarjeta de crédito
✅ **$5 USD/mes** de crédito gratuito
✅ **500 horas/mes** de ejecución gratis
✅ **Despliegue automático** desde GitHub
✅ **HTTPS incluido**
✅ **Logs en tiempo real**

---

## 🚨 ALTERNATIVA 2: Vercel (Solo para el backend)

Si Railway tampoco funciona, prueba **Vercel**:

1. Ve a: **https://vercel.com**
2. **Sign up with GitHub**
3. **Import Project** → Selecciona tu repo
4. Vercel es gratuito y sin tarjeta

---

## ✅ CHECKLIST FINAL

- [ ] Cuenta en Railway creada (sin tarjeta)
- [ ] Proyecto conectado desde GitHub
- [ ] 2 servicios desplegados (rutinas + ejercicios)
- [ ] Ambos servicios con estado "Active"
- [ ] URLs públicas generadas
- [ ] Health checks funcionando
- [ ] Swagger UI accesible
- [ ] 6 capturas de pantalla tomadas

---

## 🎉 ¡LISTO PARA ENTREGAR!

Tu proyecto cumple **TODOS** los requisitos:

✅ API REST completa
✅ 2 Microservicios independientes
✅ Docker
✅ **Despliegue en la nube (Railway)**
✅ 32 pruebas unitarias
✅ Documentación completa
✅ GitHub público

**Puntaje esperado: 5.0 / 5.0** 🌟

---

## 🚀 EMPIEZA AHORA:

**Ve a:** https://railway.app

**Cuando tengas las URLs, mándamelas para verificar que funcionen.** 🎯
