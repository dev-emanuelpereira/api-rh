from flask import request
from flask_restful import Resource, reqparse
from models.curriculo import CurriculoModel
from models.usuario import UsuarioModel

body = reqparse.RequestParser()
body.add_argument('nome', type=str, required=True, help="O campo 'NOME' nao deve ser deixa em branco")
body.add_argument('formacao', type=str, required=True, help="O campo 'FORMCAO' nao deve ser deixa em branco")
body.add_argument('area_atuacao', type=str, required=True, help="O campo 'AREA DE ATUACAO' nao deve ser deixa em branco")



class Curriculos(Resource):
    def get(self):
        return {'curriculos' : CurriculoModel.find_all()}, 200
    
class Curriculo(Resource):
    def get(self, curriculo_id):
        curriculo = CurriculoModel.find_curriculo(curriculo_id)
        if curriculo:
            return curriculo.json(), 200
        return {'message' : 'Curriculo nao encontrado'}, 404

class CurriculoRegistro(Resource):
    def post(self):
        dados = body.parse_args()
        usuario_id = request.args.get('usuario_id')

        if UsuarioModel.find_user(usuario_id):
            if CurriculoModel.find_curriculo_by_user(usuario_id):
               return {"message" : "Ja existe um curriculo para este usuario"}, 400

            curriculo = CurriculoModel(**dados, usuario_id=usuario_id)
            curriculo.save()
            return curriculo.json, 200
        return {"message" : "Nao existe um usuario com esse ID"}, 400
    
    def put(self):
        dados = body.parse_args()
        curriculo_id = request.args.get('curriculo_id')

        curriculo_encontrada = CurriculoModel.find_curriculo(curriculo_id)
        if curriculo_encontrada:
            curriculo_encontrada.update(**dados)
            curriculo_encontrada.save()
            return curriculo_encontrada.json(), 200
        
    def delete(self):
        curriculo_id = request.args.get('curriculo_id')
        curriculo_encontrada = CurriculoModel.find_curriculo(curriculo_id)

        if curriculo_encontrada:
            curriculo_encontrada.delete()
            return {'message' : 'Candidatura cancelada com sucesso'}, 200
        return {'message' : 'Nenhuma candidatura foi encontrada'}, 404