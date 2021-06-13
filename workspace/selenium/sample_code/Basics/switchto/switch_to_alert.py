from selenium import webdriver
import time


class SwitchToAlert():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        driver.find_element_by_id("name").send_keys("Akshay")
        driver.find_element_by_id("alertbtn").click()
        alert1 = driver.switch_to.alert
        time.sleep(2)
        alert1.accept()

        driver.find_element_by_id("name").send_keys("Akshay")
        driver.find_element_by_id("confirmbtn").click()
        alert2 = driver.switch_to.alert
        time.sleep(2)
        alert2.dismiss()


obj = SwitchToAlert()
obj.test()