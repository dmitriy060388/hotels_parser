from selenium.webdriver.common.by import By


class MainPageLocators:

    MAIN_PAGE = (By.XPATH, '//body[@class="antialiased"]')
    PLACE = (By.XPATH, '//input[@data-test="search_place"]')
    DATE = (By.XPATH, '//input[@data-test="search_date_field"]')
    NUMBER_OF_PEOPLE = (By.XPATH, '//div[@data-test="accommodation_field"]')
    SEARCH = (By.XPATH, '//button[@data-test="search_button"]')

    LOCATION = lambda x: (By.XPATH, '//div[contains(text(), "{}")]'.format(x)) # noqa
