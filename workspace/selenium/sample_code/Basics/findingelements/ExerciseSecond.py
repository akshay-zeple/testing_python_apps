from selenium import webdriver

class ExerciseSecond():

    def test(self):

        baseUrl = "http://dhtmlx.com/docs/products/dhtmlxGrid/"
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(baseUrl)

        ele = driver.find_element_by_xpath("//div[@id='gridbox']//a[text()='The	Green Mile']//parent::td//following-­‐sibling::td[1]")
        bookAuther = ele.text


        print ("The Author of the book The Green Mile is: "+ bookAuther)


obj = ExerciseSecond()
obj.test()
