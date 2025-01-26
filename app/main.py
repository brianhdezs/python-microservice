from fastapi import FastAPI
from app.models.database import Base, engine
from app.routers import categorias_router, componentes_router, compatibilidad_router

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# Inicializar la aplicación FastAPI
app = FastAPI(title="Microservicio de Inventario")

# Registrar enrutadores con sus tags
app.include_router(categorias_router)
app.include_router(componentes_router)
app.include_router(compatibilidad_router)
