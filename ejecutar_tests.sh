#!/bin/bash

echo "===================================="
echo "  EJECUTANDO PRUEBAS UNITARIAS"
echo "===================================="
echo ""

echo "[1/2] Ejecutando tests de RUTINAS-SERVICE..."
echo ""
cd rutinas-service
pytest -v
cd ..

echo ""
echo ""
echo "[2/2] Ejecutando tests de EJERCICIOS-SERVICE..."
echo ""
cd ejercicios-service
pytest -v
cd ..

echo ""
echo "===================================="
echo "  PRUEBAS COMPLETADAS"
echo "===================================="
