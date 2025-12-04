# 🚀 INSTRUCCIONES FINALES PARA DESPLEGAR EN RENDER

## ✅ TODO LISTO EN GITHUB:
- Repositorio: https://github.com/saracamachorodriguez/fitness-api-parcial-final
- Código actualizado con tests sin warnings
- 32 tests pasando (14 rutinas + 18 ejercicios)

---

## 🌐 AHORA: Despliega en Render (10 minutos)

### PASO 1: Ve a Render
**Abre en tu navegador:** https://render.com

### PASO 2: Crea tu cuenta
1. Click en **"Get Started for Free"**
2. Selecciona: **"Sign up with GitHub"** (botón morado con logo de GitHub)
3. Autoriza a Render para acceder a tu cuenta

### PASO 3: Conecta tu repositorio
1. En el dashboard de Render, click en: **"New +"** (arriba a la derecha)
2. Selecciona: **"Blueprint"**
3. Si te pide conectar un repo, click en **"Connect a repository"**
4. Busca: **"fitness-api-parcial-final"**
5. Click en **"Connect"**

### PASO 4: Aplicar el Blueprint
Render detectará automáticamente el archivo `render.yaml` y mostrará:

```
📦 Services to create:
✅ rutinas-service (Web Service)
✅ ejercicios-service (Web Service)
```

**Click en: "Apply"** (botón azul grande)

### PASO 5: Esperar el despliegue (5-10 minutos)
Verás los logs en tiempo real:
- 🔨 Building... (instalando dependencias)
- 🚀 Deploying... (iniciando servicios)
- ✅ Live (servicios activos)

**Espera a que ambos servicios muestren estado "Live" en verde.**

---

## 📋 PASO 6: Obtener tus URLs

Una vez desplegados, verás algo como:

### rutinas-service
```
https://rutinas-service-XXXX.onrender.com
```

### ejercicios-service
```
https://ejercicios-service-XXXX.onrender.com
```

---

## 🧪 PASO 7: Probar los Servicios

Abre estas URLs en tu navegador (reemplaza XXXX con tu ID):

### Health Checks:
```
https://rutinas-service-XXXX.onrender.com/health
https://ejercicios-service-XXXX.onrender.com/health
```

Deberías ver: `{"status":"healthy"}`

### Documentación Swagger:
```
https://rutinas-service-XXXX.onrender.com/docs
https://ejercicios-service-XXXX.onrender.com/docs
```

Verás la interfaz interactiva de Swagger con todos los endpoints.

---

## 📸 PASO 8: Capturar Evidencia

Toma capturas de pantalla de:

1. ✅ **Dashboard de Render** - Mostrando ambos servicios "Live"
2. ✅ **Logs de despliegue** - "Application startup complete"
3. ✅ **Health check funcionando** - Respuesta JSON en navegador
4. ✅ **Swagger UI** - Interfaz /docs de ambos servicios
5. ✅ **GitHub** - Tu repositorio con el código
6. ✅ **Postman** - Request exitoso a las URLs de la nube

---

## 🎯 URLS PARA TU ENTREGA

Anota estas URLs para tu documentación:

```
📦 REPOSITORIO:
https://github.com/saracamachorodriguez/fitness-api-parcial-final

🌐 RUTINAS SERVICE:
URL: https://rutinas-service-XXXX.onrender.com
Docs: https://rutinas-service-XXXX.onrender.com/docs
Health: https://rutinas-service-XXXX.onrender.com/health

🌐 EJERCICIOS SERVICE:
URL: https://ejercicios-service-XXXX.onrender.com
Docs: https://ejercicios-service-XXXX.onrender.com/docs
Health: https://ejercicios-service-XXXX.onrender.com/health
```

---

## ⚠️ IMPORTANTE: Cold Start

Los servicios gratuitos de Render se duermen después de 15 minutos de inactividad.

**Para tu presentación:**
- Abre las URLs 2-3 minutos antes de presentar
- La primera petición puede tardar 30-60 segundos (cold start)
- Después funcionan normal

---

## ✅ CHECKLIST FINAL

- [ ] Cuenta en Render creada
- [ ] Blueprint conectado al repositorio
- [ ] Ambos servicios desplegados (estado "Live")
- [ ] Health checks funcionando
- [ ] Swagger UI accesible
- [ ] 6 capturas de pantalla tomadas
- [ ] URLs anotadas para la entrega

---

## 🎉 ¡LISTO PARA ENTREGAR!

Tu proyecto cumple **TODOS** los requisitos:

✅ API REST completa (14 endpoints)
✅ 2 Microservicios independientes
✅ Docker (docker-compose.yml)
✅ **Despliegue en la nube** ← ESTE PASO
✅ 32 pruebas unitarias (sin warnings)
✅ Documentación completa (10 archivos .md)
✅ GitHub público con código

**Puntaje esperado: 5.0 / 5.0** 🌟

---

**EMPIEZA AHORA EN:** https://render.com

**Cuando tengas las URLs, mándamelas para verificar que todo funcione correctamente.** 🚀
