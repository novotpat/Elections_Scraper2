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
    # pprint(get_city_code_name(url))
    # pprint(get_city_links(url))
    new_url = get_city_links(url)
    pprint(check_every_links_data(new_url))


def get_district_links():
    url = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
    request = requests.get(url)
    soup = BS(request.text, "html.parser")
    district_data = soup.find_all("td", {"headers": re.compile("t*sa3")})
    front_link = "https://volby.cz/pls/ps2017nss/"
    district_links = []
    for link in district_data:
        rest_link = link.find("a")["href"]
        district_links.append(front_link + rest_link)
    return district_links


# pprint(get_district_links())


def arguments():
    if len(sys.argv) != 3:
        print(f"The script {sys.argv[0]} needs input two arguments.")
        quit()
    elif sys.argv[1] not in get_district_links() or not sys.argv[2].endswith(".csv"):
        print("The first argument must be URL of the scraping city in quotes.")
        print("The second argument must be the file name.")
        quit()
    else:
        url = sys.argv[1]
        file = sys.argv[2]
        print(f"Run the file {sys.argv[0]}.")
    return url, file


def get_city_code_name(url):
    request = requests.get(url)
    soup = BS(request.text, "html.parser")
    code_data = soup.find_all("td", {"class": "cislo"})
    name_data = soup.find_all("td", {"class": "overflow_name"})
    codes = []
    names = []
    for code in code_data:
        code = code.find("a")
        codes.append(code.text)

    for name in name_data:
        names.append(name.text)
    return codes, names


def get_city_links(url):
    request = requests.get(url)
    soup = BS(request.text, "html.parser")
    city_data = soup.find_all("td", {"headers": re.compile("t*sb1")})
    city_data = city_data[0:-2]
    front_link = "https://volby.cz/pls/ps2017nss/"
    city_links = []
    for link in city_data:
        rest_link = link.find("a")["href"]
        city_links.append(front_link + rest_link)
    return city_links


def check_every_links_data(new_url):
    voters_data = []
    issued_envelopes_data = []
    valid_votes_data = []

    candidate_parties = []

    for link in new_url:
        new_request = requests.get(link)
        new_soup = BS(new_request.text, "html.parser")
        voters = new_soup.find("td", {"headers": "sa2"}).text
        issued_envelopes = new_soup.find("td", {"headers": "sa3"}).text
        valid_votes = new_soup.find("td", {"headers": "sa6"})
        voters_data.append(voters)
        issued_envelopes_data.append(issued_envelopes)
        valid_votes_data.append(valid_votes.text)
    return valid_votes_data


if __name__ == "__main__":
    main()