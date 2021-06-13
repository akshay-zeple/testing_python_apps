import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json


from browsermobproxy import Server
server = Server("/home/akshayz/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy()


mobile_emulation = {"deviceName": "iPhone 6"}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(chrome_options=chrome_options)
chrome_options.add_argument("--window-size=1920,1080")

#driver = webdriver.Chrome()

url = "http://try.starz-aso.com/index-b.html"
proxy.new_har(url, options={'captureHeaders': True, 'captureContent': True})
driver.get(url)
time.sleep(10)

har_data = json.dumps(proxy.har, indent=4)
harname = "starz-aso.har"

save_har = open(harname, 'a')
save_har.write(har_data)
save_har.close()

print(proxy.har)


server.stop()
driver.quit()