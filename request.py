import requests
from bs4 import BeautifulSoup
import csv
my_url = {}
url = "https://eu.puma.com/fr/fr/homme/chaussures/baskets"



def request(urls):
    for u in url:
        reponse = requests.get(urls)
        soup = BeautifulSoup(reponse.text, 'html.parser')

        categorie_soup = soup.findAll(
            "h1", {"class": "row product-grid no-gutters"})
        categorie = categorie_soup[0].text
        my_url.update({categorie: u})
    print('my_url ', my_url)


if __name__ == '__main__':
    request(url)
