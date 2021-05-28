from sqlalchemy import create_engine
from sqlalchemy.engine import base

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///mundial2018.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class mundial(Base):
    __tablename__ = 'mundial2018'
    
    id = Column(Integer, primary_key=True)
    numero = Column(String)
    fifaDis = Column(String)
    country = Column(String)
    lastName = Column(String)
    firstName = Column(String)
    shirtName = Column(String)
    pos = Column(String)
    height = Column(Integer)
    caps = Column(Integer)
    goals = Column(Integer)
    def _repr_(self):
        return "mundial: numero=%s FIFADisplayName=%s country=%s lastName=%s firstName=%s shirtName=%s POS=%s height=%d caps=%d goals=%d" % (
                          self.numero,
                          self.fifaDis,
                          self.country,
                          self.lastName,
                          self.firstName,
                          self.shirtName,
                          self.pos,
                          self.height,
                          self.caps, 
                          self.goals)

Base.metadata.create_all(engine)
