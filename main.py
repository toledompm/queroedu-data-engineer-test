import requests
import pandas

from sys import argv
from json import load
from os import getenv
from dotenv import load_dotenv

load_dotenv()

FILE_NAME = "res.json"
URL = getenv("URL")


def fetch_data(url, retries=0):
    if retries > 2:
        raise ("Err, too many retries")

    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.Timeout:
        print("timeout, retrying...")
        fetch_data(url, retries + 1)
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
        raise SystemExit()

    df = pandas.DataFrame(data_dict)
    print(len(df))


main()
