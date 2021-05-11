import time
from functions.utils import check_exists_by_classname, accept_pumas_cookies, get_page


def get_puma_shoes_list(url):
    driver = get_page(url, accept_cookie_and_show_all)

    shoes_list = driver.find_elements_by_xpath("//div[@data-grid-tile-wrapper]")

    extract_price_list_converted = extract_pumas_data(shoes_list)

    driver.close()

    return extract_price_list_converted


def accept_cookie_and_show_all(driver, wait):
    accept_pumas_cookies(driver, wait)
    driver.execute_script("window.scrollTo(0, 150)")
    show_all_button = driver.find_element_by_xpath("//button[contains(text(), 'Voir Tout')]")
    show_all_button.click()
    time.sleep(2)


def extract_pumas_data(shoes_list):
    shoes_list_filtered = filter(lambda x: check_exists_by_classname(x, "product-tile-title"), shoes_list)
    shoes_list_filtered = filter(lambda x: check_exists_by_classname(x, "product-tile-price-standard"),
                                 shoes_list_filtered)

    extract_price = lambda x: x.text
    convert_to_float = lambda x: float(x.replace(",", ".").replace("€", ""))
    convert_to_dict = lambda x: {"name": x.find_element_by_class_name("product-tile-title").text,
                                 "price": convert_to_float(
                                     extract_price(x.find_element_by_class_name("product-tile-price-standard")))}

    extract_price_list_converted = list(map(convert_to_dict, shoes_list_filtered))

    return extract_price_list_converted


if __name__ == '__main__':
    shoes = get_puma_shoes_list("https://eu.puma.com/fr/fr/homme/chaussures")
    print(shoes)
    print(len(shoes))
