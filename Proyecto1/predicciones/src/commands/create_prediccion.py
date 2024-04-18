from .base_command import BaseCommannd
from ..models.prediccion import Prediccion, PrediccionSchema, CreatedPrediccionJsonSchema
from ..session import Session
from ..errors.errors import IncompleteParams


class CreatePrediccion(BaseCommannd):
    def __init__(self, data):
        self.data = data

    def execute(self):
        try:
            posted_prediccion = PrediccionSchema(
                only=('resena', 'clasificacion', 'probabilidad')).load(self.data)
            prediccion = Prediccion(**posted_prediccion)
            session = Session()

            session.add(prediccion)
            session.commit()

            new_prediccion = CreatedPrediccionJsonSchema().dump(prediccion)
            session.close()

            return new_prediccion
        except TypeError:
            raise IncompleteParams()