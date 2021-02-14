from decimal import Decimal
from domain.city_service import find_or_save_city
from locale import setlocale, delocalize, LC_NUMERIC
from sqlalchemy.sql.sqltypes import CHAR, Integer, Numeric

from db.config import Engine

setlocale(LC_NUMERIC, "en_US.utf8")

CHUNK_SIZE = 500


def parse_df(dataframe):
    for col_name, callback in __parse_options__():
        dataframe[col_name] = dataframe[col_name].apply(callback)


def save_entities(dataframe):
    dataframe.apply(__save_row__)
    print(dataframe["city_id"])


def __save_row__(row):
    row["city_id"] = find_or_save_city(
        municipio=row["municipio"], regiao=row["regiao"], uf=row["uf"]
    )


def __parse_options__():
    return [
        ("regiao", int),
        ("municipio", int),
        ("uf", int),
        ("cbo2002_ocupacao", int),
        ("subclasse", int),
        ("tipo_estabelecimento", int),
        ("tam_estab_jan", int),
        ("salario", __string_to_decimal_with_locale__),
        ("horas_contratuais", int),
        ("tipo_empregador", int),
        ("ind_trab_intermitente", int),
        ("ind_trab_parcial", int),
        ("indicador_aprendiz", int),
        ("fonte", int),
        ("idade", int),
        ("raca_cor", int),
        ("sexo", int),
        ("tipo_de_deficiencia", int),
        ("grau_de_instrucao", int),
        ("competencia", int),
        ("tipo_movimentacao", int),
        ("saldo_movimentacao", int),
    ]


def __postgres_data_types__():
    return {
        "regiao": Integer,
        "municipio": Integer,
        "uf": Integer,
        "cbo2002_ocupacao": Integer,
        "categoria": Integer,
        "secao": CHAR,
        "subclasse": Integer,
        "tipo_estabelecimento": Integer,
        "tam_estab_jan": Integer,
        "salario": Numeric,
        "horas_contratuais": Integer,
        "tipo_empregador": Integer,
        "ind_trab_intermitente": Integer,
        "ind_trab_parcial": Integer,
        "indicador_aprendiz": Integer,
        "fonte": Integer,
        "idade": Integer,
        "raca_cor": Integer,
        "sexo": Integer,
        "tipo_de_deficiencia": Integer,
        "grau_de_instrucao": Integer,
        "competencia": Integer,
        "tipo_movimentacao": Integer,
        "saldo_movimentacao": Integer,
    }


def __string_to_decimal_with_locale__(string):
    return Decimal(delocalize(string))
