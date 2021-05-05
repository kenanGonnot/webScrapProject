import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scroll(wait, nbr_of_scroll=1, time_to_sleep=5):
    for _ in range(nbr_of_scroll):
        print("scroll")
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(time_to_sleep)


def get_puma_price_list(url):
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(2)

    driver.execute_script(
        "document.getElementsByTagName('puma-cookie-banner')[0].shadowRoot.querySelector('.btn').click()")

    wait = WebDriverWait(driver, 15)


    # time.sleep(2)
    # driver.execute_script("window.scrollTo(0, 150)")
    # scroll(wait)
    #
    show_all_button = driver.find_element_by_xpath("//button[contains(text(), 'Voir Tout')]")
    show_all_button.click()
    elem = driver.find_element_by_name("body")
    elem.send_keys(Keys.END)
    # nbr_of_scroll = 9
    scroll(wait,3)

    shoes = driver.find_elements_by_xpath("//div[@data-grid-tile-wrapper]")
    # shoes_name = driver.find_elements_by_class_name("product-tile-title")
    # shoes_price = driver.find_elements_by_class_name("product-tile-price-standard")

    extract_price_list_converted = extract_data(shoes)

    return extract_price_list_converted


def extract_data(shoes):
    # print(shoes[0].find_element_by_class_name("product-tile-title").text)
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


def check_exists_by_classname(element, classname):
    try:
        element.find_element_by_class_name(classname)
    except NoSuchElementException:
        return False
    return True


def get_commentary_and_date(list):
    name_text_list = []
    date_text_list = []
    comment_text_list = []
    like_nbr_list = []
    # print(name, "\n", date, "\n", commentary, "\n", like_nbr, "\n")

    for comment in list:
        text_list = comment.split('\n')
        if len(text_list) < 4: continue
        text_list = text_list[:-1]
        name = text_list[0]
        date = text_list[1]
        comment = "|".join(text_list[2:-1])
        like_nbr = text_list[-1]
        name_text_list.append(name)
        date_text_list.append(date)
        comment_text_list.append(comment)
        like_nbr_list.append(like_nbr)
    dict = {'name': name_text_list, 'date': date_text_list, 'comment': comment_text_list, 'like': like_nbr_list}

    return dict


if __name__ == "__main__":
    url = "https://eu.puma.com/fr/fr/homme/chaussures"
    # price_women_list = get_puma_price_list("https://eu.puma.com/fr/fr/femme/chaussures")
    price_men_list = get_puma_price_list("https://eu.puma.com/fr/fr/homme/chaussures")
    # print(price_men_list)

    df = pd.DataFrame(data=price_men_list)
    print(df)
    df.to_csv("puma-men.csv")
