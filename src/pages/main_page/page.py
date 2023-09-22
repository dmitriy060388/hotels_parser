from base import BaseClass
from locators import MainPageLocators


class MainPage(BaseClass):

    def search_hotel(self):

        self._find_element(MainPageLocators.PLACE)
        self._click_visible_element(MainPageLocators.PLACE)
