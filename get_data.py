from bs4 import BeautifulSoup
import requests
import json


def update_data_countries():
    url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2_%D0%B8_%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D1%8B%D1%85_%D1%82%D0%B5%D1%80%D1%80%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B9_%D0%BF%D0%BE_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8E"

    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    countries_table = soup.find('table', class_='standard').find('tbody')
    all_countries = countries_table.findAll('tr')
    db = {}

    for row in all_countries[1:]:
        name = row.find('span', class_="wrap")
        population = row.find_all_next('td')[2].text.replace(" ", "")
        print(population)
        if name is None:
            name = row.find_all_next('a')[1]
        # print(name)
        db[name.text] = int(population.replace(" ", ""))

    with open("countries_population.json", "w", encoding="utf-8") as file:
        json.dump(db, file, indent=4, ensure_ascii=False)

    with open("countries_population.json", "r", encoding="utf-8") as file:
        db = json.load(file)
        print(db)

    # img_src = "https:" + row.find('img')["src"]
    # print(img_src)
    # if name is None:
    #     name = row.find_all_next('a')[1]
    # print(name.text, population)
    # print(row.find('span', class_="wrap"))
    # print(type(row))
    # print(type)
    # print(row.findAll('td'))
    # image_stream = requests.get(img_src)
    # with open(f"countries_flags/{name.text}.png", "wb") as image_file:
    #     for package in image_stream.iter_content(1024):
    #         image_file.write(package)