from sqlalchemy import Column, Integer, String, ForeignKey
from models.roles import RolesModel
from sql import session, Base


class VagasModel(Base):
    __tablename__ = 'vagas'

    usuario_id = Column(Integer, ForeignKey('usuarios.usuario_id'))
    vaga_id = Column(Integer, primary_key=True)
    nome_vaga = Column(String, nullable=True)
    descricao = Column(String, nullable=True)
    requisito_formacao = Column(String, nullable=True)
    salario = Column(String, nullable=True)

    def __init__(self, nome_vaga, descricao, requisito_formacao, salario):
        self.nome_vaga = nome_vaga
        self.descricao = descricao
        self.requisito_formacao = requisito_formacao
        self.salario = salario

    def json(self):

        return {
            'usuario_id': self.vaga_id,
            'vagas' : [vaga.json() for vaga in session.query(VagasModel).filter_by(usuario_id=self.usuario_id).all()]
            
        }

    def find_all():
        vagas = []
        for vaga in session.query(VagasModel).all():
            vagas.append(vaga.json())
        return vagas

    def save(self):
        session.add(self)
        session.commit()
