from fastapi import FastAPI
from app.models.database import Base, engine
from app.routers import router  # Importa el enrutador unificado

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# Instancia de la aplicación
app = FastAPI(title="Microservicio de Inventario")

# Incluir los enrutadores
app.include_router(router)
