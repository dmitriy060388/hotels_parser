from pages.base import BaseClass
from .locators import MainPageLocators
# from requirements import list_of_hotels
import time


class MainPage(BaseClass):

    def search_hotel(self, hotel, data):
        self.hotel = hotel
        self.data = data

        self._find_element(MainPageLocators.PLACE)
        self._click_visible_element(MainPageLocators.PLACE)
        self._send_keys(MainPageLocators.PLACE, data)
        self._click_visible_element(MainPageLocators.LOCATION(hotel))
        self._click_visible_element(MainPageLocators.DATE)
        time.sleep(100)
