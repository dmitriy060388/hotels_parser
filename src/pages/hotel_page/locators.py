from selenium.webdriver.common.by import By


class HotelPageLocators:

    CHOOSE_ROOMS = (By.XPATH, '//button[@data-test='
                    '"select_rooms"]')
    HOTEL_NOT_FOUND = (By.XPATH, '//div[@data-test="hotels_title"]')
    ROOMS_LIST = (By.XPATH, '//section[@id="rooms"]')
    ROOM_NAME1 = (By.XPATH, '//div[@data-test="room_name"]/h3')
    ROOM_NAME2 = (By.XPATH, '//p[@data-test="room_name"]')
    ROOM_PRICE = (By.XPATH, '//p[@data-test="price"]')
    BUTTON_ROOM = (By.XPATH, '//button[@data-test="book_room"]')
    # #1d2023 - black button
    # #ff0032 - red button
