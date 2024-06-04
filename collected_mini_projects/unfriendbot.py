import os
import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

os.system("")
PROCESSOR = '\033[95m'  # Light pink
BLUE = '\033[94m'  # Blue
GREEN = '\033[92m'  # Green
YELLOW = '\033[93m'  # Yellow
FAIL = '\033[91m'  # Red
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

"""
    Not working . Issues related to cookies capturing.
"""

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set up WebDriver options
options = Options()
options.headless = False
driver = webdriver.Chrome(options=options)

# Account info
email = input("Enter your email: ")
password = input("Enter your password: ")
max_attempts = 5
attempts = 0
target = "https://www.facebook.com"

def login_to_facebook(driver, email, password):
    while driver.current_url != target:
        driver.get("https://www.facebook.com")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "pass"))).send_keys(password + Keys.RETURN)
        time.sleep(6)

def navigate_to_friends_section(driver):
    try:
        profile_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[href="https://www.facebook.com/profile.php?id=100014596003638"]'))
        )
        profile_link.click()

        friends_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[href="https://www.facebook.com/profile.php?id=100014596003638&sk=friends"]'))
        )
        friends_link.click()
        print("Successfully entered Friends section.")
    except Exception as e:
        logging.error(f"Error navigating to friends section: {e}")
        return False
    return True

def unfriend_perform(driver):
    try:
        friends_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Friends"][role="button"]'))
        )
        friends_button.click()

        menu_item = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[role="menuitem"][tabindex="-1"]'))
        )
        menu_item.click()

        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Confirm"]'))
        )
        confirm_button.click()
        time.sleep(4)
    except Exception as e:
        logging.error(f"Error performing friend actions: {e}")
        return False
    return True


while attempts < max_attempts:
    try:
        login_to_facebook(driver, email, password)
        print("Successfully logged in :)")
        time.sleep(3)
        driver.refresh()
        if navigate_to_friends_section(driver):
            while unfriend_perform(driver):
                pass
            logging.info("Successfully unfriended all in friend actions.")
            break
    except Exception as e:
        logging.error(f"Login attempt {attempts + 1} failed: {e}")
        attempts += 1
        if attempts >= max_attempts:
            logging.error("OVERLOADING ERR : TERMINATING . . . ")
            break
