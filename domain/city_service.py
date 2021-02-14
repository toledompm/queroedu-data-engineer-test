from domain.city_entity import City
from db.config import session
from domain.cache import custom_lru_cache


def get_or_create_city(row):
    municipio = row["municipio"]
    regiao = row["regiao"]
    uf = row["uf"]

    resp = __get_city_by_args__(municipio, regiao, uf)

    if resp:
        return resp
    city_instance = City(municipio, regiao, uf)

    try:
        session.add(city_instance)
        session.commit()
    except Exception as err:
        with open("err.txt", "a") as f:
            f.write(
                "Error saving city instance: " + city_instance.to_string() + " - " + err
            )
        session.rollback()
        return

    __get_city_by_args__.cache_remove(municipio, regiao, uf)
    resp = __get_city_by_args__(municipio, regiao, uf)
    return resp

@custom_lru_cache
def __get_city_by_args__(municipio, regiao, uf):
    return session.query(City).filter_by(
            municipio=municipio,
            regiao=regiao,
            uf=uf
        ).first()
