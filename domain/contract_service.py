from decimal import Decimal
from locale import setlocale, delocalize, LC_NUMERIC
from sqlalchemy.sql.sqltypes import CHAR, Integer, Numeric
from domain.city_service import get_or_create_city
from db.contract_entity import Contract

from db.config import session

setlocale(LC_NUMERIC, "en_US.utf8")


def parse_df(dataframe):
    for col_name, callback in __parse_options__():
        dataframe[col_name] = dataframe[col_name].apply(callback)


def save(dataframe):
    dataframe.apply(__save_row__, axis=1)


def __save_row__(row):
    city = get_or_create_city(row)
    row["city_id"] = city.city_id
    contract_instance = Contract(row)

    try:
        session.add(contract_instance)
        session.commit()
    except Exception as err:
        input()
        with open("err.txt", "a") as f:
            f.write(
                "Error saving contract instance: "
                + contract_instance.to_string()
                + " - "
                + str(err)
            )
        session.rollback()


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


def __string_to_decimal_with_locale__(string):
    return Decimal(delocalize(string))
