from selenium import webdriver
import os


class RunFFTests():

    def test(self):

        driver = webdriver.Firefox(executable_path="/home/akshayz/Documents/Selenium_Work/geckodriver")
        driver.get("http://www.letskodeit.com")



    # def test_ie(self):
    #     driverLocation = "C:\\Users\\..."
    #     os.environ["webdriver.ie.driver"] = driverLocation
    #     driver = webdriver.Ie(driverLocation)
    #     driver.get("http://www.google.com")


ff = RunFFTests()
ff.test()



#https://github.com/mozilla/geckodriver/releases
#chmod +x geckodriver
#export PATH = $PATH:/home/akshayz/Documents/Selenium_Work