from bs4 import BeautifulSoup
import random, requests, re, datetime, time

TODAY = datetime.date.today()

def make_soup():
    url = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a#.Ww4ABXUvw5l"
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")
    return soup

def get_games(soup):
    lst = soup.select("div.swiper-slide.active > div > ul > li > div > .clearfix > a > div > img")
    return lst

def get_dates(soup):
    pattern = re.compile(r"\d+\/\d+\/\d+")
    dates = []
    lst = soup.select("div.swiper-slide.active > div > ul > li > div > span.p-b-15")
    for d in lst:
        d = re.sub(r"\s+"," ", d.text)
        match = pattern.search(d)
        dates.append(match.group())
    date = dates[-1].split("/")
    date = datetime.date(int(date[2]),int(date[1]),int(date[0]))
    return date

def get_rodada(soup):
    lst = soup.select("div.swiper-slide.active > header > h3")
    return "{} - Campeonato Brasileiro".format(lst[0].text)

def write_to_file(lst):
    with open("brasileiraoGames.txt", "w") as file:
        for g in range(len(lst)-1):
            file.write("{:^30} \033[1;34mX\033[1;33m {:^30}\033[0m|\n"
            .format(lst[g].get("title"), lst[g+1].get("title")))

def read_from_file():
    with open("brasileiraoGames.txt") as file:
        for line in file:
            print("\033[1;32m"+line+"\033[0m")

def main():
    start = time.time()
    soup = make_soup()
    threshold = get_dates(soup)
    """ threshold is the last game date for "Rodada". If less than TODAY we must scrape the page again and write to file. 
    else we read from file."""

    print("\n\033[1;35m{:^60}\033[0m".format(get_rodada(soup)))
    print("-"*64)
    if threshold < TODAY:
        games = get_games(soup)
        write_to_file(games)
        read_from_file()
    else:
        read_from_file()
        
    end = time.time()
    print("-"*64)
    print("Finished in: {:.4f}s".format(end-start))

if __name__ == '__main__':
    main()