from bs4 import BeautifulSoup
import requests

"""
    Get real time positions from the teams in the Brasileirao Serie A championship.
"""

color_dict = {0:"32",1:"34",2:"34",3:"34",16:"31",17:"31",18:"31",19:"31"}

def make_soup():
    url = "https://globoesporte.globo.com/futebol/brasileirao-serie-a/"
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")
    return soup

def get_teams(soup):
    lst = soup.select(".tabela-times-time-nome")
    return lst

def get_points(soup):
    lst = soup.select(".tabela-pontos-ponto")
    return lst

def display_output(teams, points):
    print("{:<10} {:<15} {:>10}".format("Pos.","Team", "Points"))
    print(""+"="*37+"\n")
    for team in range(len(teams)):
        if team in color_dict:
            print("\033[1;"+color_dict[team]+"m{:<10} {:<15} {:>10}\033[0m\n".format(team+1, teams[team].text, points[team].text))
        else:
            print("\033[1;97m{:<10} {:<15} {:>10}\033[0m\n".format(team+1, teams[team].text, points[team].text))

def main():
    soup = make_soup()
    teams = get_teams(soup)
    points = get_points(soup)
    display_output(teams, points)
    
if __name__ == '__main__':
    main()