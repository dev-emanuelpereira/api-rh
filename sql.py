from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///banco.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()