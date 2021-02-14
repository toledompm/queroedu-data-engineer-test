from sqlalchemy import Column, Integer, CHAR

from db.config import Base


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True)
    regiao = Column(Integer)
    municipio = Column(Integer)
    uf = Column(Integer)
    cbo2002_ocupacao = Column(Integer)
    subclasse = Column(Integer)
    tipo_estabelecimento = Column(Integer)
    tam_estab_jan = Column(Integer)
    salario = Column(Integer)
    horas_contratuais = Column(Integer)
    tipo_empregador = Column(Integer)
    ind_trab_intermitente = Column(Integer)
    ind_trab_parcial = Column(Integer)
    indicador_aprendiz = Column(Integer)
    fonte = Column(Integer)
    idade = Column(Integer)
    raca_cor = Column(Integer)
    sexo = Column(Integer)
    tipo_de_deficiencia = Column(Integer)
    grau_de_instrucao = Column(Integer)
    competencia = Column(Integer)
    tipo_movimentacao = Column(Integer)
    saldo_movimentacao = Column(Integer)
    secao = Column(CHAR)
    city_id = Column(Integer)

    def __init__(self, row):
        self.id = row["id"]
        self.regiao = row["regiao"]
        self.municipio = row["municipio"]
        self.uf = row["uf"]
        self.cbo2002_ocupacao = row["cbo2002_ocupacao"]
        self.subclasse = row["subclasse"]
        self.tipo_estabelecimento = row["tipo_estabelecimento"]
        self.tam_estab_jan = row["tam_estab_jan"]
        self.salario = row["salario"]
        self.horas_contratuais = row["horas_contratuais"]
        self.tipo_empregador = row["tipo_empregador"]
        self.ind_trab_intermitente = row["ind_trab_intermitente"]
        self.ind_trab_parcial = row["ind_trab_parcial"]
        self.indicador_aprendiz = row["indicador_aprendiz"]
        self.fonte = row["fonte"]
        self.idade = row["idade"]
        self.raca_cor = row["raca_cor"]
        self.sexo = row["sexo"]
        self.tipo_de_deficiencia = row["tipo_de_deficiencia"]
        self.grau_de_instrucao = row["grau_de_instrucao"]
        self.competencia = row["competencia"]
        self.tipo_movimentacao = row["tipo_movimentacao"]
        self.saldo_movimentacao = row["saldo_movimentacao"]
        self.secao = row["secao"]
        self.city_id = row["city_id"]

    def to_string(self):
        return str(self.id)