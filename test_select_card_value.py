from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time


class TestSelectCard(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_select_card_value(self):
        wd = self.wd
        wd.get("https://HR:test@qa.digift.ru/")
        wd.find_element(By.XPATH, "//li[1]/button").click()
        wd.find_element(By.XPATH, "//li[2]/button").click()
        wd.find_element(By.XPATH, "//li[3]/button").click()
        wd.find_element(By.XPATH, "//li[4]/button").click()
        wd.find_element(By.XPATH, "//li[5]/button").click()
        wd.find_element(By.XPATH, "//li[6]/button").click()
        time.sleep(5)

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
