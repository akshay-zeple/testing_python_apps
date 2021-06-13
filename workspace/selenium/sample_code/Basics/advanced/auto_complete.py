from selenium import webdriver
import time


class AutoComplete():

    def test(self):
        baseUrl = "https://www.southwest.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        #time.sleep(5)
        driver.implicitly_wait(10)

        cityField = driver.find_element_by_xpath("//input[@id='air-city-departure']")
        cityField.send_keys("new york")

        driver.find_element_by_xpath("//ul[@id='air-city-departure-menu']//li[contains(text(),'EWR')]").click()
        time.sleep(5)

obj = AutoComplete()
obj.test()