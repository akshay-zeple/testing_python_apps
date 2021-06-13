from selenium import webdriver
import time


class SwitchToWindow():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        parentHandle = driver.current_window_handle
        print ("Parent Window Handle - "+parentHandle)

        driver.find_element_by_id("openwindow").click()

        handles = driver.window_handles
        for handle in handles:
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print ("Switched to window handle - "+handle)
                driver.find_element_by_id("search-courses").send_keys("python")
                time.sleep(5)
                driver.close()
                break

        driver.switch_to.window(parentHandle)
        driver.find_element_by_id("name").send_keys("Name")
        print("Switched to Parent window - "+parentHandle)
        time.sleep(5)

obj = SwitchToWindow()
obj.test()