from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class Write_and_send(BasePage):
    URL = "https://dream-school.ispringlearn.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to (self):
        self.driver.get(Write_and_send.URL)

    def write(self, login, paasord):

        my_lastname = self.driver.find_element(By.NAME, "login")
        my_lastname.send_keys(login)

        my_name = self.driver.find_element(By.NAME, "password")
        my_name.send_keys(paasord)

    def send(self):
        my_send = self.driver.find_element(By.CLASS_NAME, "submit_button")
        my_send.click()

    def check_title(self, exepected_title):
        return self.driver.title == exepected_title