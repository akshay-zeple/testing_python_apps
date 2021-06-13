from selenium import webdriver

class BrowserInteractions():

    def test(self):

        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get(baseUrl)

        title = driver.title
        print (title)

        currentUrl = driver.current_url
        print (currentUrl)

        driver.refresh()

        driver.get(driver.current_url)

        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")

        driver.back()

        driver.forward()

        pageSource = driver.page_source

obj = BrowserInteractions()
obj.test()

