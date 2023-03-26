from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DogModel(Base):
    __tablename__ = 'dog'
    id = Column(Integer, primary_key=True, autoincrement=True,)
    breed = Column(String(20))
    color = Column(String(10))

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def __repr__(self):
        return "<Dog('%s', '%s')>" % (self.breed, self.color)
