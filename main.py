import requests
import pandas

from sys import argv
from json import load
from os import getenv
from dotenv import load_dotenv

from domain.contract_service import parse_df, save

load_dotenv()

FILE_NAME = "resp.json"
URL = getenv("URL")


def fetch_data(url, retries=0, err=None):
    if retries > 2:
        raise (err)

    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.Timeout as e:
        print("timeout, retrying...")
        fetch_data(url, retries + 1, e)
    except requests.exceptions.HTTPError as e:
        raise SystemExit(e)

    file = open(FILE_NAME, "w")
    file.write(r.text)
    file.close()


def main():
    if any(opt in argv for opt in ["-f", "--fetch"]):
        fetch_data(URL)

    try:
        with open(FILE_NAME) as f:
            data_dict = load(f)
    except FileNotFoundError as e:
        print(
            "File: " + FILE_NAME + " not found, run with --fetch to send a get request"
        )
        raise SystemExit(e)

    df = pandas.DataFrame(data_dict["caged"])

    parse_df(df)
    save(df)


main()
