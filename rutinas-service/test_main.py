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
    assert data["service"] == "rutinas-service"
    assert "timestamp" in data

# Tests CRUD para Rutinas
def test_crear_rutina(client):
    """Test de creación de rutina"""
    rutina_data = {
        "nombre": "Rutina de Fuerza",
        "descripcion": "Entrenamiento de fuerza básico",
        "duracion_estimada": 60,
        "nivel": "Intermedio"
    }
    response = client.post("/api/rutinas", json=rutina_data)
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == rutina_data["nombre"]
    assert data["duracion_estimada"] == rutina_data["duracion_estimada"]
    assert data["nivel"] == rutina_data["nivel"]
    assert "id" in data
    assert "fecha_creacion" in data

def test_crear_rutina_nivel_invalido(client):
    """Test de creación de rutina con nivel inválido"""
    rutina_data = {
        "nombre": "Rutina Test",
        "descripcion": "Test",
        "duracion_estimada": 30,
        "nivel": "Experto"  # Nivel inválido
    }
    response = client.post("/api/rutinas", json=rutina_data)
    assert response.status_code == 400
    assert "Nivel inválido" in response.json()["detail"]

def test_listar_rutinas(client):
    """Test de listado de rutinas"""
    # Crear rutinas de prueba
    rutinas = [
        {"nombre": "Rutina 1", "descripcion": "Desc 1", "duracion_estimada": 30, "nivel": "Principiante"},
        {"nombre": "Rutina 2", "descripcion": "Desc 2", "duracion_estimada": 45, "nivel": "Intermedio"},
    ]
    for rutina in rutinas:
        client.post("/api/rutinas", json=rutina)
    
    response = client.get("/api/rutinas")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert isinstance(data, list)

def test_obtener_rutina_existente(client):
    """Test de obtener una rutina específica"""
    # Crear rutina
    rutina_data = {
        "nombre": "Rutina Test",
        "descripcion": "Test",
        "duracion_estimada": 40,
        "nivel": "Avanzado"
    }
    create_response = client.post("/api/rutinas", json=rutina_data)
    rutina_id = create_response.json()["id"]
    
    # Obtener rutina
    response = client.get(f"/api/rutinas/{rutina_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == rutina_id
    assert data["nombre"] == rutina_data["nombre"]

def test_obtener_rutina_no_existente(client):
    """Test de obtener una rutina que no existe"""
    response = client.get("/api/rutinas/9999")
    assert response.status_code == 404
    assert "no encontrada" in response.json()["detail"]

def test_actualizar_rutina(client):
    """Test de actualización de rutina"""
    # Crear rutina
    rutina_data = {
        "nombre": "Rutina Original",
        "descripcion": "Descripción original",
        "duracion_estimada": 30,
        "nivel": "Principiante"
    }
    create_response = client.post("/api/rutinas", json=rutina_data)
    rutina_id = create_response.json()["id"]
    
    # Actualizar rutina
    update_data = {
        "nombre": "Rutina Actualizada",
        "duracion_estimada": 45
    }
    response = client.put(f"/api/rutinas/{rutina_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == update_data["nombre"]
    assert data["duracion_estimada"] == update_data["duracion_estimada"]
    assert data["descripcion"] == rutina_data["descripcion"]  # No cambiado

def test_actualizar_rutina_no_existente(client):
    """Test de actualizar una rutina que no existe"""
    update_data = {"nombre": "Test"}
    response = client.put("/api/rutinas/9999", json=update_data)
    assert response.status_code == 404

def test_eliminar_rutina(client):
    """Test de eliminación de rutina"""
    # Crear rutina
    rutina_data = {
        "nombre": "Rutina a Eliminar",
        "descripcion": "Test",
        "duracion_estimada": 30,
        "nivel": "Principiante"
    }
    create_response = client.post("/api/rutinas", json=rutina_data)
    rutina_id = create_response.json()["id"]
    
    # Eliminar rutina
    response = client.delete(f"/api/rutinas/{rutina_id}")
    assert response.status_code == 200
    assert "eliminada exitosamente" in response.json()["message"]
    
    # Verificar que ya no existe
    get_response = client.get(f"/api/rutinas/{rutina_id}")
    assert get_response.status_code == 404

def test_eliminar_rutina_no_existente(client):
    """Test de eliminar una rutina que no existe"""
    response = client.delete("/api/rutinas/9999")
    assert response.status_code == 404

# Tests de validación
def test_crear_rutina_sin_nombre(client):
    """Test de crear rutina sin nombre"""
    rutina_data = {
        "descripcion": "Test",
        "duracion_estimada": 30,
        "nivel": "Principiante"
    }
    response = client.post("/api/rutinas", json=rutina_data)
    assert response.status_code == 422  # Validation error

def test_crear_rutina_duracion_negativa(client):
    """Test de crear rutina con duración negativa"""
    rutina_data = {
        "nombre": "Test",
        "descripcion": "Test",
        "duracion_estimada": -10,
        "nivel": "Principiante"
    }
    response = client.post("/api/rutinas", json=rutina_data)
    assert response.status_code == 422  # Validation error

# Test de integración: flujo completo
def test_flujo_completo_rutina(client):
    """Test del flujo completo: crear, leer, actualizar, eliminar"""
    # Crear
    rutina_data = {
        "nombre": "Rutina Completa",
        "descripcion": "Test de flujo completo",
        "duracion_estimada": 50,
        "nivel": "Intermedio"
    }
    create_response = client.post("/api/rutinas", json=rutina_data)
    assert create_response.status_code == 201
    rutina_id = create_response.json()["id"]
    
    # Leer
    get_response = client.get(f"/api/rutinas/{rutina_id}")
    assert get_response.status_code == 200
    
    # Actualizar
    update_data = {"duracion_estimada": 60}
    update_response = client.put(f"/api/rutinas/{rutina_id}", json=update_data)
    assert update_response.status_code == 200
    assert update_response.json()["duracion_estimada"] == 60
    
    # Eliminar
    delete_response = client.delete(f"/api/rutinas/{rutina_id}")
    assert delete_response.status_code == 200
    
    # Verificar eliminación
    final_get_response = client.get(f"/api/rutinas/{rutina_id}")
    assert final_get_response.status_code == 404
