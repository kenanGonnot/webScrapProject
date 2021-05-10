from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def scroll(wait, nbr_of_scroll=1, time_to_sleep=5):
    for _ in range(nbr_of_scroll):
        print("scroll")
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(time_to_sleep)


def accept_pumas_cookies(driver):
    driver.execute_script(
        "document.getElementsByTagName('puma-cookie-banner')[0].shadowRoot.querySelector('.btn').click()")


def accept_nike_cookies(driver):
    nike_button = driver.find_element_by_class_name('pre-cookie-modal-body')
    nike_cookies_button = nike_button.find_element_by_class_name("ncss-btn-primary-dark")
    nike_cookies_button.click()


def check_exists_by_classname(element, classname):
    try:
        element.find_element_by_class_name(classname)
    except NoSuchElementException:
        return False
    return True
