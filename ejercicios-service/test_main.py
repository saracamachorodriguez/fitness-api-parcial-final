import pytest
from fastapi.testclient import TestClient
from main import app, init_db, get_db_connection
import os
import tempfile

# Configurar base de datos de prueba
@pytest.fixture(scope="function")
def test_db():
    """Crear una base de datos temporal para las pruebas"""
    db_fd, db_path = tempfile.mkstemp()
    os.environ["DB_PATH"] = db_path
    
    # Inicializar la base de datos
    init_db()
    
    yield db_path
    
    # Limpiar
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture(scope="function")
def client(test_db):
    """Cliente de prueba de FastAPI"""
    return TestClient(app)

# Tests para el endpoint raíz
def test_root(client):
    """Test del endpoint raíz"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert data["version"] == "1.0.0"

# Tests para health check
def test_health_check(client):
    """Test del health check"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "ejercicios-service"
    assert "timestamp" in data

# Tests CRUD para Ejercicios
def test_crear_ejercicio(client):
    """Test de creación de ejercicio"""
    ejercicio_data = {
        "rutina_id": 1,
        "nombre": "Press de banca",
        "series": 4,
        "repeticiones": 10,
        "tiempo_descanso": 90,
        "tiempo_ejecucion": 15,
        "categoria": "Fuerza"
    }
    response = client.post("/api/ejercicios", json=ejercicio_data)
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == ejercicio_data["nombre"]
    assert data["series"] == ejercicio_data["series"]
    assert data["categoria"] == ejercicio_data["categoria"]
    assert "id" in data
    assert "fecha_creacion" in data

def test_crear_ejercicio_categoria_invalida(client):
    """Test de creación de ejercicio con categoría inválida"""
    ejercicio_data = {
        "rutina_id": 1,
        "nombre": "Test",
        "series": 3,
        "repeticiones": 10,
        "tiempo_descanso": 60,
        "tiempo_ejecucion": 10,
        "categoria": "Invalida"
    }
    response = client.post("/api/ejercicios", json=ejercicio_data)
    assert response.status_code == 400
    assert "Categoría inválida" in response.json()["detail"]

def test_listar_ejercicios(client):
    """Test de listado de ejercicios"""
    # Crear ejercicios de prueba
    ejercicios = [
        {"rutina_id": 1, "nombre": "Ejercicio 1", "series": 3, "repeticiones": 10, 
         "tiempo_descanso": 60, "tiempo_ejecucion": 10, "categoria": "Fuerza"},
        {"rutina_id": 1, "nombre": "Ejercicio 2", "series": 4, "repeticiones": 12, 
         "tiempo_descanso": 90, "tiempo_ejecucion": 15, "categoria": "Cardio"},
    ]
    for ejercicio in ejercicios:
        client.post("/api/ejercicios", json=ejercicio)
    
    response = client.get("/api/ejercicios")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert isinstance(data, list)

def test_listar_ejercicios_por_categoria(client):
    """Test de listado de ejercicios filtrado por categoría"""
    # Crear ejercicios
    ejercicios = [
        {"rutina_id": 1, "nombre": "Press banca", "series": 4, "repeticiones": 10, 
         "tiempo_descanso": 90, "tiempo_ejecucion": 15, "categoria": "Fuerza"},
        {"rutina_id": 1, "nombre": "Correr", "series": 1, "repeticiones": 1, 
         "tiempo_descanso": 0, "tiempo_ejecucion": 1200, "categoria": "Cardio"},
    ]
    for ejercicio in ejercicios:
        client.post("/api/ejercicios", json=ejercicio)
    
    response = client.get("/api/ejercicios?categoria=Fuerza")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["categoria"] == "Fuerza"

