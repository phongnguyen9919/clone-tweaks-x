import time
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TwitterLogin:
    def __init__(self, driver, username, password, cookie_file):
        self.driver = driver
        self.username = username
        self.password = password
        self.cookie_file = cookie_file

    def login(self):
        self.driver.get("https://twitter.com/login")

        # Wait for the username input to appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )

        # Find and enter username
        username_input = self.driver.find_element(By.NAME, "text")
        username_input.send_keys(self.username)
        username_input.send_keys(Keys.RETURN)

        # Wait for the password input to appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        # Find and enter password
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)

        # Wait for login to complete (e.g., wait for the home page to load)
        time.sleep(10)

        # Save cookies after login
        self.save_cookies()

    def save_cookies(self):
        with open(self.cookie_file, "wb") as file:
            pickle.dump(self.driver.get_cookies(), file)
        print("Login successful and cookies saved!")