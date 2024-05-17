from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel
from secrets import compare_digest



body = reqparse.RequestParser()
body.add_argument('nome', type=str, required=True, help="O campo 'NOME' nao deve ser deixa em branco")
body.add_argument('email', type=str, required=True, help="O campo 'EMAIL' nao deve ser deixa em branco")
body.add_argument('cpf', type=str, required=True, help="O campo 'CPF' nao deve ser deixa em branco")
body.add_argument('senha', type=str, required=True, help="O campo 'SENHA' nao deve ser deixa em branco")
body.add_argument('confirmar_senha', type=str, required=True, help="O campo 'CONFIRMAR SENHA' nao deve ser deixa em branco")
body.add_argument('aluno', type=bool, required=True, help="Você deve colocar se é um aluno ou nao")

class Usuario(Resource):
    def get(self, usuario_id):
        usuario = UsuarioModel.find_user(usuario_id)
        if usuario:
            return usuario.json()
        return {'message' : 'Usuario nao encontrado'}, 404
    
class UsuarioRegistro(Resource):
    def post(self):
        dados = body.parse_args()
        if not UsuarioModel.valida_cpf(dados['cpf']):
            return {"message" : "Digite um CPF valido."}, 400
        
        if UsuarioModel.find_by_cpf(dados['cpf']):
            return {'message' : 'O usuario com esse CPF ja existe'}, 400
        
        if compare_digest(dados['senha'], dados['confirmar_senha']):
            del dados['confirmar_senha']
            if dados['aluno']:
                usuario = UsuarioModel(**dados, role_id=1)
                usuario.save()
            else:
                usuario = UsuarioModel(**dados, role_id=2)
                usuario.save()
            return {"message" : f"O usuario com o email '{usuario.email}' foi criado com sucesso!"}, 201


            
        return {'message' : 'As senhas nao coincidem'}, 400