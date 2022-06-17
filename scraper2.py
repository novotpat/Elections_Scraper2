"""
Elections Scraper.py: Třetí projekt do Engeto Online Python Akademie
author: Patrik Novotny
email: novotpat@gmail.com
discord: PatrikN#7617
"""
import re
import sys
import csv
from pprint import pprint

import requests
from bs4 import BeautifulSoup as BS


def main():
    url = arguments()[0]
    file = arguments()[1]


def get_city_links():
    url = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
    request = requests.get(url)
    soup = BS(request.text, "html.parser")
    city_data = soup.find_all("td", {"headers": re.compile("t*sa3")})
    front_link = "https://volby.cz/pls/ps2017nss/"
    city_links = []
    for link in city_data:
        rest_link = link.find("a")["href"]
        city_links.append(front_link + rest_link)
    return city_links


# pprint(get_city_links())


def arguments():
    if len(sys.argv) != 3:
        print(f"The script {sys.argv[0]} needs input two arguments.")
        quit()
    elif sys.argv[1] not in get_city_links() or not sys.argv[2].endswith(".csv"):
        print("The first argument must be URL of the scraping city in quotes.")
        print("The second argument must be the file name.")
        quit()
    else:
        url = sys.argv[1]
        file = sys.argv[2]
        print(f"Run the file {sys.argv[0]}.")
    return url, file


if __name__ == "__main__":
    main()