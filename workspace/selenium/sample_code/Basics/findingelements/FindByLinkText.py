from selenium import webdriver
import time

class FindByXpathCss():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        #driver = webdriver.Firefox(executable_path="/home/akshayz/Documents/Selenium_Work/geckodriver")
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        time.sleep (5)

        elementByLinkText = driver.find_element_by_link_text("Login")

        if elementByLinkText is not None:
            print("We found an element by Link Text")

        elementByPartialLinkText = driver.find_element_by_partial_link_text("Pract")

        if elementByPartialLinkText is not None:
            print ("We found an element by Partial Link Text")


obj = FindByXpathCss()
obj.test()