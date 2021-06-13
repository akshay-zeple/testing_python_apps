from selenium import webdriver

class FindByXpathCss():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        elemenyByXpath = driver.find_element_by_xpath("//input[@id='name']")

        if elemenyByXpath is not None:
            print("We found an element by XPATH")

        elementByCss = driver.find_element_by_css_selector("#displayed-text")

        if elementByCss is not None:
            print ("We found an element by CSS")


obj = FindByXpathCss()
obj.test()