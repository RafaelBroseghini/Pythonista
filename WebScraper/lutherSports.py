import requests
from bs4 import BeautifulSoup

def get_sports_page():
    url = "http://www.luther.edu/sports/"
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")
    lst = soup.select(".list > ul > li > ul > li > a")
    return lst

def get_sports_from_page(men_or_women, lst):
    for elem in lst:
        elem = elem.get("href")
        if men_or_women in elem:
            url = "http://www.luther.edu"+elem
            data = requests.get(url).text
            soup = BeautifulSoup(data, "html.parser")
            all_sports = soup.find_all("h4")
            return all_sports

def print_sports(sex,lst):
    print("{:^70}".format(sex))
    print("-"*70+"\n")
    for elem in lst:
        print("{:^70}\n".format(elem.text))

def choose_sex():
    print("\nHey there! Glad to have you here! Let's find out Sports for a chosen sex @ Luther College!\n")
    print("Option 1: Men's")
    print("Option 2: Women's\n")
    selected = 0
    found = False
    while not found:
        selected = int(input("Choose 1 or 2 to see their respective sports at Luther College: "))
        print()
        if selected == 1:
            return "Men's sports at Luther College",selected
        elif selected == 2:
            return "Women's sports at Luther College", selected
        else:
            print("{} is not supported: Choose either 1 or 2".format(selected))

def selected_sport(inp):
    if inp == 1:
        return "/sports/men"
    elif inp == 2:
        return "/sports/women"
    else:
        return "Not supported"

def main():
    selected_inp_num = choose_sex()
    selected_sex = selected_sport(selected_inp_num[1])
    sports_page = get_sports_page()
    all_sports = get_sports_from_page(selected_sex, sports_page)
    print_sports(selected_inp_num[0],all_sports)

if __name__ == "__main__":
    main()
