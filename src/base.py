import undetected_chromedriver as uc

class BaseClass:

    def __init__(self) -> None:
        driver = uc.Chrome(headless=False)
        driver.maximize_window()
        url = "https://travel.mts.ru/"
        driver.get(url)


client = BaseClass()
