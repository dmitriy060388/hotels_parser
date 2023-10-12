from pages.base import BaseClass
from pages.main_page.page import MainPage
from .locators import HotelPageLocators
from selenium.common.exceptions import TimeoutException
import time

class HotelPage(BaseClass):

    def parse_data(self):

        # Проверка на наличие предложений с отелями
        self._wait_visible_element(HotelPageLocators.CHOOSE_ROOMS)

        self._click_visible_element(HotelPageLocators.CHOOSE_ROOMS)
        try:
            rooms_list = self._find_element(HotelPageLocators.ROOMS_LIST)
            # import pdb; pdb.set_trace()
            if self._find_elements(HotelPageLocators.ROOM_NAME1):
                rooms_card = self._find_elements(HotelPageLocators.ROOM_NAME1)
            else:
                rooms_card = self._find_elements(HotelPageLocators.ROOM_NAME2)
            # rooms_card = self._find_elements(HotelPageLocators.ROOM_NAME1)
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
