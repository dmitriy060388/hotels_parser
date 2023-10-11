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
            rooms_card = self._find_elements(HotelPageLocators.ROOM_NAME)
            rooms_price = self._find_elements(HotelPageLocators.ROOM_PRICE)
            scheme_init(conn, "mts_scheme", DBUSER, LOGGING)
            table_init(conn, "mts_scheme", "result", LOGGING)
            tabmaxid=table_check_last_id(conn, "mts_scheme", "result") + 1
            # Все цены
            for x in rooms_price:
                print(str(x.text))
            # Типы номеров
            for x in rooms_card:
                print(str(x.text))
            for x in rooms_price:
                tabmaxid=tabmaxid + 1 + x
                table_insert(conn, "mts_scheme", "result", tabmaxid, rooms_card[x], NULL, rooms_price[x], NULL, NULL, LOGGING)
        except:
            result = self._find_element(HotelPageLocators.HOTEL_NOT_FOUND).text
            print(result)


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
