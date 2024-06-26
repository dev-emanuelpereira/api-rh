from flask_restful import Resource, reqparse
from flask import request
from models.vagas import VagasModel
from models.usuario import UsuarioModel

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
        if vaga:
            return vaga, 200
        return {'message' : 'Este usuario nao criou vagas'}


class VagaRegistro(Resource):
    def post(self):
        dados = body.parse_args()
        usuario_id = request.args.get('usuario_id')

        vaga = VagasModel(**dados, usuario_id=usuario_id)
        vaga.save()
        return vaga.json(), 201
    
    def put(self):
        dados = body.parse_args()
        vaga_id = request.args.get('vaga_id')

        vaga_encontrada = VagasModel.find_vagas_by_id(vaga_id)
        if vaga_encontrada:
            vaga_encontrada.update(**dados)
            vaga_encontrada.save()
            return vaga_encontrada.json(), 200
        
    def delete(self):
        vaga_id = request.args.get('vaga_id')
        vaga_encontrada = VagasModel.find_vagas_by_id(vaga_id)

        if vaga_encontrada:
            vaga_encontrada.delete()
            return {'message' : 'Vaga deletada com sucesso'}, 200
        return {'message' : 'Nenhuma vaga foi encontrada'}, 404


    
