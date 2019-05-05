from sqlalchemy import create_engine, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
 
engine = create_engine('sqlite:///polyvisu.sqlite', echo=True)
Base = declarative_base(engine)

class Roadlink(Base):
    """"""
    __tablename__ = 'profiles_1h'
    __table_args__ = {'autoload':True, 'extend_existing':True}
    profile_id = Column(Integer, primary_key=True)
    time_stamp = Column(String, primary_key=True)

def loadSession():
    """"""
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

