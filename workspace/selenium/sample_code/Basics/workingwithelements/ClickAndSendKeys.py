from selenium import webdriver
import time

class ClickAndSendKeys():

    def test(self):

        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get(baseUrl)

        driver.implicitly_wait(10)

        loginLink = driver.find_element_by_xpath("//*[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        emailField = driver.find_element_by_id("user_email")
        emailField.send_keys("test")

        passwordField = driver.find_element_by_id("user_password")
        passwordField.send_keys("test")


        time.sleep(3)

        emailField.clear()

        emailField.send_keys("test")


obj = ClickAndSendKeys()
obj.test()

