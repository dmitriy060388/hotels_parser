import undetected_chromedriver as uc
import time


driver = uc.Chrome(headless=False)
url = "https://travel.mts.ru/"
driver.get(url)
time.sleep(15)
driver.quit()
