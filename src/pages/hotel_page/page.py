from pages.base import BaseClass
from .locators import HotelPageLocators
from selenium.common.exceptions import TimeoutException
from time import sleep
from random import randint


class HotelPage(BaseClass):

    def parse_data(self):
        result = {}
        result["price"] = []
        result["card"] = []
        self._wait_visible_element(HotelPageLocators.CHOOSE_ROOMS)
        sleep(randint(2, 8))
        self._click_visible_element(HotelPageLocators.CHOOSE_ROOMS)
        sleep(randint(2, 8))
        try:
            self._wait_visible_element(HotelPageLocators.BUTTON_ROOM)
            button = self._find_element(
                HotelPageLocators.BUTTON_ROOM
                ).value_of_css_property('background-color')
            if "rgba(255, 0, 50, 1)" in button:
                rooms_list = self._find_element(HotelPageLocators.ROOMS_LIST)
                rooms_card = self._find_elements(HotelPageLocators.ROOM_NAME1)
                rooms_price = self._find_elements(HotelPageLocators.ROOM_PRICE)
                # Все цены
                for rooms_prices in rooms_price:
                    result["price"].append(rooms_prices.text)
                # Типы номеров
                for rooms_cards in rooms_card:
                    result["card"].append(rooms_cards.text)
                return result

        except TimeoutException:
            nothing = "Номера не найдены"
            result["price"] = nothing
            result["card"] = nothing
            return result
