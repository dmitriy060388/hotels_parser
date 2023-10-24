from pages.base import BaseClass
from .locators import MainPageLocators
from utils.days_generator import DaysGenerator
from time import sleep
from random import randint


class MainPage(BaseClass):

    def search_hotel(self, hotel, data):
        DaysGenerator.week_generate(self)

        self.hotel = hotel
        self.data = data

        self._find_element(MainPageLocators.PLACE)
        self._click_visible_element(MainPageLocators.PLACE)
        sleep(randint(2, 8))
        self._send_keys(MainPageLocators.PLACE, data)
        sleep(randint(2, 8))
        self._click_visible_element(MainPageLocators.LOCATION(hotel))
        sleep(randint(2, 8))
        self._click_visible_element(MainPageLocators.DATE)
        sleep(randint(2, 8))
        self._click_visible_element(
            MainPageLocators.CURRENT_DAY(self.days_list[0])
        )
        sleep(randint(2, 8))
        self._click_visible_element(MainPageLocators.NEXT_DAY(self.days_list[1]))
        sleep(randint(2, 8))
        self._click_visible_element(MainPageLocators.SEARCH)
