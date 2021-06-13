from selenium import webdriver
import time


class CalendarSelection():
    def test1(self):
        baseUrl = "https://www.expedia.co.in"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        time.sleep(5)
        driver.implicitly_wait(10)
        checkInField = driver.find_element_by_id("hotel-checkin-hp-hotel")
        checkInField.send_keys("31/05/2018")
        time.sleep(5)

    def test2(self):
        baseUrl = "https://www.expedia.co.in"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        time.sleep(5)
        checkInField = driver.find_element_by_id("hotel-checkin")
        checkInField.click()
        driver.find_element_by_xpath("//div[@class='datepicker-cal-month'][position()=1]//button[text()='31']").click()
        time.sleep(5)

    def test3(self):
        baseUrl = "https://www.expedia.co.in"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        time.sleep(5)
        checkInField = driver.find_element_by_id("hotel-checkin-hp-hotel")
        checkInField.click()
        dates = driver.find_elements_by_xpath("//div[@class='datepicker-cal-month'][position()=1]//button")
        for date in dates:
            if date.text == "31":
                date.click()
                break
        time.sleep(5)


obj = CalendarSelection()
obj.test2()
