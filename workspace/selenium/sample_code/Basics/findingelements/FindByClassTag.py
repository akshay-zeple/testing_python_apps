from selenium import webdriver

class FindByClassTag():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        #driver = webdriver.Firefox(executable_path="/home/akshayz/Documents/Selenium_Work/geckodriver")
        driver.get(baseUrl)

        elementyByClassName = driver.find_element_by_class_name("displayed-class")
        elementyByClassName.send_keys("TestInput")

        if elementyByClassName is not None:
            print("We found an element by Class Name")

        elementByTagName = driver.find_element_by_tag_name("h1")
        elementByTagText = elementByTagName.text

        if elementByTagName is not None:
            print ("We found an element by Tag Name and the text on element is: "+elementByTagText)


obj = FindByClassTag()
obj.test()