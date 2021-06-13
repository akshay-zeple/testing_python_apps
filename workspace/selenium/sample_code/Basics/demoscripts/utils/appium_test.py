from appium import webdriver
import unittest


BASE_URL = "https://www.starz-aso.com"

class demo (unittest.TestCase):

    def setUp(self):

        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '11.2'
        desired_caps['deviceName'] = 'iPhone 6'
        desired_caps['browserName'] = 'Safari'
        desired_caps['autoAcceptAlerts'] = True
        desired_caps['safariAllowPopups'] = True
        desired_caps['automationName'] = 'XCUITest'

        self.driver = webdriver.Remote(command_executor="http://0.0.0.0:4723/wd/hub", desired_capabilities=desired_caps)

    def test_url(self):
        print (self.driver.title)