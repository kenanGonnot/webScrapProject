from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from functions.utils import scroll, check_exists_by_classname, accept_pumas_cookies


def get_puma_shoes_list(url):
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(2)
    accept_pumas_cookies(driver)

    wait = WebDriverWait(driver, 15)

    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 150)")
    time.sleep(1)

    show_all_button = driver.find_element_by_xpath("//button[contains(text(), 'Voir Tout')]")
    show_all_button.click()
    time.sleep(1)

    scroll(wait, nbr_of_scroll=7, time_to_sleep=4)

    shoes = driver.find_elements_by_xpath("//div[@data-grid-tile-wrapper]")

    # shoes_name = driver.find_elements_by_class_name("product-tile-title")
    # shoes_price = driver.find_elements_by_class_name("product-tile-price-standard")

    extract_price_list_converted = extract_pumas_data(shoes)

    return extract_price_list_converted


def extract_pumas_data(shoes):
    shoes_list_filtered = filter(lambda x: check_exists_by_classname(x, "product-tile-title"), shoes)
    shoes_list_filtered = filter(lambda x: check_exists_by_classname(x, "product-tile-price-standard"),
                                 shoes_list_filtered)

    extract_price = lambda x: x.text
    convert_to_float = lambda x: float(x.replace(",", ".").replace("€", ""))
    # extract_price_list = list(map(extract_price, shoes_price))
    # extract_price_list_converted = list(map(convert_to_float, extract_price_list))

    convert_to_dict = lambda x: {"name": x.find_element_by_class_name("product-tile-title").text,
                                 "price": convert_to_float(
                                     extract_price(x.find_element_by_class_name("product-tile-price-standard")))}

    extract_price_list_converted = list(map(convert_to_dict, shoes_list_filtered))

    return extract_price_list_converted

if __name__ == '__main__':
    shoes = get_puma_shoes_list("https://eu.puma.com/fr/fr/homme/chaussures")
    print(shoes)
