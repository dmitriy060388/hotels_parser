from pages.base import BaseClass
from .locators import MainPageLocators
from utils.days_generator import DaysGenerator


class MainPage(BaseClass):

    def search_hotel(self, hotel, data):
        DaysGenerator.one_day_generate(self)

        self.hotel = hotel
        self.data = data

        self._find_element(MainPageLocators.PLACE)
        self._click_visible_element(MainPageLocators.PLACE)
        self._send_keys(MainPageLocators.PLACE, data)
        self._click_visible_element(MainPageLocators.LOCATION(hotel))
        self._click_visible_element(MainPageLocators.DATE)
        self._click_visible_element(
            MainPageLocators.CURRENT_DAY(self.current_date)
        )
        self._click_visible_element(MainPageLocators.NEXT_DAY(self.next_date))
        self._click_visible_element(MainPageLocators.SEARCH)
