from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class DragAndDrop():

    def test(self):
        baseUrl = "https://jqueryui.com/droppable/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.switch_to.frame(0)

        fromElement = driver.find_element_by_id("draggable")
        toElement = driver.find_element_by_id("droppable")

        action = ActionChains(driver)
        #action.drag_and_drop(fromElement, toElement).perform()
        action.click_and_hold(fromElement).move_to_element(toElement).release().perform()


        time.sleep(2)


obj = DragAndDrop()
obj.test()