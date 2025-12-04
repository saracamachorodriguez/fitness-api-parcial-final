#!/bin/bash

# Script de inicio automático para el proyecto
# Sistema de Registro de Rutinas de Ejercicio

echo "=================================================="
echo "  Sistema de Registro de Rutinas de Ejercicio"
echo "=================================================="
echo ""

# Verificar si Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker no está instalado o no está en el PATH"
    echo "Por favor instala Docker Desktop desde: https://www.docker.com/products/docker-desktop"
    exit 1
fi

# Verificar si Docker está corriendo
if ! docker info &> /dev/null; then
    echo "❌ Docker no está corriendo"
    echo "Por favor inicia Docker Desktop y vuelve a ejecutar este script"
    exit 1
fi

echo "✅ Docker está instalado y corriendo"
echo ""

# Detener contenedores existentes si existen
echo "🧹 Limpiando contenedores anteriores..."
docker-compose down 2>/dev/null

echo ""
echo "🔨 Construyendo e iniciando servicios..."
echo ""

# Iniciar servicios con Docker Compose
docker-compose up --build -d

# Esperar a que los servicios estén listos
echo ""
echo "⏳ Esperando a que los servicios estén listos..."
sleep 10

# Verificar health check
echo ""
echo "🔍 Verificando estado de los servicios..."

RUTINAS_HEALTH=$(curl -s http://localhost:8001/health)
EJERCICIOS_HEALTH=$(curl -s http://localhost:8002/health)

if [ -z "$RUTINAS_HEALTH" ] || [ -z "$EJERCICIOS_HEALTH" ]; then
    echo "⚠️  Los servicios están iniciando, puede tomar unos segundos más..."
else
    echo "✅ Servicios listos!"
fi

echo ""
echo "=================================================="
echo "  ✨ Servicios Desplegados Exitosamente ✨"
echo "=================================================="
echo ""
echo "📍 Microservicio de Rutinas:"
echo "   🌐 API: http://localhost:8001"
echo "   📚 Docs: http://localhost:8001/docs"
echo "   ❤️  Health: http://localhost:8001/health"
echo ""
echo "📍 Microservicio de Ejercicios:"
echo "   🌐 API: http://localhost:8002"
echo "   📚 Docs: http://localhost:8002/docs"
echo "   ❤️  Health: http://localhost:8002/health"
echo ""
echo "=================================================="
echo ""
echo "📖 Comandos útiles:"
echo "   Ver logs:     docker-compose logs -f"
echo "   Detener:      docker-compose down"
echo "   Reiniciar:    docker-compose restart"
echo "   Ver estado:   docker-compose ps"
echo ""
echo "🧪 Ejecutar pruebas:"
echo "   cd rutinas-service && pytest"
echo "   cd ejercicios-service && pytest"
echo ""
echo "=================================================="
echo "¡Listo para usar! 🚀"
echo "=================================================="
