from sql import Base, session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class RolesModel(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True)
    role = Column(String)

    usuario = relationship('UsuarioModel', backref='roles_user', lazy=True)

    def __init__(self, role):
        self.role = role

    def json(self):
            return {
                'role_id' : self.role_id,
                'role' : self.role
            }

    def initial_data(*args, **kargs):
        role_user = RolesModel(role="USER_ROLE")
        role_admin = RolesModel(role="ADMIN_ROLE")
        session.add(role_user)
        session.add(role_admin)
        session.commit()

    def find_all():
        roles = []
        for role in session.query(RolesModel).all():
            roles.append(role.json())
        return roles