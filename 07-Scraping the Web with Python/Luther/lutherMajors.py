import requests
from bs4 import BeautifulSoup

url = "http://www.luther.edu/academics/"
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")
lst = soup.select("strong > a")


def main():
    print("{}".format("-----Majors at Luther College-----\n"))
    print("Total Majors:{:>19}\n".format(len(lst)))
    for elem in range(0, len(lst)):
        print("{}:{:>30}\n".format(elem + 1, lst[elem].get("title")))


if __name__ == "__main__":
    main()
