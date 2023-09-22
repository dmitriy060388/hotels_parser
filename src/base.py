from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class BaseClass:

    def _right_click(self, element) -> None:
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    def _set_checkboxes(self, *args) -> bool:
        for arg in args:
            self._click_checkbox(arg)

        for arg in args:
            checkbox = self._find_checkbox(arg)
            assert checkbox.is_selected() is True

        return True

    def _click_checkbox(self, xpath):
        checkbox = self._find_checkbox(xpath)
        if not checkbox.is_selected():
            checkbox.click()

    def _find_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def _find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            ec.visibility_of_element_located(locator),
            message="Can't find element by locator {}".format(locator),
        )

    def _find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            ec.visibility_of_all_elements_located(locator),
            message="Can't find elements by locator {}".format(locator),
        )

    def _find_checkbox(self, xpath):
        return self._find_element_by_xpath(xpath)

    def _send_keys(self, locator, data, time=10):
        wait = WebDriverWait(self.driver, time)
        wait.until(
            ec.visibility_of_element_located(locator),
            message="Not visibility element {}".format(locator),
        ).send_keys(data)

    def _wait_invisible_element(self, locator, time=10):
        wait = WebDriverWait(self.driver, time)
        wait.until(
            ec.invisibility_of_element_located(locator),
            message="Not visibility element {}".format(locator),
        )

    def _wait_visible_element(self, locator, time=10):
        wait = WebDriverWait(self.driver, time)
        wait.until(
            ec.visibility_of_element_located(locator),
            message="Not visibility element {}".format(locator),
        )

    def _click_visible_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(
            ec.visibility_of_element_located(locator),
            message="Not visibility element {}".format(locator),
        ).click()

    def _click_clickable_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(
            ec.element_to_be_clickable(locator),
            message="Not visibility element {}".format(locator)
        ).click()
