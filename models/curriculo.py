from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sql import session, Base




class CurriculoModel(Base): 
    __tablename__ = 'curriculos'

    curriculo_id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=True)
    formacao = Column(String, nullable=True)
    area_atuacao = Column(String, nullable=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.usuario_id'))

    def __init__(self, nome, formacao, area_atuacao, usuario_id):
        self.nome = nome
        self.formacao = formacao
        self.area_atuacao = area_atuacao
        self.usuario_id = usuario_id

    def json(self):
            
            return {
                'usuario_id' : self.usuario_id,
                'curriculo_id': self.curriculo_id,
                'nome': self.nome,
                'formacao': self.formacao,
                'area_atuacao': self.area_atuacao
            }
     
    def find_curriculo_by_user(usuario_id):
        curriculo = session.query(CurriculoModel).filter_by(usuario_id=usuario_id).first()
        if curriculo:
            return curriculo
        return None

    def find_all():
        curriculos = []
        for curriculo in session.query(CurriculoModel).all():
            curriculos.append(curriculo.json())
        return curriculos
    
    def save(self):
        try:
            session.add(self)
            session.commit()
        except:
            return {"message" : "Erro ao salvar no banco de dados"}