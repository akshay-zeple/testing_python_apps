from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

class DropdownSelect():

    def test(self):

        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get(baseUrl)

        driver.implicitly_wait(10)

        element = driver.find_element_by_id("carselect")

        s = Select(element)

        s.select_by_index(2)
        print ("Select honda by index")
        time.sleep (2)

        s.select_by_value("benz")
        print("Select benz by value")
        time.sleep(2)

        s.select_by_visible_text("BMW")
        print ("Select BMW by visible text")
        time.sleep(2)

obj = DropdownSelect()
obj.test()

