from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class Sliders():

    def test(self):
        baseUrl = "https://jqueryui.com/slider/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.switch_to.frame(0)

        e = driver.find_element_by_xpath("//div[@id='slider']/span")
        action = ActionChains(driver)

        action.drag_and_drop_by_offset(e, 100, 0).perform()



        time.sleep(2)


obj = Sliders()
obj.test()