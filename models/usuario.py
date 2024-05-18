from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models.roles import RolesModel
from models.curriculo import CurriculoModel
from sql import session, Base

class UsuarioModel(Base): 
    __tablename__ = 'usuarios'

    usuario_id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=True)
    email = Column(String, nullable=True)
    cpf = Column(String, nullable=True)
    senha = Column(String, nullable=True)
    aluno = Column(Boolean, nullable=True)
    role_id = Column(Integer, ForeignKey('roles.role_id'))
    curriculo = relationship('CurriculoModel', backref='curriculo', lazy=True)
    vagas = relationship('VagasModel', backref='usuario', lazy=True)


    def __init__(self, nome, email, cpf, senha, aluno, role_id):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha
        self.aluno = aluno
        self.role_id = role_id

    def json(self):
            if self.aluno and self.curriculo:
                return {
                    'usuario_id' : self.usuario_id,
                    'email' : self.email,
                    'cpf' : self.cpf,
                    'aluno' : self.aluno,
                    'role' : session.query(RolesModel).filter_by(role_id=self.role_id).first().json(),
                    'curriculo' : session.query(CurriculoModel).filter_by(usuario_id=self.usuario_id).first().json()
                }
            return {
                    'usuario_id' : self.usuario_id,
                    'email' : self.email,
                    'cpf' : self.cpf,
                    'aluno' : self.aluno,
                    'role' : session.query(RolesModel).filter_by(role_id=self.role_id).first().json()
                }
     
    def find_user(usuario_id):
        usuario = session.query(UsuarioModel).filter_by(usuario_id=usuario_id).first()
        if usuario:
            return usuario
        return None
    
    def find_by_cpf(cpf):
        usuario = session.query(UsuarioModel).filter_by(cpf=cpf).first()
        if usuario:
            return usuario
        return None
    
    def find_by_id(usuario_id):
        usuario = session.query(UsuarioModel).filter_by(usuario_id=usuario_id).first()
        if usuario:
            return usuario
        return None
    
    def save(self):
        try:
            session.add(self)
            session.commit()
        except:
            return {'message' : 'Nao foi possivel salvar o usuario'}, 500
        
    def update(self, nome, email, cpf, senha, aluno):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha

    def delete(self):
        try:
            session.delete(self)
            session.commit()
        except:
            return {'message' : 'Nao foi possivel deletar o usuario'}, 500

    def valida_cpf(cpf):
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            return False
        if cpf == cpf[0] * 11:
            return False
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        digito1 = 11 - soma % 11
        if digito1 > 9:
            digito1 = 0
        if int(cpf[9]) != digito1:
            return False
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        digito2 = 11 - soma % 11
        if digito2 > 9:
            digito2 = 0
        if int(cpf[10]) != digito2:
            return False

        return True