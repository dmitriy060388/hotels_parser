from pages.base import BaseClass
from .locators import HotelPageLocators


class HotelPage(BaseClass):

    def parse_data(self):
        self._wait_visible_element(HotelPageLocators.CHOOSE_ROOMS)
        self._click_visible_element(HotelPageLocators.CHOOSE_ROOMS)
        try:
            self._wait_visible_element(HotelPageLocators.BUTTON_ROOM)
            button = self._find_element(HotelPageLocators.BUTTON_ROOM).value_of_css_property('background-color')
            if "rgba(255, 0, 50, 1)" in button:
                rooms_list = self._find_element(HotelPageLocators.ROOMS_LIST)
                rooms_card = self._find_elements(HotelPageLocators.ROOM_NAME1)
                rooms_price = self._find_elements(HotelPageLocators.ROOM_PRICE)
                # Все цены
                for rooms_prices in rooms_price:
                    price = (str(rooms_prices.text))
                # Типы номеров
                for rooms_cards in rooms_card:
                    card = (str(rooms_cards.text))
                return price, card

            rooms_price = self._find_elements(HotelPageLocators.ROOM_PRICE)
            # Все цены
            for x in rooms_price:
                print(str(x.text))
            # Типы номеров
            for x in rooms_card:
                print(str(x.text))
        except:
            result = self._find_element(HotelPageLocators.HOTEL_NOT_FOUND).text
            print(result)
