from selenium import webdriver
import time

class JavascriptExecution():

    def test(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        #driver.get("https://letskodeit.teachable.com/p/practice")
        driver.execute_script("window.location='https://letskodeit.teachable.com/p/practice';")
        driver.implicitly_wait(10)

        #element = driver.find_element_by_id("name")
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("test")

obj = JavascriptExecution()
obj.test()
