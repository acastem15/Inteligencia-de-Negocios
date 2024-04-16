from .base_command import BaseCommannd
from ..models.prediccion import Prediccion, PrediccionSchema, CreatedPrediccionJsonSchema
from ..session import Session
from ..errors.errors import IncompleteParams
import joblib

class CreatePrediccion(BaseCommannd):
    def _init_(self, data, model_path):
        self.data = data
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        try:
            return joblib.load(self.model_path)
        except FileNotFoundError:
            raise FileNotFoundError("No se encontró el modelo en la ruta especificada")

    def execute(self):
        try:
            posted_prediccion_data = PrediccionSchema(
                only=('reseña',)).load(self.data)
            reseña_text = posted_prediccion_data['reseña']

            prediction = self.model.predict_proba([reseña_text])[0]
            clasificacion = prediction.argmax()
            probabilidad = prediction[clasificacion]

            prediccion = Prediccion(
                reseña=reseña_text,
                clasificacion=clasificacion,
                probabilidad=probabilidad
            )
            
            session = Session()
            session.add(prediccion)
            session.commit()

            new_prediccion = CreatedPrediccionJsonSchema().dump(prediccion)
            session.close()

            return new_prediccion
        except TypeError:
            raise IncompleteParams()