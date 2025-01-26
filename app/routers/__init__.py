from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import models
from app.models.database import get_db
from app.schemas import componentes as componentes_schemas
from app.schemas import categorias as categorias_schemas
from app.schemas import compatibilidad as compatibilidad_schemas

router = APIRouter()

# --- Endpoints de Categorías ---
@router.post("/categorias/", response_model=categorias_schemas.Categoria)
def crear_categoria(categoria: categorias_schemas.CategoriaCreate, db: Session = Depends(get_db)):
    nueva_categoria = models.Categoria(**categoria.dict())
    db.add(nueva_categoria)
    db.commit()
    db.refresh(nueva_categoria)
    return nueva_categoria

@router.get("/categorias/", response_model=list[categorias_schemas.Categoria])
def listar_categorias(db: Session = Depends(get_db)):
    return db.query(models.Categoria).all()

# --- Endpoints de Componentes ---
@router.post("/componentes/", response_model=componentes_schemas.Componente)
def crear_componente(componente: componentes_schemas.ComponenteCreate, db: Session = Depends(get_db)):
    nuevo_componente = models.Componente(**componente.dict())
    db.add(nuevo_componente)
    db.commit()
    db.refresh(nuevo_componente)
    return nuevo_componente

@router.get("/componentes/", response_model=list[componentes_schemas.Componente])
def listar_componentes(db: Session = Depends(get_db)):
    return db.query(models.Componente).all()

# --- Endpoints de Compatibilidad ---
@router.post("/compatibilidad/", response_model=compatibilidad_schemas.Compatibilidad)
def crear_compatibilidad(data: compatibilidad_schemas.CompatibilidadCreate, db: Session = Depends(get_db)):
    nueva_compatibilidad = models.Compatibilidad(**data.dict())
    db.add(nueva_compatibilidad)
    db.commit()
    db.refresh(nueva_compatibilidad)
    return nueva_compatibilidad

@router.get("/compatibilidad/", response_model=list[compatibilidad_schemas.Compatibilidad])
def listar_compatibilidades(db: Session = Depends(get_db)):
    return db.query(models.Compatibilidad).all()
