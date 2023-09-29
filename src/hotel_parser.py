import undetected_chromedriver as uc
import time

from pages.main_page.page import MainPage
from pages.hotel_page.page import HotelPage
from requirements import list_of_hotels


class Parser(MainPage, HotelPage):

    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.driver = uc.Chrome(headless=False)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.url = "https://travel.mts.ru/"
        self.driver.get(self.url)


cosmos = Parser(list_of_hotels.hotels[0])
cosmos.search_hotel(list_of_hotels.hotels[0], list_of_hotels.hotels[0])
cosmos.parse_data()

time.sleep(25)


@property
def main_page(self):
    return MainPage(self.driver)


@property
def hotel_page(self):
    return HotelPage(self.driver)
