from sqlalchemy import Column, Integer

from db.config import Base


class City(Base):
    __tablename__ = "cities"

    city_id = Column(Integer, primary_key=True)
    municipio = Column(Integer)
    regiao = Column(Integer)
    uf = Column(Integer)

    def __init__(self, municipio, regiao, uf):
        self.municipio = municipio
        self.regiao = regiao
        self.uf = uf
