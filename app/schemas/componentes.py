from pydantic import BaseModel
from decimal import Decimal

class ComponenteBase(BaseModel):
    nombre: str
    categoria_id: int
    marca: str
    modelo: str
    cantidad: int
    precio: Decimal
    descripcion: str | None = None

class ComponenteCreate(ComponenteBase):
    pass

class Componente(ComponenteBase):
    id: int

    class Config:
        orm_mode = True
