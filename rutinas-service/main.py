from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import sqlite3
import os

app = FastAPI(
    title="Microservicio de Rutinas",
    description="API REST para gestionar rutinas de entrenamiento",
    version="1.0.0"
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
class RutinaBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre de la rutina")
    descripcion: Optional[str] = Field(None, max_length=500, description="Descripción de la rutina")
    duracion_estimada: int = Field(..., gt=0, description="Duración estimada en minutos")
    nivel: str = Field(..., description="Nivel de dificultad: Principiante, Intermedio, Avanzado")

class RutinaCreate(RutinaBase):
    pass

class RutinaUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=500)
    duracion_estimada: Optional[int] = Field(None, gt=0)
    nivel: Optional[str] = None

class Rutina(RutinaBase):
    id: int
    fecha_creacion: str

    class Config:
        from_attributes = True

# Base de datos
DB_PATH = os.getenv("DB_PATH", "rutinas.db")

def get_db_connection():
    """Crear conexión a la base de datos"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicializar base de datos"""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS rutinas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            duracion_estimada INTEGER NOT NULL,
            nivel TEXT NOT NULL,
            fecha_creacion TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Inicializar DB al arrancar
@app.on_event("startup")
async def startup():
    init_db()

# Endpoints
@app.get("/", tags=["Root"])
async def root():
    """Endpoint raíz"""
    return {
        "message": "Microservicio de Rutinas de Entrenamiento",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "docs": "/docs",
            "rutinas": "/api/rutinas"
        }
    }

@app.get("/health", tags=["Health"])
async def health_check():
    """Health check del servicio"""
    return {
        "status": "healthy",
        "service": "rutinas-service",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api/rutinas", response_model=List[Rutina], tags=["Rutinas"])
async def listar_rutinas():
    """Obtener todas las rutinas"""
    conn = get_db_connection()
    rutinas = conn.execute('SELECT * FROM rutinas ORDER BY fecha_creacion DESC').fetchall()
    conn.close()
    return [dict(rutina) for rutina in rutinas]

@app.get("/api/rutinas/{rutina_id}", response_model=Rutina, tags=["Rutinas"])
async def obtener_rutina(rutina_id: int):
    """Obtener una rutina específica por ID"""
    conn = get_db_connection()
    rutina = conn.execute('SELECT * FROM rutinas WHERE id = ?', (rutina_id,)).fetchone()
    conn.close()
    
    if rutina is None:
        raise HTTPException(status_code=404, detail=f"Rutina con ID {rutina_id} no encontrada")
    
    return dict(rutina)

@app.post("/api/rutinas", response_model=Rutina, status_code=201, tags=["Rutinas"])
async def crear_rutina(rutina: RutinaCreate):
    """Crear una nueva rutina"""
    # Validar nivel
    niveles_validos = ["Principiante", "Intermedio", "Avanzado"]
    if rutina.nivel not in niveles_validos:
        raise HTTPException(
            status_code=400, 
            detail=f"Nivel inválido. Debe ser uno de: {', '.join(niveles_validos)}"
        )
    
    fecha_creacion = datetime.now().isoformat()
    conn = get_db_connection()
    cursor = conn.execute(
        'INSERT INTO rutinas (nombre, descripcion, duracion_estimada, nivel, fecha_creacion) VALUES (?, ?, ?, ?, ?)',
        (rutina.nombre, rutina.descripcion, rutina.duracion_estimada, rutina.nivel, fecha_creacion)
    )
    conn.commit()
    rutina_id = cursor.lastrowid
    
    nueva_rutina = conn.execute('SELECT * FROM rutinas WHERE id = ?', (rutina_id,)).fetchone()
    conn.close()
    
    return dict(nueva_rutina)

@app.put("/api/rutinas/{rutina_id}", response_model=Rutina, tags=["Rutinas"])
async def actualizar_rutina(rutina_id: int, rutina: RutinaUpdate):
    """Actualizar una rutina existente"""
    conn = get_db_connection()
    rutina_existente = conn.execute('SELECT * FROM rutinas WHERE id = ?', (rutina_id,)).fetchone()
    
    if rutina_existente is None:
        conn.close()
        raise HTTPException(status_code=404, detail=f"Rutina con ID {rutina_id} no encontrada")
    
    # Validar nivel si se proporciona
    if rutina.nivel is not None:
        niveles_validos = ["Principiante", "Intermedio", "Avanzado"]
        if rutina.nivel not in niveles_validos:
            conn.close()
            raise HTTPException(
                status_code=400, 
                detail=f"Nivel inválido. Debe ser uno de: {', '.join(niveles_validos)}"
            )
    
    # Actualizar solo los campos proporcionados
    updates = []
    params = []
    
    if rutina.nombre is not None:
        updates.append("nombre = ?")
        params.append(rutina.nombre)
    if rutina.descripcion is not None:
        updates.append("descripcion = ?")
        params.append(rutina.descripcion)
    if rutina.duracion_estimada is not None:
        updates.append("duracion_estimada = ?")
        params.append(rutina.duracion_estimada)
    if rutina.nivel is not None:
        updates.append("nivel = ?")
        params.append(rutina.nivel)
    
    if updates:
        params.append(rutina_id)
        query = f"UPDATE rutinas SET {', '.join(updates)} WHERE id = ?"
        conn.execute(query, params)
        conn.commit()
    
    rutina_actualizada = conn.execute('SELECT * FROM rutinas WHERE id = ?', (rutina_id,)).fetchone()
    conn.close()
    
    return dict(rutina_actualizada)

@app.delete("/api/rutinas/{rutina_id}", tags=["Rutinas"])
async def eliminar_rutina(rutina_id: int):
    """Eliminar una rutina"""
    conn = get_db_connection()
    rutina = conn.execute('SELECT * FROM rutinas WHERE id = ?', (rutina_id,)).fetchone()
    
    if rutina is None:
        conn.close()
        raise HTTPException(status_code=404, detail=f"Rutina con ID {rutina_id} no encontrada")
    
    conn.execute('DELETE FROM rutinas WHERE id = ?', (rutina_id,))
    conn.commit()
    conn.close()
    
    return {
        "message": f"Rutina con ID {rutina_id} eliminada exitosamente",
        "deleted_id": rutina_id
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8001))
    uvicorn.run(app, host="0.0.0.0", port=port)
