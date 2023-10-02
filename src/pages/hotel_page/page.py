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
        rooms_list = self._find_element(HotelPageLocators.ROOMS_LIST)
        try:
            rooms_card = self._find_elements(HotelPageLocators.ROOM_NAME)
        except TimeoutException:
            error = self._find_element(HotelPageLocators.HOTEL_NOT_FOUND).text
            raise TimeoutException(
                "Номера в отеле не найдены, {}".format(error)
            )
        rooms_price = self._find_elements(HotelPageLocators.ROOM_PRICE)

        # Все цены
        for x in rooms_price:
            print(str(x.text))
        # Типы номеров
        for x in rooms_card:
            print(str(x.text))

    # def save_data(self):
    #     with open(f'savedata/data_result'
    #               f'{MainPage.current_date} {MainPage.next_date}.csv',
    #               'a', newline='') as file:
    #         """открывем файл на дозапись
    #         (иначе перезатрём данные из цикла)"""
    #         self.writer = csv.writer(file, delimiter=' ')
    #         """сохраняем результат
    #         функции writer в переменную"""
    #         self.writer.writerow([rooms_card])
    #         self.writer.writerow([rooms_price])
    #         # self.writer.writerow([eat])
