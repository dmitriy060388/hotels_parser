import undetected_chromedriver as uc
import time

from pages.base import BaseClass
from pages.main_page.page import MainPage
from pages.hotel_page.page import HotelPage
from pages.main_page.locators import MainPageLocators
from requirements import list_of_hotels


class Cosmos(MainPage, HotelPage):
    pass
x = Cosmos()
x.search_hotel(list_of_hotels.hotels[0], list_of_hotels.hotels[0])
x.choose_hotel()
time.sleep(25)




@property
def main_page(self):
    return MainPage(self.driver)

@property
def hotel_page(self):
    return HotelPage(self.driver)


# class Parser(BaseClass):

#     def __init__(self) -> None:
#         self.driver = uc.Chrome(headless=False)
#         self.driver.maximize_window()
#         self.driver.delete_all_cookies()
#         self.url = "https://travel.mts.ru/"
#         self.driver.get(self.url)


# if __name__ == '__main__':
#     client = Parser()
#     client._find_element(MainPageLocators.MAIN_PAGE)
#     client._click_visible_element(MainPageLocators.PLACE)
#     client._send_keys(MainPageLocators.PLACE, list_of_hotels.hotels[0])
#     client._wait_visible_element(
#         MainPageLocators.LOCATION(list_of_hotels.hotels[0])
#     )
#     client._click_clickable_element(
#         MainPageLocators.LOCATION(list_of_hotels.hotels[0])
#     )
#     client._click_visible_element(MainPageLocators.DATE)

    # time.sleep(150)
