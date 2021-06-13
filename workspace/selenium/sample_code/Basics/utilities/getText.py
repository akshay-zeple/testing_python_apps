from selenium import webdriver
import time

class getText():

    def test(self):

        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get(baseUrl)

        driver.implicitly_wait(10)

        element = driver.find_element_by_id("opentab")

        openTabBtnText = element.text

        print ("Text on CTA is: "+ openTabBtnText)


obj = getText()
obj.test()

