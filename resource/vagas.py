from flask_restful import Resource, reqparse
from flask import request
from models.vagas import VagasModel
from models.usuario import UsuarioModel
import json

body = reqparse.RequestParser()
body.add_argument('nome_vaga', type=str, required=True, help="O campo 'NOME VAGA' nao deve ser deixa em branco")
body.add_argument('descricao', type=str, required=True, help="O campo 'DESCRICAO' nao deve ser deixa em branco")
body.add_argument('requisito_formacao', type=str, required=True, help="O campo 'REQUISITO FORMACAO' nao deve ser deixa em branco")
body.add_argument('salario', type=float, required=True, help="O campo 'SALARIO' nao deve ser deixa em branco")


class Vagas(Resource):
    def get(self):
        return {'vagas' : VagasModel.find_all()}, 200

class Vaga(Resource):
    def get(self):
        usuario_id = request.args.get('usuario_id')
        if not UsuarioModel.find_user(usuario_id):
            return {'message' : 'Esse usuario nao existe'}
        vaga = VagasModel.find_vagas_by_user(usuario_id)
        return vaga, 200


class VagaRegistro(Resource):
    def post(self):
        dados = body.parse_args()
        usuario_id = request.args.get('usuario_id')

        vaga = VagasModel(**dados, usuario_id=usuario_id)
        vaga.save()
        return vaga.json(), 201


    
