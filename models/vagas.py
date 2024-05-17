from sqlalchemy import Column, Integer, String, ForeignKey, Float
from models.usuario import UsuarioModel
from sql import session, Base


class VagasModel(Base):
    __tablename__ = 'vagas'

    usuario_id = Column(Integer, ForeignKey('usuarios.usuario_id'))
    vaga_id = Column(Integer, primary_key=True)
    nome_vaga = Column(String, nullable=True)
    descricao = Column(String, nullable=True)
    requisito_formacao = Column(String, nullable=True)
    salario = Column(Float, nullable=True)

    def __init__(self, nome_vaga, descricao, requisito_formacao, salario, usuario_id):
        self.nome_vaga = nome_vaga
        self.descricao = descricao
        self.requisito_formacao = requisito_formacao
        self.salario = salario
        self.usuario_id = usuario_id

    def json(self):
        return {
            'vaga_id': self.vaga_id,
            'nome_vaga': self.nome_vaga,
            'descricao': self.descricao,
            'requisito_formacao': self.requisito_formacao,
            'salario': self.salario    
        }
    
    def find_vagas_by_user(usuario_id):
        vagas = session.query(VagasModel).filter_by(usuario_id=usuario_id).all()

        vagas_por_usuario = {
                    'usuario_id' : usuario_id,
                    'vagas_criadas' : [vaga.json() for vaga in vagas] 
                }
        
        if len(vagas_por_usuario['vagas_criadas']) != 0:
            return vagas_por_usuario
        return None
    
    def find_all():
        usuarios = session.query(UsuarioModel).all()
        vagas = []

        for usuario in usuarios:
            if len(usuario.vagas) != 0:
                vagas_por_usuario = {
                    'usuario_id' : usuario.usuario_id,
                    'nome' : usuario.nome,
                    'vagas_criadas' : [vaga.json() for vaga in usuario.vagas] 
                }
                vagas.append(vagas_por_usuario)
        return vagas
        

    def save(self):
        session.add(self)
        session.commit()
