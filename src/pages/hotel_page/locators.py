from selenium.webdriver.common.by import By


class HotelPageLocators:

    CHOOSE_ROOMS = (By.XPATH, '//button[@data-test='
                    '"select_rooms"]')
    HOTEL_NOT_FOUND = (
        By.XPATH, '//h2[@class="p2-medium"][contains(text(), "По вашему запросу ничего не нашлось")]'
    )