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
        return {'curriculos' : CurriculoModel.find_all()}
    
class Curriculo(Resource):
    def get(self, curriculo_id):
        curriculo = CurriculoModel.find_curriculo(curriculo_id)
        if curriculo:
            return curriculo.json()
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
            return curriculo.json()
        return {"message" : "Nao existe um usuario com esse ID"}