from selenium.webdriver.common.by import By


class HandyWrappers():

    def __init__(self,driver):
        self.driver = driver


    def getByType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID

        elif locatorType == "xpath":
            return By.XPATH

        elif locatorType == "css":
            return By.CSS_SELECTOR

        elif locatorType == "classname":
            return By.CLASS_NAME

        elif locatorType == "linktext":
            return By.LINK_TEXT

        elif locatorType == "tagname":
            return By.TAG_NAME

        elif locatorType == "partiallinktext":
            return By.PARTIAL_LINK_TEXT

        elif locatorType == "name":
            return By.NAME

        else:
            print ("Locator Type Not Supported")
        return False


    def getElement(self, locator, locatorType="id"):

        element = None

        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print ("Element Found")

        except:
            print ("Element Not Found")

        return element


    def isElementPresent(self, locator, locatorType="id"):

        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)

            if element is not None:
                print ("Element Found")
                return True
            else:
                print("Element Not Found")
                return False

        except:
            print ("Element Not Found")
            return False



