import undetected_chromedriver as uc
import time

from base import BaseClass
from pages.main_page.locators import MainPageLocators
from requirements import list_of_hotels


class Parser(BaseClass):

    def __init__(self) -> None:
        self.driver = uc.Chrome(headless=False)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.url = "https://travel.mts.ru/"
        self.driver.get(self.url)


if __name__ == '__main__':
    client = Parser()
    client._find_element(MainPageLocators.MAIN_PAGE)
    client._click_visible_element(MainPageLocators.PLACE)
    client._send_keys(MainPageLocators.PLACE, list_of_hotels.hotels[0])
    client._wait_visible_element(
        MainPageLocators.LOCATION(list_of_hotels.hotels[0])
    )
    client._click_clickable_element(
        MainPageLocators.LOCATION(list_of_hotels.hotels[0])
    )
    client._click_visible_element(MainPageLocators.DATE)

    time.sleep(150)
