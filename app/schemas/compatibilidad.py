from pydantic import BaseModel

class CompatibilidadBase(BaseModel):
    categoria_id: int
    componente_id: int

class CompatibilidadCreate(CompatibilidadBase):
    pass

class Compatibilidad(CompatibilidadBase):
    id: int

    class Config:
        orm_mode = True
