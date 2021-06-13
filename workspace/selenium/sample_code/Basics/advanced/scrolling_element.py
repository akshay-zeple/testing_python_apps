from selenium import webdriver
import time

class ScrollingElement():

    def test(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.implicitly_wait(10)

        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(3)

        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(3)

        element = driver.find_element_by_id("mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("window.scrollBy(0,-150)")
        time.sleep(3)



obj = ScrollingElement()
obj.test()