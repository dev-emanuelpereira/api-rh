from flask_restful import Resource, reqparse
from models.curriculo import CurriculoModel

body = reqparse.RequestParser()
body.add_argument('nome', type=str, required=True, help="O campo 'NOME' nao deve ser deixa em branco")
body.add_argument('formacao', type=str, required=True, help="O campo 'FORMCAO' nao deve ser deixa em branco")
body.add_argument('area_atuacao', type=str, required=True, help="O campo 'AREA DE ATUACAO' nao deve ser deixa em branco")

class Curriculo(Resource):
    def get(self, curriculo_id):
        curriculo = CurriculoModel.find_curriculo(curriculo_id)
        if curriculo:
            return curriculo.json()
        return {'message' : 'Curriculo nao encontrado'}, 404

class CurriculoRegistro(Resource):
    def post(self):
        body.parse_args()
        # if CurriculoModel.find_curriculo():
        #     return {"message" : "Ja existe um curriculo"}, 400
        
        curriculo = CurriculoModel(**body)
        curriculo.save()
        return curriculo.json()