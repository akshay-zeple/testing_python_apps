from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import random


class FirstClass():
    def test(self):
        # chrome_options= webdriver.ChromeOptions()
        # chrome_options.add_argument('headless')

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://get.myollie.com/profile.html")
        print(driver.title)
        time.sleep(3)

        yourname = driver.find_element_by_xpath("//input[@placeholder='Your first name']")
        yourname.send_keys("akshay")
        # time.sleep(2)


        pupname = driver.find_element_by_id("jsPupsName")
        pupname.send_keys("bruno")
        # time.sleep(2)

        email = driver.find_element_by_xpath("//input[@data-key='email']")

        emailid = "sol-mail-bot+{}@ampush.com".format(random.randint(0, 1000))

        email.send_keys(emailid)
        time.sleep(2)

        zip = driver.find_element_by_id("zipCodeElement")
        zip.send_keys("95107")
        time.sleep(2)

        nextbtn = driver.find_element(By.ID, "jsNextBtn")
        nextbtn.click()

        time.sleep(3)

        headerText = driver.find_element_by_xpath(
            "//section[@class='pupsinfo js-tabs js-timeline show']//h2[contains(text(),'Tell us about')]")

        print(headerText.text)
        assert "bruno" in headerText.text

        time.sleep(5)

        driver.quit()


obj = FirstClass()
obj.test()


# class Employee():
#
#     def __init__(self, firstname, lastname, pay):
#         self.first = firstname
#         self.last = lastname
#         self.pay = pay
#
#     def fullname(self):
#         #pass
#         return "{} {}".format(self.first, self.last)
#
# emp1 = Employee("Snehal", "Karande", 100000)
# emp2 = Employee("Divya", "D", 10000)
#
#
#
#
# print(emp1.fullname())
# print(emp2.fullname())
#
# Employee.fullname(emp1)
# emp1.fullname()
