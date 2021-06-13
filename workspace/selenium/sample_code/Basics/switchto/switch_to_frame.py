from selenium import webdriver
import time



class SwitchToFrame():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.execute_script("window.scrollBy(0,1000);")

        #Switch to frame using id
        #driver.switch_to.frame("courses-iframe")

        #Switch to frame using name
        #driver.switch_to.frame("iframe-name")

        #Switch to frame using number
        driver.switch_to.frame(0)

        time.sleep(2)

        driver.find_element_by_id("search-courses").send_keys("python")
        time.sleep(2)

obj = SwitchToFrame()
obj.test()