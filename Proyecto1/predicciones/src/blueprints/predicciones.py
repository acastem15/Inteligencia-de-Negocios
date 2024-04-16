from flask import Flask, jsonify, request, Blueprint
from ..commands.create_prediccion import CreatePrediccion
from ..commands.reset import Reset

predicciones_blueprint = Blueprint('predicciones', __name__)


@predicciones_blueprint.route('/predicciones', methods=['POST'])
def create():
    model_path = 'Proyecto1/predicciones/src/assets/model.pkl'
    prediccion = CreatePrediccion(request.get_json(), model_path).execute()
    return jsonify(prediccion), 201


@predicciones_blueprint.route('/predicciones/ping', methods=['GET'])
def ping():
    return 'pong'


@predicciones_blueprint.route('/predicciones/reset', methods=['POST'])
def reset():
    Reset().execute()
    return jsonify({'status': 'OK'})