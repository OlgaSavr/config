from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class Search(BasePage):
    URL = "https://citrusdev.com.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to (self):
        self.driver.get(Search.URL)
    
    def search(self):
        sing_in = self.driver.find_element(By.CLASS_NAME, "popup-search-wrap")
        sing_in.click()

        write = self.driver.find_element(By.CLASS_NAME, "search-field")
        write.send_keys("test seaching\
                        ")
        
