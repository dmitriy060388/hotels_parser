from pages.base import BaseClass
from .locators import MainPageLocators
# from requirements import list_of_hotels
import datetime
import time


class MainPage(BaseClass):

    def search_hotel(self, hotel, data):
        self.current_date = datetime.date.today()
        self.delta_date = datetime.timedelta(
            days=1
            )
        self.time = (datetime.datetime.now(
            datetime.timezone.utc
            ) + self.delta_date)
        self.next_date = self.time.strftime(
            "%Y-%m-%d"
            )
        self.hotel = hotel
        self.data = data

        self._find_element(MainPageLocators.PLACE)
        self._click_visible_element(MainPageLocators.PLACE)
        self._send_keys(MainPageLocators.PLACE, data)
        self._click_visible_element(MainPageLocators.LOCATION(hotel))
        self._click_visible_element(MainPageLocators.DATE)
        self._click_visible_element(MainPageLocators.CURRENT_DAY(self.current_date))
        self._click_visible_element(MainPageLocators.NEXT_DAY(self.next_date))
        self._click_visible_element(MainPageLocators.SEARCH)
        time.sleep(100)
