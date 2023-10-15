import undetected_chromedriver as uc
import time

from pages.main_page.page import MainPage
from pages.hotel_page.page import HotelPage
from requirements.list_of_hotels import hotels
from utils.days_generator import DaysGenerator

import psycopg2 #1
from psycopg2 import sql #1
from psql_connector.psql import scheme_init #1
from psql_connector.psql import table_init #1
from psql_connector.psql import table_insert #1
# from psql_connector.psql import table_check_last_id #1
from pages.hotel_page.psql_connect import DBNAME, DBUSER, DBPASSWORD, DBHOST, DBPORT, LOGGING #1

conn = psycopg2.connect(dbname=DBNAME, user=DBUSER, password=DBPASSWORD, host=DBHOST, port=DBPORT) #1
conn.autocommit = True #1

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


scheme_init(conn, "mts_scheme", DBUSER, LOGGING) #1
table_init(conn, "mts_scheme", "result", LOGGING) #1
# print(table_check_last_id(conn, "mts_scheme", "result"))
# tabmaxid = table_check_last_id(conn, "mts_scheme", "result") + 1 #1
x = 10
while x != 0:
    for i in range(len(hotels)):
        parser = Parser()
        parser.search_hotel(hotels[i], hotels[i])
        y = parser.parse_data()
        date = parser.get_date()
        # tabmaxid=tabmaxid + 1 #1
        table_insert(conn, "mts_scheme", "result", hotels[i], date, y[1], y[0], 'NULL', LOGGING) #1
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
