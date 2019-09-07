from selenium.webdriver.common.by import By

from base.base_action import BaseAction

class SearchPage(BaseAction):

    search_button = By.ID, "com.android.settings:id/search"

    # text_button = By.XPATH, "//*[contains(@text, 'Search…')]"
    text_button = By.XPATH, "text,Search…"

    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def click_search(self):
        self.click(SearchPage.search_button)

    def input_text(self, text):
        self.send_keys(SearchPage.text_button, text)

    def click_back(self):
        self.click(SearchPage.back_button)