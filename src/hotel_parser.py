import undetected_chromedriver as uc
import psycopg2
from datetime import datetime  # ToDo удалить после изменения цикла на 30 дней

from time import sleep
from random import randint
from pages.main_page.page import MainPage
from pages.hotel_page.page import HotelPage
from requirements.list_of_hotels import hotels
from utils.days_generator import DaysGenerator
from psql_connector.psql import scheme_init
from psql_connector.psql import table_init
from psql_connector.psql import table_insert
from pages.hotel_page.psql_connect import (DBNAME,
                                           DBUSER,
                                           DBPASSWORD,
                                           DBHOST,
                                           DBPORT,
                                           LOGGING,
                                           SCHEMENAME,
                                           TABLENAME)

conn = psycopg2.connect(
    dbname=DBNAME, user=DBUSER, password=DBPASSWORD, host=DBHOST, port=DBPORT
    )
conn.autocommit = True


class Parser(MainPage, HotelPage, DaysGenerator):

    def __init__(self):
        self.driver = uc.Chrome(headless=False)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.url = "https://travel.mts.ru/"
        self.driver.get(self.url)

    def close_browser(self):
        self.driver.quit()


scheme_init(conn, SCHEMENAME, DBUSER, LOGGING)
table_init(conn, SCHEMENAME, TABLENAME, LOGGING)
count_hotels = 10
start = datetime.now()  # ToDo удалить после изменения цикла на 30 дней
while count_hotels != 0:
    # Итерация по счетчику списка отелей
    for hotel in range(len(hotels)):
        # Итерация по позициям из списка
        parser = Parser()
        parser.search_hotel(hotels[hotel], hotels[hotel])
        parse_result = parser.parse_data()
        date = parser.get_date()
        table_insert(
            conn,
            SCHEMENAME,
            TABLENAME,
            hotels[hotel],
            date,
            str(parse_result["card"])
            .replace("[", "")
            .replace("]", "")
            .replace("'", ""),
            str(parse_result["price"])
            .replace("[", "")
            .replace("]", "")
            .replace("'", ""),
            str(parse_result["breakfast"])
            .replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .replace("(", "")
            .replace(")", ""),
            LOGGING
        )
        sleep(randint(2, 8))
        parser.close_browser()
        count_hotels -= 1
        print(hotel)
    sleep(randint(10, 15))
end = datetime.now()  # ToDo удалить после изменения цикла на 30 дней
execution_time = end - start  # ToDo удалить после изменения цикла на 30 дней
print(execution_time)  # ToDo удалить после изменения цикла на 30 дней


@property
def main_page(self):
    return MainPage(self.driver)


@property
def hotel_page(self):
    return HotelPage(self.driver)
