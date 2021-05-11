from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def scroll(wait, nbr_of_scroll=1, time_to_sleep=5):
    for _ in range(nbr_of_scroll):
        print("scroll")
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.PAGE_UP)
        time.sleep(time_to_sleep)


def get_page(url, acceptcookie):
    driver = webdriver.Firefox()
    driver.get(url)
    wait = WebDriverWait(driver, 15)

    acceptcookie(driver, wait)

    scroll(wait, nbr_of_scroll=7, time_to_sleep=4)

    return driver


def accept_pumas_cookies(driver):
    driver.execute_script(
        "document.getElementsByTagName('puma-cookie-banner')[0].shadowRoot.querySelector('.btn').click()")


def accept_nike_cookies(driver, wait):
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "pre-cookie-modal-body")))
    nike_button = driver.find_element_by_class_name('pre-cookie-modal-body')
    nike_cookies_button = nike_button.find_element_by_class_name("ncss-btn-primary-dark")
    nike_cookies_button.click()


def check_exists_by_classname(element, classname):
    try:
        element.find_element_by_class_name(classname)
    except NoSuchElementException:
        return False
    return True

