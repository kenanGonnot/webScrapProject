from bs4 import BeautifulSoup
import unicodedata
from functions.utils import accept_nike_cookies, get_page


def get_nike_shoes_list(url):
    source = get_page(url, accept_nike_cookies)

    soup = BeautifulSoup(source.page_source, 'html.parser')

    shoes_list = soup.find_all('div', {"class": "product-card"})

    print(" =============== Extract Data =============== ")

    extract_price_list_converted = extract_nikes_data(shoes_list)
    return extract_price_list_converted


def extract_nikes_data(shoes_list):
    extract_price = lambda x: x.get_text()
    convert_to_float = lambda x: float(x.replace(",", ".").replace("€", ""))
    normalize_text = lambda x: unicodedata.normalize("NFKD", x.get_text())

    convert_to_dict = lambda x: {"name": normalize_text(x.find('div', {"class": "product-card__title"})),
                                 "price": convert_to_float(
                                     extract_price(x.find('div', {"class": "product-price"})))}

    extract_price_list_converted = list(map(convert_to_dict, shoes_list))

    return extract_price_list_converted


if __name__ == '__main__':
    shoes = get_nike_shoes_list("https://www.nike.com/fr/w/femmes-chaussures-5e1x6zy7ok")
    print(shoes)
    print(len(shoes))
