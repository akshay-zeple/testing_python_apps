from selenium import webdriver
import time

class RadioBtnAndCheckBoxes():

    def isSelected(self):

        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get(baseUrl)

        driver.implicitly_wait(10)


        bmwRadioBtn = driver.find_element_by_id("bmwradio")
        bmwRadioBtn.click()

        benzRadioBtn = driver.find_element_by_id("benzradio")
        benzRadioBtn.click()

        bmwCheckBox = driver.find_element_by_id("bmwcheck")
        bmwCheckBox.click()

        benzCheckBox = driver.find_element_by_id("benzcheck")
        benzCheckBox.click()

        print ("Is BMW Radio Btn Selected? -> " +str(bmwRadioBtn.is_selected()))
        print("Is Benz Radio Btn Selected? -> " + str(benzRadioBtn.is_selected()))
        print("Is BMW Checkbox Btn Selected? -> " + str(bmwCheckBox.is_selected()))
        print("Is Benz Checkbox Btn Selected? -> " + str(benzCheckBox.is_selected()))



obj = RadioBtnAndCheckBoxes()
obj.isSelected()

