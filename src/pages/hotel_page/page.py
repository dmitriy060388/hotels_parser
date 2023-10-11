from pages.base import BaseClass
from pages.main_page.page import MainPage
from .locators import HotelPageLocators
from selenium.common.exceptions import TimeoutException
import time
import psycopg2 #1
from psycopg2 import sql #1
from src.psql_connector.psql import scheme_init #1
from src.psql_connector.psql import table_init #1
from src.psql_connector.psql import table_insert #1

DBNAME='mts_test_1' #1
DBUSER='postgres' #1
DBPASSWORD='P@ssw0rd!' #1
DBHOST='localhost' #1
DBPORT='5432' #1
LOGGING = "DEBUG" # состояния: ERROR, DEBUG. В состоянии DEBUG в терминал будет попадать вывод из postgres #1

conn = psycopg2.connect(dbname=DBNAME, user=DBUSER, password=DBPASSWORD, host=DBHOST, port=DBPORT) #1
conn.autocommit = True #1

class HotelPage(BaseClass):

    def parse_data(self):

        # Проверка на наличие предложений с отелями
        self._wait_visible_element(HotelPageLocators.CHOOSE_ROOMS)

        self._click_visible_element(HotelPageLocators.CHOOSE_ROOMS)
        try:
            rooms_list = self._find_element(HotelPageLocators.ROOMS_LIST)
            rooms_card = self._find_elements(HotelPageLocators.ROOM_NAME)
            rooms_price = self._find_elements(HotelPageLocators.ROOM_PRICE)
            scheme_init(conn, "mts_scheme", DBUSER, LOGGING) #1
            table_init(conn, "mts_scheme", "result", LOGGING) #1
            tabmaxid=table_check_last_id(conn, "mts_scheme", "result") + 1 #1
            # Все цены
            for x in rooms_price:
                print(str(x.text))
            # Типы номеров
            for x in rooms_card:
                print(str(x.text))
            for x in rooms_price: #1
                tabmaxid=tabmaxid + 1 + x #1
                table_insert(conn, "mts_scheme", "result", tabmaxid, rooms_card[x], NULL, rooms_price[x], NULL, NULL, LOGGING) #1
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
