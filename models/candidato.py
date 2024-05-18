from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sql import session, Base

class CandidatoModel(Base):
    __tablename__ = 'canditatos'

    candidatura_id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.usuario_id"), nullable=True)
    vaga_id = Column(Integer, ForeignKey("vagas.vaga_id"), nullable=True)
    inscrito = Column(Boolean, nullable=True, default=False)

    def __init__(self, usuario_id, vaga_id, inscrever):
        self.usuario_id = usuario_id
        self.vaga_id = vaga_id
        self.inscrito = inscrever

    def json(self):
        return {
            'candidatura_id' : self.candidatura_id,
            'usuario_id' : self.usuario_id,
            'vaga_id' : self.vaga_id,
            'inscrito' : self.inscrito
        }

    def find_vaga_by_user_and_vaga(usuario_id, vaga_id):
        vaga = session.query(CandidatoModel).filter_by(usuario_id=usuario_id, vaga_id=vaga_id).first()
        if vaga:
            return vaga
        return None
    
    def find_vaga_by_user(usuario_id):
        vaga = session.query(CandidatoModel).filter_by(usuario_id=usuario_id).first()
        if vaga:
            return vaga
        return None
    
    def find_candidatura_by_id(candidatura_id):
        candidatura = session.query(CandidatoModel).filter_by(candidatura_id=candidatura_id).first()
        if candidatura:
            return candidatura
        return None

    def save(self):
        try:
            session.add(self)
            session.commit()
        except:
            return {"message" : "Erro ao salvar"}, 500
        
    def update(self, usuario_id, vaga_id, inscrever):
        self.usuario_id = usuario_id
        self.vaga_id = vaga_id
        self.inscrito = inscrever

    def delete(self):
        try:
            session.delete(self)
            session.commit()
        except:
            return {'message' : 'Nao foi possivel deletar a candidatura'}, 500
    