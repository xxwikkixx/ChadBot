from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


def dlData():
    chrome_options = Options()
    # chrome_options.add_argument("start-minimized")
    driver = webdriver.Chrome(r'C:\chromedriver.exe', options=chrome_options)
    user_name = ''
    password = ''
    driver.get("https://www.barchart.com/login")
    element = driver.find_element_by_name("email")
    element.send_keys(user_name)
    element = driver.find_element_by_name("password")
    element.send_keys(password)
    element.send_keys(Keys.RETURN)
    driver.get("https://www.barchart.com/options/unusual-activity/stocks")
    driver.find_element_by_xpath("//span[contains(.,'download')]").click()
    driver.get("https://www.barchart.com/options/unusual-activity/etfs")
    print("etfs")
    driver.find_element_by_xpath("//span[contains(.,'download')]").click()
    driver.get("https://www.barchart.com/options/unusual-activity/indices")
    print("Indices")
    driver.find_element_by_xpath("//span[contains(.,'download')]").click()
    driver.quit()

def sortData():
    pass

if __name__ == "__main__":
     print("test")