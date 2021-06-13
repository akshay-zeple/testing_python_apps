from selenium import webdriver
import time

class WorkingWithElementsList():

    def test(self):

        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get(baseUrl)

        driver.implicitly_wait(10)

        radioBtnList = driver.find_elements_by_xpath("//input[contains(@type, 'radio') and contains(@name, 'cars')]")

        size = len (radioBtnList)
        print ("Size of List: "+str(size))

        for radioBtn in radioBtnList:
            isSelected = radioBtn.is_selected()

            if not isSelected:
                radioBtn.click()
                time.sleep(2)


obj = WorkingWithElementsList()
obj.test()

