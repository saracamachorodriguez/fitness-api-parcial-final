from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime
from contextlib import asynccontextmanager
import sqlite3
import os

# Lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown (si fuera necesario)

app = FastAPI(
    title="Microservicio de Ejercicios",
    description="API REST para gestionar ejercicios y tiempos de entrenamiento",
    version="1.0.0",
    lifespan=lifespan
)

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos Pydantic
class EjercicioBase(BaseModel):
    rutina_id: int = Field(..., description="ID de la rutina a la que pertenece")
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre del ejercicio")
    series: int = Field(..., gt=0, description="Número de series")
    repeticiones: int = Field(..., gt=0, description="Número de repeticiones por serie")
    tiempo_descanso: int = Field(..., ge=0, description="Tiempo de descanso en segundos")
    tiempo_ejecucion: int = Field(..., gt=0, description="Tiempo de ejecución en segundos")
    categoria: str = Field(..., description="Categoría: Fuerza, Cardio, Flexibilidad, etc.")

class EjercicioCreate(EjercicioBase):
    pass

class EjercicioUpdate(BaseModel):
    rutina_id: Optional[int] = None
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    series: Optional[int] = Field(None, gt=0)
    repeticiones: Optional[int] = Field(None, gt=0)
    tiempo_descanso: Optional[int] = Field(None, ge=0)
    tiempo_ejecucion: Optional[int] = Field(None, gt=0)
    categoria: Optional[str] = None

class Ejercicio(EjercicioBase):
    id: int
    fecha_creacion: str

    model_config = ConfigDict(from_attributes=True)

class TiempoTotal(BaseModel):
    rutina_id: int
    total_ejercicios: int
    tiempo_total_ejecucion: int
    tiempo_total_descanso: int
    tiempo_total_estimado: int

# Base de datos
DB_PATH = os.getenv("DB_PATH", "ejercicios.db")

def get_db_connection():
    """Crear conexión a la base de datos"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicializar base de datos"""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS ejercicios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rutina_id INTEGER NOT NULL,
            nombre TEXT NOT NULL,
            series INTEGER NOT NULL,
            repeticiones INTEGER NOT NULL,
            tiempo_descanso INTEGER NOT NULL,
            tiempo_ejecucion INTEGER NOT NULL,
            categoria TEXT NOT NULL,
            fecha_creacion TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Funciones auxiliares
def calcular_tiempo_total_ejercicio(ejercicio: dict) -> int:
    """Calcular el tiempo total de un ejercicio (ejecución + descanso * series)"""
    tiempo_ejecucion_total = ejercicio['tiempo_ejecucion'] * ejercicio['series']
    tiempo_descanso_total = ejercicio['tiempo_descanso'] * (ejercicio['series'] - 1)  # No hay descanso después de la última serie
    return tiempo_ejecucion_total + tiempo_descanso_total

# Endpoints
@app.get("/", tags=["Root"])
async def root():
    """Endpoint raíz"""
    return {
        "message": "Microservicio de Ejercicios y Tiempos",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "docs": "/docs",
            "ejercicios": "/api/ejercicios"
        }
    }

