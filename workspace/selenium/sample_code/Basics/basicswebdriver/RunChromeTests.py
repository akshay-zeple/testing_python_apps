#from selenium import webdriver
import selenium.webdriver

class RunChromeTests():

    def test(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('headless')

        driver = selenium.webdriver.Chrome()
        driver.get("http://get.myollie.com/profile.html")
        print(driver.title)
        driver.quit()


obj = RunChromeTests()
obj.test()



# Check you have installed latest version of chrome brwoser-> chromium-browser -version
# If not, install latest version of chrome sudo apt-get install chromium-browser

# sudo apt-get install unzip
# wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip
# unzip chromedriver_linux64.zip
# chmod +x chromedriver
# sudo mv -f chromedriver /usr/local/bin/chromedriver
# sudo chown root:root /usr/local/bin/chromedriver
# sudo chmod 0755 /usr/local/bin/chromedriver