from pages.base import BaseClass
from .locators import MainPageLocators
import time


class MainPage(BaseClass):

    def search_hotel(self):

        self._find_element(MainPageLocators.PLACE)
        self._click_visible_element(MainPageLocators.PLACE)
        time.sleep(100)
