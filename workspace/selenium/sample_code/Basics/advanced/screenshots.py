from selenium import webdriver
import time


class Screenshots():

    def test(self):
        baseUrl = "https://sso.teachable.com/secure/42299/users/sign_in"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        driver.find_element_by_id("user_email").send_keys("abc@gmail.com")
        driver.find_element_by_id("user_password").send_keys("abc")
        driver.find_element_by_xpath("//input[@type='submit']").click()

        self.takeScreenshot(driver)


    def takeScreenshot(self, driver):

        fileName = str(round(time.time()*1000))+".png"
        screenshotDirectory = "/home/akshayz/Documents/Selenium_Work/Basics/testdata/"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print ("Screenshot saved to directory --> ::" + destinationFile)
        except NotADirectoryError:
            print ("Not a directory issue")


obj = Screenshots()
obj.test()