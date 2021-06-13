from selenium import webdriver

class FindByIdName():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        elemenyById = driver.find_element_by_id("name")

        if elemenyById is not None:
            print("We found an element by ID")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print ("We found an element by Name")


obj = FindByIdName()
obj.test()