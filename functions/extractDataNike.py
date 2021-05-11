import requests
from bs4 import BeautifulSoup
import unicodedata


def get_nike_shoes_list(url):
    reponse = requests.get(url)
    #selenium scroll

    soup = BeautifulSoup(reponse.text, 'html.parser')

    shoes = soup.find_all('div', {"class": "product-card"})


    print(" =============== Extract Data =============== ")
    # name = "product-card__title"
    # price = "product-price"

    extract_price_list_converted = extract_nikes_data(shoes)
    return extract_price_list_converted


def extract_nikes_data(shoes):
    shoes_list_filtered = shoes

    extract_price = lambda x: x.get_text()
    convert_to_float = lambda x: float(x.replace(",", ".").replace("€", ""))
    normalize_text = lambda x: unicodedata.normalize("NFKD", x.get_text())

    convert_to_dict = lambda x: {"name": normalize_text(x.find('div', {"class": "product-card__title"})),
                                 "price": convert_to_float(
                                     extract_price(x.find('div', {"class": "product-price"})))}

    extract_price_list_converted = list(map(convert_to_dict, shoes_list_filtered))

    return extract_price_list_converted


# def check_exists_by_classname(element, classname):
#     try:
#         element.find('div', {"class": classname})
#     except NoSuchElementException:
#         return False
#     return True


if __name__ == '__main__':
    shoes = get_nike_shoes_list("https://www.nike.com/fr/w/femmes-chaussures-5e1x6zy7ok")
    print(len(shoes))
