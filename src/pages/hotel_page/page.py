from pages.base import BaseClass
from .locators import HotelPageLocators
from selenium.common.exceptions import TimeoutException


class HotelPage(BaseClass):

    def choose_hotel(self):

        # Проверка на наличие предложений с отелями
        try:
            self._wait_visible_element(HotelPageLocators.CHOOSE_ROOMS)
        except TimeoutException:
            error = self._find_element(HotelPageLocators.HOTEL_NOT_FOUND).text
            raise TimeoutException("Ошибка - {}".format(error))

        self._click_visible_element(HotelPageLocators.CHOOSE_ROOMS)
