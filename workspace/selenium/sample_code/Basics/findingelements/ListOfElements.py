from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        elementListByClassNames = driver.find_elements_by_class_name("inputs")
        length1 = len(elementListByClassNames)
        if elementListByClassNames is not None:
            print("ClassName -> Size of list is: "+ str(length1))

        elementListByTagName = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(elementListByTagName)
        if elementListByTagName is not None:
            print("TagName -> Size of list is: " + str(length2))


obj = ListOfElements()
obj.test()