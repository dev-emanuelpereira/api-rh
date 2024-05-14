import os
from flask import Flask
from flask_restful import Api
from resource.usuario import Usuario, UsuarioRegistro
from resource.curriculo import Curriculo, CurriculoRegistro, Curriculos
from models.roles import RolesModel
from resource.roles import Roles
from sql import engine, Base

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

#Roles
api.add_resource(Roles, '/roles')
#Usuarios
api.add_resource(Usuario, '/usuario/<int:usuario_id>')
api.add_resource(UsuarioRegistro, '/usuario')
#Curriculos
api.add_resource(Curriculos, '/curriculos')
api.add_resource(Curriculo, '/curriculo/<int:curriculo_id>')
api.add_resource(CurriculoRegistro, '/curriculo')

@app.before_request
def criar_banco():
    Base.metadata.create_all(engine)
    if not RolesModel.find_all():
        RolesModel.initial_data()

if __name__ == '__main__':
    app.run(debug=True)
