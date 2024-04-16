from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, Float
from .model import Model, Base


class Prediccion(Model, Base):
    __tablename__ = 'predicciones'

    resena = Column(String)
    clasificacion = Column(String)
    probabilidad = Column(Float)


    def __init__(self, resena, clasificacion, probabilidad):
        Model.__init__(self)
        self.resena = resena
        self.clasificacion = clasificacion
        self.probabilidad = probabilidad


class PrediccionSchema(Schema):
    id = fields.UUID()
    resena = fields.Str()
    clasificacion = fields.Str()
    probabilidad = fields.Float()
    expireAt = fields.DateTime()
    createdAt = fields.DateTime()


class CreatedPrediccionJsonSchema(Schema):
    resena = fields.Str()
    clasificacion = fields.Str()
    probabilidad = fields.Float()
    createdAt = fields.DateTime()


class PrediccionJsonSchema(Schema):
    id = fields.UUID()
    resena = fields.Str()
    clasificacion = fields.Str()
    probabilidad = fields.Float()