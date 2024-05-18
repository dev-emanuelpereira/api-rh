from flask_restful import Resource, reqparse
from flask import request
from models.candidato import CandidatoModel
from models.curriculo import CurriculoModel

body = reqparse.RequestParser()
body.add_argument('usuario_id', type=int, required=True, help="O campo 'USUARIO ID' nao deve ser deixa em branco")
body.add_argument('vaga_id', type=int, required=True, help="O campo 'VAGA ID' nao deve ser deixa em branco")
body.add_argument('inscrever', type=bool, required=True, help="O campo 'INSCREVER' nao deve ser deixa em branco")

class Candidato(Resource):

    def get(self):
        usuario_id = request.args.get('usuario_id')
        vaga_id = request.args.get('vaga_id')

        if usuario_id is None or vaga_id is None:
            return {'message' : 'Verifique se todos os parametros estao senso passados corretamente'}
        candidatura = CandidatoModel.find_vaga_by_user_and_vaga(usuario_id, vaga_id)
        if candidatura:
            return candidatura.json(), 200
        return {'message' : 'Nao existe uma candidatura deste usuario para esta vaga'}
    
    def post(self):
        dados = body.parse_args()

        if CandidatoModel.find_vaga_by_user_and_vaga(dados['usuario_id'], dados['vaga_id']):
            return {'message' : 'Este usuario ja se inscreveu nesta vaga'}, 400
        if CandidatoModel.find_vaga_by_user(dados['usuario_id']):
            return {'message' : 'Este usuario ja esta inscrito em outra vaga'}, 400
        if not CurriculoModel.find_curriculo_by_user(dados['usuario_id']):
            return {'message' : 'Este usuario nao possui um curriculo'}, 404
        
        candidatura = CandidatoModel(dados['usuario_id'], dados['vaga_id'], dados['inscrever'])
        candidatura.save()
        return candidatura.json(), 201
    
    def put(self):
        dados = body.parse_args()

        candidatura_encontrada = CandidatoModel.find_vaga_by_user(dados['usuario_id'])
        if candidatura_encontrada:
            candidatura_encontrada.update(**dados)
            candidatura_encontrada.save()
            return candidatura_encontrada.json(), 200
        
    def delete(self):
        dados = body.parse_args()

        candidatura_encontrada = CandidatoModel.find_vaga_by_user(dados['usuario_id'])
        if candidatura_encontrada:
            candidatura_encontrada.delete()
            return {'message' : 'Candidatura cancelada com sucesso'}, 200
        return {'message' : 'Nenhuma candidatura foi encontrada'}, 404








