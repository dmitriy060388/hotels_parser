from pages.base import BaseClass
from .locators import HotelPageLocators
from selenium.common.exceptions import TimeoutException


class HotelPage(BaseClass):

    def parse_data(self):

        # Проверка на наличие предложений с отелями
        try:
            self._wait_visible_element(HotelPageLocators.CHOOSE_ROOMS)
        except TimeoutException:
            error = self._find_element(HotelPageLocators.HOTEL_NOT_FOUND).text
            raise TimeoutException("Ошибка - {}".format(error))

        self._click_visible_element(HotelPageLocators.CHOOSE_ROOMS)
        rooms_list = self._find_element(HotelPageLocators.ROOMS_LIST)
        rooms_card = self._find_elements(HotelPageLocators.ROOM_NAME)
        rooms_price = self._find_elements(HotelPageLocators.ROOM_PRICE)

        # Все цены
        for x in rooms_price:
            print(str(x.text))
        # Типы номеров
        for x in rooms_card:
            print(str(x.text))
