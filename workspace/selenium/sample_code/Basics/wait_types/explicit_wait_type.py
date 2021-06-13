from utilities.HandyWrappers import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitType():

    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrappers()

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):

        element=None
        try:
            byType = self.hw.getByType(locatorType)

            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotSelectableException,
                                                 ElementNotVisibleException])

            element = wait.until(EC.element_to_be_clickable((byType, "stopFilter_stops-0")))

            print("Element appeared on webpage")
        except:
            print("Element appeared on webpage")

        return element
