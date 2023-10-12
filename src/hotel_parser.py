import undetected_chromedriver as uc
import time

from pages.main_page.page import MainPage
from pages.hotel_page.page import HotelPage
from requirements.list_of_hotels import hotels


class Parser(MainPage, HotelPage):

    def __init__(self):
        # self.hotel_name = hotel_name
        self.driver = uc.Chrome(headless=False)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.url = "https://travel.mts.ru/"
        self.driver.get(self.url)

    def close_browser(self):
        self.driver.quit()


x = 10
while x != 0:
    for i in range(len(hotels)):
        parser = Parser()
        parser.search_hotel(hotels[i], hotels[i])
        parser.parse_data()
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
