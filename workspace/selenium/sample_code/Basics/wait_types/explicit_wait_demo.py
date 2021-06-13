from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWaitDemo():
    def test(self):
        baseUrl = "https://www.expedia.com/"
        driver = webdriver.Chrome()
        driver.implicitly_wait(0.5)
        driver.maximize_window()
        driver.get(baseUrl)

        driver.find_element_by_xpath("//button[contains(@id, 'tab-flight-tab')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[contains(@id,'flight-origin-hp-flight')]").send_keys("SFO")
        driver.find_element_by_xpath("//input[contains(@id,'flight-destination-hp-flight')]").send_keys("NYC")
        driver.find_element_by_id("flight-departing-hp-flight").send_keys("5/26/2018")
        driver.find_element_by_id("flight-returning-hp-flight").send_keys("5/28/2018")
        driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

        #driver.find_element_by_id("stopFilter_stops-0").click()
        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotSelectableException,
                                                 ElementNotVisibleException])

        element = wait.until(EC.element_to_be_clickable((By.ID,"stopFilter_stops-0")))
        element.click()


obj = ExplicitWaitDemo()
obj.test()

