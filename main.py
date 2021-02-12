import requests
import sys
import json


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

    file = open("resp.json", "w")
    file.write(r.text)
    file.close()


def main():
    if "-f" or "--fetch" in sys.argv:
        fetch_data("a real url :D")
    with open("resp.json") as f:
        data_dict = json.load(f)

    print(len(data_dict))


main()
