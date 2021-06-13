from selenium import webdriver
import time

class getAttribute():

    def test(self):

        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get(baseUrl)

        driver.implicitly_wait(10)

        element = driver.find_element_by_id("name")

        valueOfAttribute = element.get_attribute("placeholder")

        print ("Value of Attribute is: "+ valueOfAttribute)


obj = getAttribute()
obj.test()

