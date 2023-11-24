from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to (self):
        self.driver.get(SignInPage.URL)

    def try_login (self, username, passwor):
        #Incorrect login input
        login = self.driver.find_element(By.ID, "login_field")
        login.send_keys(username)

        #Input password incorrect 
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(passwor)

        #Push buton sing in
        sing_in = self.driver.find_element(By.NAME, "commit")
        sing_in.click()

    def check_title(self, exepected_title):
        return self.driver.title == exepected_title