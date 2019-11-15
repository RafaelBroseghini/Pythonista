import requests
from bs4 import BeautifulSoup


def get_article(url):
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")
    lst = soup.select("#mp-tfa")
    return lst


def get_fun_facts(url):
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")
    lst = soup.select("#mp-dyk > ul > li")
    return lst


def get_picture(url):
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")
    lst = soup.select("#mp-tfp > table > tr > td > p ")
    title = soup.select("#mp-tfp > table > tr > td > p > b > a")
    return title, lst


def displayPictureInfo(title, lst):
    print(
        "\033[1;31mToday's Featured Picture on the Wikipedia (English) Main Page is: {} \033[0m\n".format(
            title[0].text
        )
    )
    print("\033[1;36mDescription:\033[0m\n")
    print(lst[0].text)


def displayFunFactsInfo(lst):
    print(
        "\033[1;31mToday's 'Did you know' questions on the Wikipedia (English) Main Page are: \033[0m\n"
    )
    print("\033[1;36mQuestions:\033[0m\n")
    for elem in lst:
        print(elem.text)
    print()


def displayArticleInfo(lst):
    print(
        "\033[1;31mToday's Featured Article on the Wikipedia (English) Main Page is: \033[0m\n"
    )
    print("\033[1;36mDescription:\033[0m\n")
    print(lst[0].text)


def main():
    url = "https://en.wikipedia.org/wiki/Main_Page"
    article = get_article(url)
    picture = get_picture(url)
    fun_facts = get_fun_facts(url)
    displayArticleInfo(article)
    displayFunFactsInfo(fun_facts)
    displayPictureInfo(picture[0], picture[1])


if __name__ == "__main__":
    main()
