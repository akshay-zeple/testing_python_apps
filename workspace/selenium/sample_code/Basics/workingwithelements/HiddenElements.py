from selenium import webdriver
import time

class HiddenElements():

    def isEnabled(self):

        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get(baseUrl)

        driver.implicitly_wait(10)


        e = driver.find_element_by_id("displayed-text")
        elementState = e.is_displayed()
        print ("Is the element visible -> " +str(elementState))
        time.sleep(2)

        driver.find_element_by_id("hide-textbox").click()

        elementState = e.is_displayed()
        print("Is the element visible -> " + str(elementState))
        time.sleep(2)

        driver.find_element_by_id("show-textbox").click()

        elementState = e.is_displayed()
        print("Is the element visible -> " + str(elementState))
        time.sleep(2)

obj = HiddenElements()
obj.isEnabled()

