#!/usr/bin/env python

"""
I am curious as to how many times
LCMS has played some teams since 2011.

This python script will go into the 
LCMS page, iterate over the years and
put every team into a dictionary keeping
a count for repeated matches.
"""

from collections import Counter
import requests
from bs4 import BeautifulSoup


URL = "https://www.luther.edu/sports/men/soccer/schedule/"

headers = {"User-Agent": "Python Script"}
session = requests.Session()

source = session.get(URL, headers=headers).text
soup = BeautifulSoup(source, "html.parser")
all_games = Counter()

all_years = soup.find("form").find_all("option")

for year in all_years:
    past = session.post(URL, data={"season":year["value"]}).text
    new_soup = BeautifulSoup(past, "html.parser")
    all_teams = new_soup.find_all("td", class_="event")
    for team in all_teams:
        if team.text not in all_games:
            all_games[team.text] = 1
        else:
            all_games[team.text] += 1

with open("LCMS.txt", "w+") as outfile:
    outfile.write("{:<65} {}\n".format("Opponent", "Count"))
    for match in all_games.most_common():
        #using most_common() method of Counter for sorting.
        outfile.write("{:<65} {}\n".format(match[0], match[1]))




