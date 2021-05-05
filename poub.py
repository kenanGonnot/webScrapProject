from itertools import product

import request
import writeToCsv

import requests
from bs4 import BeautifulSoup

my_url = {}
url = "https://eu.puma.com/fr/fr/homme/chaussures/baskets"

reponse = requests.get(url)
soup = BeautifulSoup(reponse.text, 'html.parser')

# product_containers = soup.find_all({"class": "row product-grid no-gutters"})
 #
# product_title_containers = product_containers.find_all({"class": "product-tile-info-text"})
#
# product_price_containers = product_containers.find_all(
#     {"class": "product-tile-price-standard product-tile__price--standard"})
#
# dico_all_product = dict()
dico_prices = dict()

print(reponse.content[:100])

# print(product_price_containers.text)

#
# if __name__ == '__main__':
#     request.request(url)
#     writeToCsv.writeCSV()
#
