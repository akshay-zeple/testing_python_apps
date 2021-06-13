from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class MouseHover():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        driver.execute_script("window.scrollBy(0,600);")

        toElement = driver.find_element_by_id("mousehover")

        action = ActionChains(driver)
        action.move_to_element(toElement).perform()
        time.sleep(2)

        topLink = driver.find_element_by_xpath("//div[@class='mouse-hover-content']//a[text()='Top']")
        action.move_to_element(topLink).click().perform()

        time.sleep(2)


obj = MouseHover()
obj.test()