@app.get("/health", tags=["Health"])
async def health_check():
    """Health check del servicio"""
    return {
        "status": "healthy",
        "service": "ejercicios-service",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api/ejercicios", response_model=List[Ejercicio], tags=["Ejercicios"])
async def listar_ejercicios(categoria: Optional[str] = None):
    """Obtener todos los ejercicios, opcionalmente filtrados por categoría"""
    conn = get_db_connection()
    
    if categoria:
        ejercicios = conn.execute(
            'SELECT * FROM ejercicios WHERE categoria = ? ORDER BY fecha_creacion DESC',
            (categoria,)
        ).fetchall()
    else:
        ejercicios = conn.execute('SELECT * FROM ejercicios ORDER BY fecha_creacion DESC').fetchall()
    
    conn.close()
    return [dict(ejercicio) for ejercicio in ejercicios]

@app.get("/api/ejercicios/{ejercicio_id}", response_model=Ejercicio, tags=["Ejercicios"])
async def obtener_ejercicio(ejercicio_id: int):
    """Obtener un ejercicio específico por ID"""
    conn = get_db_connection()
    ejercicio = conn.execute('SELECT * FROM ejercicios WHERE id = ?', (ejercicio_id,)).fetchone()
    conn.close()
    
    if ejercicio is None:
        raise HTTPException(status_code=404, detail=f"Ejercicio con ID {ejercicio_id} no encontrado")
    
    return dict(ejercicio)

@app.get("/api/ejercicios/rutina/{rutina_id}", response_model=List[Ejercicio], tags=["Ejercicios"])
async def obtener_ejercicios_por_rutina(rutina_id: int):
    """Obtener todos los ejercicios de una rutina específica"""
    conn = get_db_connection()
    ejercicios = conn.execute(
        'SELECT * FROM ejercicios WHERE rutina_id = ? ORDER BY id',
        (rutina_id,)
    ).fetchall()
    conn.close()
    
    return [dict(ejercicio) for ejercicio in ejercicios]

@app.get("/api/ejercicios/rutina/{rutina_id}/tiempo-total", response_model=TiempoTotal, tags=["Tiempos"])
async def calcular_tiempo_total_rutina(rutina_id: int):
    """Calcular el tiempo total estimado de una rutina"""
    conn = get_db_connection()
    ejercicios = conn.execute(
        'SELECT * FROM ejercicios WHERE rutina_id = ?',
        (rutina_id,)
    ).fetchall()
    conn.close()
    
    if not ejercicios:
        raise HTTPException(
            status_code=404, 
            detail=f"No se encontraron ejercicios para la rutina {rutina_id}"
        )
    
    tiempo_total_ejecucion = 0
    tiempo_total_descanso = 0
    
    for ejercicio in ejercicios:
        ej_dict = dict(ejercicio)
        tiempo_total_ejecucion += ej_dict['tiempo_ejecucion'] * ej_dict['series']
        tiempo_total_descanso += ej_dict['tiempo_descanso'] * (ej_dict['series'] - 1)
    
    tiempo_total_estimado = tiempo_total_ejecucion + tiempo_total_descanso
    
    return {
        "rutina_id": rutina_id,
        "total_ejercicios": len(ejercicios),
        "tiempo_total_ejecucion": tiempo_total_ejecucion,
        "tiempo_total_descanso": tiempo_total_descanso,
        "tiempo_total_estimado": tiempo_total_estimado
    }

@app.post("/api/ejercicios", response_model=Ejercicio, status_code=201, tags=["Ejercicios"])
async def crear_ejercicio(ejercicio: EjercicioCreate):
    """Crear un nuevo ejercicio"""
    # Validar categoría
    categorias_validas = ["Fuerza", "Cardio", "Flexibilidad", "Resistencia", "HIIT", "Funcional"]
    if ejercicio.categoria not in categorias_validas:
        raise HTTPException(
            status_code=400, 
            detail=f"Categoría inválida. Debe ser una de: {', '.join(categorias_validas)}"
        )
    
    fecha_creacion = datetime.now().isoformat()
    conn = get_db_connection()
    cursor = conn.execute(
        '''INSERT INTO ejercicios 
           (rutina_id, nombre, series, repeticiones, tiempo_descanso, tiempo_ejecucion, categoria, fecha_creacion) 
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        (ejercicio.rutina_id, ejercicio.nombre, ejercicio.series, ejercicio.repeticiones, 
         ejercicio.tiempo_descanso, ejercicio.tiempo_ejecucion, ejercicio.categoria, fecha_creacion)
    )
    conn.commit()
    ejercicio_id = cursor.lastrowid
    
    nuevo_ejercicio = conn.execute('SELECT * FROM ejercicios WHERE id = ?', (ejercicio_id,)).fetchone()
    conn.close()
    
    return dict(nuevo_ejercicio)

@app.put("/api/ejercicios/{ejercicio_id}", response_model=Ejercicio, tags=["Ejercicios"])
async def actualizar_ejercicio(ejercicio_id: int, ejercicio: EjercicioUpdate):
    """Actualizar un ejercicio existente"""
    conn = get_db_connection()
    ejercicio_existente = conn.execute('SELECT * FROM ejercicios WHERE id = ?', (ejercicio_id,)).fetchone()
    
    if ejercicio_existente is None:
        conn.close()
        raise HTTPException(status_code=404, detail=f"Ejercicio con ID {ejercicio_id} no encontrado")
    
    # Validar categoría si se proporciona
    if ejercicio.categoria is not None:
        categorias_validas = ["Fuerza", "Cardio", "Flexibilidad", "Resistencia", "HIIT", "Funcional"]
        if ejercicio.categoria not in categorias_validas:
            conn.close()
            raise HTTPException(
                status_code=400, 
                detail=f"Categoría inválida. Debe ser una de: {', '.join(categorias_validas)}"
            )
    
    # Actualizar solo los campos proporcionados
    updates = []
    params = []
    
    if ejercicio.rutina_id is not None:
        updates.append("rutina_id = ?")
        params.append(ejercicio.rutina_id)
    if ejercicio.nombre is not None:
        updates.append("nombre = ?")
        params.append(ejercicio.nombre)
    if ejercicio.series is not None:
        updates.append("series = ?")
        params.append(ejercicio.series)
    if ejercicio.repeticiones is not None:
        updates.append("repeticiones = ?")
        params.append(ejercicio.repeticiones)
    if ejercicio.tiempo_descanso is not None:
        updates.append("tiempo_descanso = ?")
        params.append(ejercicio.tiempo_descanso)
    if ejercicio.tiempo_ejecucion is not None:
        updates.append("tiempo_ejecucion = ?")
        params.append(ejercicio.tiempo_ejecucion)
    if ejercicio.categoria is not None:
        updates.append("categoria = ?")
        params.append(ejercicio.categoria)
    
    if updates:
        params.append(ejercicio_id)
        query = f"UPDATE ejercicios SET {', '.join(updates)} WHERE id = ?"
        conn.execute(query, params)
        conn.commit()
    
    ejercicio_actualizado = conn.execute('SELECT * FROM ejercicios WHERE id = ?', (ejercicio_id,)).fetchone()
    conn.close()
    
    return dict(ejercicio_actualizado)

@app.delete("/api/ejercicios/{ejercicio_id}", tags=["Ejercicios"])
async def eliminar_ejercicio(ejercicio_id: int):
    """Eliminar un ejercicio"""
    conn = get_db_connection()
    ejercicio = conn.execute('SELECT * FROM ejercicios WHERE id = ?', (ejercicio_id,)).fetchone()
    
    if ejercicio is None:
        conn.close()
        raise HTTPException(status_code=404, detail=f"Ejercicio con ID {ejercicio_id} no encontrado")
    
    conn.execute('DELETE FROM ejercicios WHERE id = ?', (ejercicio_id,))
    conn.commit()
    conn.close()
    
    return {
        "message": f"Ejercicio con ID {ejercicio_id} eliminado exitosamente",
        "deleted_id": ejercicio_id
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8002))
    uvicorn.run(app, host="0.0.0.0", port=port)
