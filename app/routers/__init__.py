from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import models
from app.models.database import get_db
from app.schemas import categorias as categorias_schemas
from app.schemas import componentes as componentes_schemas
from app.schemas import compatibilidad as compatibilidad_schemas

# Rutas para categorías
categorias_router = APIRouter(prefix="/categorias", tags=["Categorías"])

@categorias_router.get("/", response_model=list[categorias_schemas.Categoria])
def listar_categorias(db: Session = Depends(get_db)):
    return db.query(models.Categoria).all()

@categorias_router.get("/{id}", response_model=categorias_schemas.Categoria)
def obtener_categoria(id: int, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@categorias_router.post("/", response_model=categorias_schemas.Categoria)
def crear_categoria(categoria: categorias_schemas.CategoriaCreate, db: Session = Depends(get_db)):
    nueva_categoria = models.Categoria(**categoria.dict())
    db.add(nueva_categoria)
    db.commit()
    db.refresh(nueva_categoria)
    return nueva_categoria

@categorias_router.put("/{id}", response_model=categorias_schemas.Categoria)
def actualizar_categoria(id: int, categoria_actualizada: categorias_schemas.CategoriaCreate, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    categoria.nombre = categoria_actualizada.nombre
    db.commit()
    db.refresh(categoria)
    return categoria

@categorias_router.delete("/{id}", status_code=204)
def eliminar_categoria(id: int, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    db.delete(categoria)
    db.commit()
    return {"message": "Categoría eliminada"}

# Rutas para componentes
componentes_router = APIRouter(prefix="/componentes", tags=["Componentes"])

@componentes_router.get("/", response_model=list[componentes_schemas.Componente])
def listar_componentes(db: Session = Depends(get_db)):
    return db.query(models.Componente).all()

@componentes_router.get("/{id}", response_model=componentes_schemas.Componente)
def obtener_componente(id: int, db: Session = Depends(get_db)):
    componente = db.query(models.Componente).filter(models.Componente.id == id).first()
    if not componente:
        raise HTTPException(status_code=404, detail="Componente no encontrado")
    return componente

@componentes_router.post("/", response_model=componentes_schemas.Componente)
def crear_componente(componente: componentes_schemas.ComponenteCreate, db: Session = Depends(get_db)):
    nuevo_componente = models.Componente(**componente.dict())
    db.add(nuevo_componente)
    db.commit()
    db.refresh(nuevo_componente)
    return nuevo_componente

@componentes_router.put("/{id}", response_model=componentes_schemas.Componente)
def actualizar_componente(id: int, componente_actualizado: componentes_schemas.ComponenteCreate, db: Session = Depends(get_db)):
    componente = db.query(models.Componente).filter(models.Componente.id == id).first()
    if not componente:
        raise HTTPException(status_code=404, detail="Componente no encontrado")
    componente.nombre = componente_actualizado.nombre
    componente.categoria_id = componente_actualizado.categoria_id
    componente.marca = componente_actualizado.marca
    componente.modelo = componente_actualizado.modelo
    componente.cantidad = componente_actualizado.cantidad
    componente.precio = componente_actualizado.precio
    componente.descripcion = componente_actualizado.descripcion
    db.commit()
    db.refresh(componente)
    return componente

@componentes_router.delete("/{id}", status_code=204)
def eliminar_componente(id: int, db: Session = Depends(get_db)):
    componente = db.query(models.Componente).filter(models.Componente.id == id).first()
    if not componente:
        raise HTTPException(status_code=404, detail="Componente no encontrado")
    db.delete(componente)
    db.commit()
    return {"message": "Componente eliminado"}

# Rutas para compatibilidad
compatibilidad_router = APIRouter(prefix="/compatibilidad", tags=["Compatibilidad"])

@compatibilidad_router.get("/", response_model=list[compatibilidad_schemas.Compatibilidad])
def listar_compatibilidades(db: Session = Depends(get_db)):
    return db.query(models.Compatibilidad).all()

@compatibilidad_router.get("/{id}", response_model=compatibilidad_schemas.Compatibilidad)
def obtener_compatibilidad(id: int, db: Session = Depends(get_db)):
    compatibilidad = db.query(models.Compatibilidad).filter(models.Compatibilidad.id == id).first()
    if not compatibilidad:
        raise HTTPException(status_code=404, detail="Compatibilidad no encontrada")
    return compatibilidad

@compatibilidad_router.post("/", response_model=compatibilidad_schemas.Compatibilidad)
def crear_compatibilidad(data: compatibilidad_schemas.CompatibilidadCreate, db: Session = Depends(get_db)):
    nueva_compatibilidad = models.Compatibilidad(**data.dict())
    db.add(nueva_compatibilidad)
    db.commit()
    db.refresh(nueva_compatibilidad)
    return nueva_compatibilidad

@compatibilidad_router.put("/{id}", response_model=compatibilidad_schemas.Compatibilidad)
def actualizar_compatibilidad(id: int, compatibilidad_actualizada: compatibilidad_schemas.CompatibilidadCreate, db: Session = Depends(get_db)):
    compatibilidad = db.query(models.Compatibilidad).filter(models.Compatibilidad.id == id).first()
    if not compatibilidad:
        raise HTTPException(status_code=404, detail="Compatibilidad no encontrada")
    compatibilidad.categoria_id = compatibilidad_actualizada.categoria_id
    compatibilidad.componente_id = compatibilidad_actualizada.componente_id
    db.commit()
    db.refresh(compatibilidad)
    return compatibilidad

@compatibilidad_router.delete("/{id}", status_code=204)
def eliminar_compatibilidad(id: int, db: Session = Depends(get_db)):
    compatibilidad = db.query(models.Compatibilidad).filter(models.Compatibilidad.id == id).first()
    if not compatibilidad:
        raise HTTPException(status_code=404, detail="Compatibilidad no encontrada")
    db.delete(compatibilidad)
    db.commit()
    return {"message": "Compatibilidad eliminada"}
