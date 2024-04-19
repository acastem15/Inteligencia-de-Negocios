from .base_command import BaseCommannd
from ..models.prediccion import Prediccion, PrediccionSchema, CreatedPrediccionJsonSchema
from ..session import Session
from ..errors.errors import IncompleteParams
from joblib import load
import pandas as pd
import os


class CreatePrediccion(BaseCommannd):
    def __init__(self, data):
        self.data = data

    def load_model(self):
        path = os.path.join(os.path.dirname(__file__), 'assets/modelLemmatizer.joblib')
        model = load(path)
        try:
            return model
        except FileNotFoundError:
            raise FileNotFoundError("No se encontró el modelo en la ruta especificada")

    def execute(self):
        try:
            posted_prediccion_data = PrediccionSchema(
                only=('resena',)).load(self.data)

            df = pd.DataFrame(posted_prediccion_data, columns=posted_prediccion_data.keys(), index=[0])
            model = self.load_model()
            result = model.predict(df)
            
            session = Session()
            session.add(result)
            session.commit()

            new_prediccion = CreatedPrediccionJsonSchema().dump(result)
            session.close()

            return new_prediccion
        except TypeError:
            raise IncompleteParams()