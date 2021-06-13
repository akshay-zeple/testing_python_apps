from selenium import webdriver
import time

class ElementState():

    def isEnabled(self):

        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get(baseUrl)

        driver.implicitly_wait(10)


        e = driver.find_element_by_id("gs_htif0")
        elementState = e.is_enabled()
        print ("Is the elemet enabled -> " +str(elementState))
        #e.send_keys("test")


        e1 = driver.find_element_by_id("lst-ib")
        elementState = e1.is_enabled()
        print("Is the elemet enabled -> " + str(elementState))
        e1.send_keys("test")


obj = ElementState()
obj.isEnabled()

