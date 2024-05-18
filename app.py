from flask import Flask
from flask_restful import Api
from resource.usuario import Usuario
from resource.curriculo import Curriculo, CurriculoRegistro, Curriculos
from resource.vagas import Vagas, VagaRegistro, Vaga
from resource.roles import Roles
from resource.candidato import Candidato
from models.roles import RolesModel
from sql import engine, Base

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

#Roles
api.add_resource(Roles, '/roles')
#Usuarios
api.add_resource(Usuario, '/usuario')
#Curriculos
api.add_resource(Curriculos, '/curriculos')
api.add_resource(Curriculo, '/curriculo/<int:curriculo_id>')
api.add_resource(CurriculoRegistro, '/curriculo')
#Vagas
api.add_resource(Vagas, '/vagas')
api.add_resource(VagaRegistro, '/vaga')
api.add_resource(Vaga, '/vaga')
#Candidatar-se
api.add_resource(Candidato, '/candidato')

@app.before_request
def criar_banco():
    Base.metadata.create_all(engine)
    if not RolesModel.find_all():
        RolesModel.initial_data()

if __name__ == '__main__':
    app.run(debug=True)
