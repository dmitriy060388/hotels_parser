import undetected_chromedriver as uc
import time
import psycopg2

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
                                           LOGGING)

conn = psycopg2.connect(
    dbname=DBNAME, user=DBUSER, password=DBPASSWORD, host=DBHOST, port=DBPORT
    )
conn.autocommit = True


class Parser(MainPage, HotelPage, DaysGenerator):

    def __init__(self):
        # self.hotel_name = hotel_name
        self.driver = uc.Chrome(headless=False)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.url = "https://travel.mts.ru/"
        self.driver.get(self.url)

    def close_browser(self):
        self.driver.quit()


scheme_init(conn, "mts_scheme", DBUSER, LOGGING)
table_init(conn, "mts_scheme", "result", LOGGING)
x = 10
while x != 0:
    for i in range(len(hotels)):
        parser = Parser()
        parser.search_hotel(hotels[i], hotels[i])
        y = parser.parse_data()
        date = parser.get_date()
        table_insert(
            conn,
            "mts_scheme",
            "result",
            hotels[i],
            date,
            y[1],
            y[0],
            'NULL',
            LOGGING
        )
        time.sleep(5)
        parser.close_browser()
        x -= 1
    time.sleep(15)


@property
def main_page(self):
    return MainPage(self.driver)


@property
def hotel_page(self):
    return HotelPage(self.driver)