def test_obtener_ejercicio_existente(client):
    """Test de obtener un ejercicio específico"""
    # Crear ejercicio
    ejercicio_data = {
        "rutina_id": 1,
        "nombre": "Sentadillas",
        "series": 5,
        "repeticiones": 8,
        "tiempo_descanso": 120,
        "tiempo_ejecucion": 20,
        "categoria": "Fuerza"
    }
    create_response = client.post("/api/ejercicios", json=ejercicio_data)
    ejercicio_id = create_response.json()["id"]
    
    # Obtener ejercicio
    response = client.get(f"/api/ejercicios/{ejercicio_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == ejercicio_id
    assert data["nombre"] == ejercicio_data["nombre"]

def test_obtener_ejercicio_no_existente(client):
    """Test de obtener un ejercicio que no existe"""
    response = client.get("/api/ejercicios/9999")
    assert response.status_code == 404
    assert "no encontrado" in response.json()["detail"]

def test_obtener_ejercicios_por_rutina(client):
    """Test de obtener ejercicios por rutina"""
    # Crear ejercicios para diferentes rutinas
    ejercicios = [
        {"rutina_id": 1, "nombre": "Ej Rutina 1-1", "series": 3, "repeticiones": 10, 
         "tiempo_descanso": 60, "tiempo_ejecucion": 10, "categoria": "Fuerza"},
        {"rutina_id": 1, "nombre": "Ej Rutina 1-2", "series": 3, "repeticiones": 10, 
         "tiempo_descanso": 60, "tiempo_ejecucion": 10, "categoria": "Fuerza"},
        {"rutina_id": 2, "nombre": "Ej Rutina 2-1", "series": 4, "repeticiones": 12, 
         "tiempo_descanso": 90, "tiempo_ejecucion": 15, "categoria": "Cardio"},
    ]
    for ejercicio in ejercicios:
        client.post("/api/ejercicios", json=ejercicio)
    
    response = client.get("/api/ejercicios/rutina/1")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert all(ej["rutina_id"] == 1 for ej in data)

def test_calcular_tiempo_total_rutina(client):
    """Test de cálculo de tiempo total de una rutina"""
    # Crear ejercicios
    ejercicios = [
        {"rutina_id": 1, "nombre": "Ejercicio 1", "series": 3, "repeticiones": 10, 
         "tiempo_descanso": 60, "tiempo_ejecucion": 10, "categoria": "Fuerza"},
        {"rutina_id": 1, "nombre": "Ejercicio 2", "series": 4, "repeticiones": 12, 
         "tiempo_descanso": 90, "tiempo_ejecucion": 15, "categoria": "Fuerza"},
    ]
    for ejercicio in ejercicios:
        client.post("/api/ejercicios", json=ejercicio)
    
    response = client.get("/api/ejercicios/rutina/1/tiempo-total")
    assert response.status_code == 200
    data = response.json()
    assert data["rutina_id"] == 1
    assert data["total_ejercicios"] == 2
    # Ejercicio 1: (10*3) + (60*2) = 30 + 120 = 150
    # Ejercicio 2: (15*4) + (90*3) = 60 + 270 = 330
    # Total: 480 segundos
    assert data["tiempo_total_estimado"] == 480

def test_calcular_tiempo_total_rutina_sin_ejercicios(client):
    """Test de cálculo de tiempo total para rutina sin ejercicios"""
    response = client.get("/api/ejercicios/rutina/999/tiempo-total")
    assert response.status_code == 404
    assert "No se encontraron ejercicios" in response.json()["detail"]

def test_actualizar_ejercicio(client):
    """Test de actualización de ejercicio"""
    # Crear ejercicio
    ejercicio_data = {
        "rutina_id": 1,
        "nombre": "Ejercicio Original",
        "series": 3,
        "repeticiones": 10,
        "tiempo_descanso": 60,
        "tiempo_ejecucion": 10,
        "categoria": "Fuerza"
    }
    create_response = client.post("/api/ejercicios", json=ejercicio_data)
    ejercicio_id = create_response.json()["id"]
    
    # Actualizar ejercicio
    update_data = {
        "nombre": "Ejercicio Actualizado",
        "series": 5
    }
    response = client.put(f"/api/ejercicios/{ejercicio_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == update_data["nombre"]
    assert data["series"] == update_data["series"]
    assert data["repeticiones"] == ejercicio_data["repeticiones"]  # No cambiado

def test_actualizar_ejercicio_no_existente(client):
    """Test de actualizar un ejercicio que no existe"""
    update_data = {"nombre": "Test"}
    response = client.put("/api/ejercicios/9999", json=update_data)
    assert response.status_code == 404

def test_eliminar_ejercicio(client):
    """Test de eliminación de ejercicio"""
    # Crear ejercicio
    ejercicio_data = {
        "rutina_id": 1,
        "nombre": "Ejercicio a Eliminar",
        "series": 3,
        "repeticiones": 10,
        "tiempo_descanso": 60,
        "tiempo_ejecucion": 10,
        "categoria": "Fuerza"
    }
    create_response = client.post("/api/ejercicios", json=ejercicio_data)
    ejercicio_id = create_response.json()["id"]
    
    # Eliminar ejercicio
    response = client.delete(f"/api/ejercicios/{ejercicio_id}")
    assert response.status_code == 200
    assert "eliminado exitosamente" in response.json()["message"]
    
    # Verificar que ya no existe
    get_response = client.get(f"/api/ejercicios/{ejercicio_id}")
    assert get_response.status_code == 404

def test_eliminar_ejercicio_no_existente(client):
    """Test de eliminar un ejercicio que no existe"""
    response = client.delete("/api/ejercicios/9999")
    assert response.status_code == 404

# Tests de validación
def test_crear_ejercicio_sin_nombre(client):
    """Test de crear ejercicio sin nombre"""
    ejercicio_data = {
        "rutina_id": 1,
        "series": 3,
        "repeticiones": 10,
        "tiempo_descanso": 60,
        "tiempo_ejecucion": 10,
        "categoria": "Fuerza"
    }
    response = client.post("/api/ejercicios", json=ejercicio_data)
    assert response.status_code == 422  # Validation error

def test_crear_ejercicio_series_negativas(client):
    """Test de crear ejercicio con series negativas"""
    ejercicio_data = {
        "rutina_id": 1,
        "nombre": "Test",
        "series": -1,
        "repeticiones": 10,
        "tiempo_descanso": 60,
        "tiempo_ejecucion": 10,
        "categoria": "Fuerza"
    }
    response = client.post("/api/ejercicios", json=ejercicio_data)
    assert response.status_code == 422  # Validation error

# Test de integración: flujo completo
def test_flujo_completo_ejercicio(client):
    """Test del flujo completo: crear, leer, actualizar, eliminar"""
    # Crear
    ejercicio_data = {
        "rutina_id": 1,
        "nombre": "Ejercicio Completo",
        "series": 4,
        "repeticiones": 10,
        "tiempo_descanso": 90,
        "tiempo_ejecucion": 15,
        "categoria": "Fuerza"
    }
    create_response = client.post("/api/ejercicios", json=ejercicio_data)
    assert create_response.status_code == 201
    ejercicio_id = create_response.json()["id"]
    
    # Leer
    get_response = client.get(f"/api/ejercicios/{ejercicio_id}")
    assert get_response.status_code == 200
    
    # Actualizar
    update_data = {"series": 5, "repeticiones": 12}
    update_response = client.put(f"/api/ejercicios/{ejercicio_id}", json=update_data)
    assert update_response.status_code == 200
    assert update_response.json()["series"] == 5
    
    # Eliminar
    delete_response = client.delete(f"/api/ejercicios/{ejercicio_id}")
    assert delete_response.status_code == 200
    
    # Verificar eliminación
    final_get_response = client.get(f"/api/ejercicios/{ejercicio_id}")
    assert final_get_response.status_code == 404
