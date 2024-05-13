from flask_restful import Resource
from models.roles import RolesModel

class Roles(Resource):
    def get(self):
        return {'message' : RolesModel.find_all()}, 200