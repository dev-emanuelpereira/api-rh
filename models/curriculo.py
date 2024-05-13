from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from models.roles import RolesModel
from sql import session, Base

class CurriculoModel(Base): 
    __tablename__ = 'curriculos'

    curriculo_id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=True)
    formacao = Column(String, nullable=True)
    area_atuacao = Column(String, nullable=True)

    def __init__(self, nome, formacao, area_atuacao):
        self.nome = nome
        self.formacao = formacao
        self.area_atuacao = area_atuacao

    def json(self):
            
            return {
                'curriculo_id' : self.curriculo_id,
                'nome' : self.nome,
                'formacao' : self.formacao,
                'area_atuacao' : self.area_atuacao
            }
     
    def find_curriculo(curriculo_id):
        curriculo = session.query(CurriculoModel).filter_by(curriculo_id=curriculo_id).first()
        if curriculo:
            return curriculo
        return None
    
    def save(self):
        try:
            session.add(self)
            session.commit()
        except:
            return {"message" : "Erro ao salvar no banco de dados"}