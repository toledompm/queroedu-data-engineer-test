from domain.city_entity import City
from db.config import session


def get_or_create_city(row):
    municipio = row["municipio"]
    regiao = row["regiao"]
    uf = row["uf"]

    resp = (
        session.query(City).filter_by(municipio=municipio, regiao=regiao, uf=uf).first()
    )

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

    resp = (
        session.query(City).filter_by(municipio=municipio, regiao=regiao, uf=uf).first()
    )

    return resp
