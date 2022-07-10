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
    # pprint(check_every_links_data(new_url))
    # pprint(check_parties_votes(new_url))
    # pprint(create_table_data(url, new_url))
    create_csv_file(url, new_url, file)
    print(f"Save to file {file}.")


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


def arguments():
    if len(sys.argv) != 3:
        print(f"The script {sys.argv[0]} needs input two arguments.")
        quit()
    elif sys.argv[1] not in get_district_links():
        print("The first argument must be URL of the scraping city in quotes.")
    elif not sys.argv[2].endswith("csv"):
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
    name_data = soup.find_all("td", {"headers": re.compile("t*sb2")})
    codes = []
    names = []
    for code in code_data:
        code = code.find("a")
        codes.append(code.text)

    for name in name_data:
        if name.text == "-":
            continue
        else:
            names.append(name.text)
    return codes, names


def get_city_links(url):
    request = requests.get(url)
    soup = BS(request.text, "html.parser")
    city_data = soup.find_all("td", {"class": "cislo"})
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
        valid_votes = new_soup.find("td", {"headers": "sa6"}).text
        voters_data.append(voters.replace("\xa0", ""))
        issued_envelopes_data.append(issued_envelopes.replace("\xa0", ""))
        valid_votes_data.append(valid_votes.replace("\xa0", ""))

    for party in new_soup.find_all("td", {"headers": re.compile("t*sb2")}):
        if party.text.isnumeric():
            continue
        else:
            candidate_parties.append(party.text)

    return voters_data, issued_envelopes_data, valid_votes_data, candidate_parties


def check_parties_votes(new_url):
    parties_votes_data = []

    for link in new_url:
        new_request = requests.get(link)
        new_soup = BS(new_request.text, "html.parser")
        votes = new_soup.find_all("td", {"headers": re.compile("t*sb3")})
        parties_votes_data.append(votes)

    for i in range(len(parties_votes_data)):
        for j in range(len(parties_votes_data[i])):
            parties_votes_data[i][j] = parties_votes_data[i][j].text

    for x in parties_votes_data:
        del x[0]

    return parties_votes_data


def create_table_data(url, new_url):
    code = get_city_code_name(url)[0]
    name = get_city_code_name(url)[1]
    voters = check_every_links_data(new_url)[0]
    envelopes = check_every_links_data(new_url)[1]
    valid_votes = check_every_links_data(new_url)[2]
    party_votes = check_parties_votes(new_url)

    table = []
    for x in range(len(code)):
        row = [code[x], name[x], voters[x], envelopes[x], valid_votes[x]]

        for y in range(len(party_votes[x])):
            row.append(party_votes[x][y])
        table.append(row)

    return table


def create_csv_file(url, new_url, file):
    headline = ["Kód obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"]

    for parties in check_every_links_data(new_url)[3]:
        headline.append(parties)

    data = create_table_data(url, new_url)

    create_file = open(file, "w", newline="")
    writer = csv.writer(create_file)
    writer.writerow(headline)
    writer.writerows(data)
    create_file.close()


if __name__ == "__main__":
    main()