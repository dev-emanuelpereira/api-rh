from flask_restful import Resource, reqparse
from models.vagas import VagasModel
from secrets import compare_digest

body = reqparse.RequestParser()
body.add_argument('nome_vaga', type=str, required=True, help="O campo 'NOME VAGA' nao deve ser deixa em branco")
body.add_argument('descricao', type=str, required=True, help="O campo 'DESCRICAO' nao deve ser deixa em branco")
body.add_argument('requisito_formacao', type=str, required=True, help="O campo 'REQUISITO FORMACAO' nao deve ser deixa em branco")
body.add_argument('salario', type=str, required=True, help="O campo 'SALARIO' nao deve ser deixa em branco")


class Vagas(Resource):
    def get(self):
        return {'vagas' : VagasModel.find_all()}
