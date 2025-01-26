from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime, func
from sqlalchemy.orm import relationship
from app.models.database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)

    componentes = relationship("Componente", back_populates="categoria")


class Componente(Base):
    __tablename__ = "componentes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    cantidad = Column(Integer, default=0)
    precio = Column(DECIMAL(10, 2), nullable=False)
    descripcion = Column(String)
    creado_en = Column(DateTime, default=func.now())
    actualizado_en = Column(DateTime, default=func.now(), onupdate=func.now())

    categoria = relationship("Categoria", back_populates="componentes")


class Compatibilidad(Base):
    __tablename__ = "compatibilidad"

    id = Column(Integer, primary_key=True, index=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    componente_id = Column(Integer, ForeignKey("componentes.id"), nullable=False)
