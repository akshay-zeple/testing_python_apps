from selenium import webdriver

class ExerciseFirst():

    def test(self):

        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(baseUrl)

        ele = driver.find_element_by_xpath("//table[@id='product']//td[text()='Python Programming Language']//following-sibling::td")
        coursePrice = ele.text


        print ("The price of the course Python Programming Language is: "+ coursePrice)


obj = ExerciseFirst()
obj.test()