# Colección de Postman - Sistema de Rutinas de Ejercicio

## Importar en Postman

1. Abre Postman
2. Click en "Import"
3. Copia y pega este archivo JSON completo

```json
{
  "info": {
    "name": "Sistema de Rutinas de Ejercicio",
    "description": "API REST para gestionar rutinas, ejercicios y tiempos de entrenamiento",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "variable": [
    {
      "key": "rutinas_url",
      "value": "http://localhost:8001",
      "type": "string"
    },
    {
      "key": "ejercicios_url",
      "value": "http://localhost:8002",
      "type": "string"
    }
  ],
  "item": [
    {
      "name": "Microservicio Rutinas",
      "item": [
        {
          "name": "Health Check - Rutinas",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{rutinas_url}}/health",
              "host": ["{{rutinas_url}}"],
              "path": ["health"]
            }
          }
        },
        {
          "name": "Listar Todas las Rutinas",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{rutinas_url}}/api/rutinas",
              "host": ["{{rutinas_url}}"],
              "path": ["api", "rutinas"]
            }
          }
        },
        {
          "name": "Obtener Rutina por ID",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{rutinas_url}}/api/rutinas/1",
              "host": ["{{rutinas_url}}"],
              "path": ["api", "rutinas", "1"]
            }
          }
        },
        {
          "name": "Crear Rutina - Fuerza",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"nombre\": \"Rutina de Fuerza\",\n  \"descripcion\": \"Entrenamiento enfocado en ganar fuerza muscular\",\n  \"duracion_estimada\": 60,\n  \"nivel\": \"Intermedio\"\n}"
            },
            "url": {
              "raw": "{{rutinas_url}}/api/rutinas",
              "host": ["{{rutinas_url}}"],
              "path": ["api", "rutinas"]
            }
          }
        },
        {
          "name": "Crear Rutina - Cardio",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"nombre\": \"Rutina de Cardio HIIT\",\n  \"descripcion\": \"Entrenamiento de alta intensidad por intervalos\",\n  \"duracion_estimada\": 30,\n  \"nivel\": \"Avanzado\"\n}"
            },
            "url": {
              "raw": "{{rutinas_url}}/api/rutinas",
              "host": ["{{rutinas_url}}"],
              "path": ["api", "rutinas"]
            }
          }
        },
        {
          "name": "Actualizar Rutina",
          "request": {
            "method": "PUT",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"duracion_estimada\": 75,\n  \"descripcion\": \"Entrenamiento completo de fuerza con énfasis en pesas\"\n}"
            },
            "url": {
              "raw": "{{rutinas_url}}/api/rutinas/1",
              "host": ["{{rutinas_url}}"],
              "path": ["api", "rutinas", "1"]
            }
          }
        },
        {
          "name": "Eliminar Rutina",
          "request": {
            "method": "DELETE",
            "header": [],
            "url": {
              "raw": "{{rutinas_url}}/api/rutinas/1",
              "host": ["{{rutinas_url}}"],
              "path": ["api", "rutinas", "1"]
            }
          }
        }
      ]
    },
    {
      "name": "Microservicio Ejercicios",
      "item": [
        {
          "name": "Health Check - Ejercicios",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{ejercicios_url}}/health",
              "host": ["{{ejercicios_url}}"],
              "path": ["health"]
            }
          }
        },
        {
          "name": "Listar Todos los Ejercicios",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{ejercicios_url}}/api/ejercicios",
              "host": ["{{ejercicios_url}}"],
              "path": ["api", "ejercicios"]
            }
          }
        },
        {
          "name": "Listar Ejercicios por Categoría",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{ejercicios_url}}/api/ejercicios?categoria=Fuerza",
              "host": ["{{ejercicios_url}}"],
              "path": ["api", "ejercicios"],
              "query": [
                {
                  "key": "categoria",
                  "value": "Fuerza"
                }
              ]
            }
          }
        },
        {
          "name": "Obtener Ejercicio por ID",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{ejercicios_url}}/api/ejercicios/1",
              "host": ["{{ejercicios_url}}"],
              "path": ["api", "ejercicios", "1"]
            }
          }
        },
        {
          "name": "Obtener Ejercicios de una Rutina",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{ejercicios_url}}/api/ejercicios/rutina/1",
              "host": ["{{ejercicios_url}}"],
              "path": ["api", "ejercicios", "rutina", "1"]
            }
          }
        },
        {
          "name": "Calcular Tiempo Total de Rutina",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{ejercicios_url}}/api/ejercicios/rutina/1/tiempo-total",
              "host": ["{{ejercicios_url}}"],
              "path": ["api", "ejercicios", "rutina", "1", "tiempo-total"]
            }
          }
        },
        {
          "name": "Crear Ejercicio - Press de Banca",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"rutina_id\": 1,\n  \"nombre\": \"Press de banca\",\n  \"series\": 4,\n  \"repeticiones\": 10,\n  \"tiempo_descanso\": 90,\n  \"tiempo_ejecucion\": 15,\n  \"categoria\": \"Fuerza\"\n}"
            },
            "url": {
              "raw": "{{ejercicios_url}}/api/ejercicios",
              "host": ["{{ejercicios_url}}"],
              "path": ["api", "ejercicios"]
            }
          }
        },
        {
          "name": "Crear Ejercicio - Sentadillas",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"rutina_id\": 1,\n  \"nombre\": \"Sentadillas\",\n  \"series\": 5,\n  \"repeticiones\": 8,\n  \"tiempo_descanso\": 120,\n  \"tiempo_ejecucion\": 20,\n  \"categoria\": \"Fuerza\"\n}"
            },
            "url": {
              "raw": "{{ejercicios_url}}/api/ejercicios",
              "host": ["{{ejercicios_url}}"],
              "path": ["api", "ejercicios"]
            }
          }
        },
        {
          "name": "Crear Ejercicio - Cardio",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"rutina_id\": 2,\n  \"nombre\": \"Burpees\",\n  \"series\": 6,\n  \"repeticiones\": 15,\n  \"tiempo_descanso\": 30,\n  \"tiempo_ejecucion\": 45,\n  \"categoria\": \"HIIT\"\n}"
            },
            "url": {
              "raw": "{{ejercicios_url}}/api/ejercicios",
              "host": ["{{ejercicios_url}}"],
              "path": ["api", "ejercicios"]
            }
          }
        },
        {
          "name": "Actualizar Ejercicio",
          "request": {
            "method": "PUT",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"series\": 5,\n  \"repeticiones\": 12,\n  \"tiempo_descanso\": 60\n}"
            },
            "url": {
              "raw": "{{ejercicios_url}}/api/ejercicios/1",
              "host": ["{{ejercicios_url}}"],
              "path": ["api", "ejercicios", "1"]
            }
          }
        },
        {
          "name": "Eliminar Ejercicio",
          "request": {
            "method": "DELETE",
            "header": [],
            "url": {
              "raw": "{{ejercicios_url}}/api/ejercicios/1",
              "host": ["{{ejercicios_url}}"],
              "path": ["api", "ejercicios", "1"]
            }
          }
        }
      ]
    }
  ]
}
```

## Configuración de Variables

Antes de usar la colección, configura las URLs de tus servicios:

### Para desarrollo local:
- `rutinas_url`: `http://localhost:8001`
- `ejercicios_url`: `http://localhost:8002`

### Para producción (ejemplo con Render):
- `rutinas_url`: `https://rutinas-service.onrender.com`
- `ejercicios_url`: `https://ejercicios-service.onrender.com`

## Flujo de Prueba Recomendado

1. **Health Checks**: Verificar que ambos servicios estén activos
2. **Crear Rutinas**: Crear 2-3 rutinas de ejemplo
3. **Crear Ejercicios**: Agregar ejercicios a las rutinas creadas
4. **Consultar**: Listar y filtrar los datos
5. **Calcular Tiempos**: Verificar el cálculo de tiempos totales
6. **Actualizar**: Modificar rutinas y ejercicios
7. **Eliminar**: Limpiar datos de prueba
