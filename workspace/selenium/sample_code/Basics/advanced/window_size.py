from selenium import webdriver
import time

class WindowSize():

    def test(self):

        driver = webdriver.Chrome()
        #driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.implicitly_wait(10)

        height = driver.execute_script("return window.innerHeight")
        width = driver.execute_script("return window.innerWidth")

        print ("Height: "+str(height))
        print ("Width: "+str(width))


obj = WindowSize()
obj.test()
