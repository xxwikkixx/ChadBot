import os
import sys
import fnmatch
import shutil
import time
import config as cfg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

pathOfFilesDled = r'C:\\Users\\ChadBot\\Downloads\\'
pathToMoveDLStocks = r'C:\\Users\\ChadBot\\Desktop\\ChadBot\\barchart\\Stocks\\'
pathToMoveDLETF = r'C:\\Users\\ChadBot\\Desktop\\ChadBot\\barchart\\ETF\\'
pathToMoveDLIndices= r'C:\\Users\\ChadBot\\Desktop\\ChadBot\\barchart\\Indices\\'

def dlData():
    chrome_options = Options()
    # chrome_options.add_argument("start-minimized")
    driver = webdriver.Chrome(r'C:\chromedriver.exe', options=chrome_options)
    driver.get("https://www.barchart.com/login")
    element = driver.find_element_by_name("email")
    element.send_keys(cfg.login['user'])
    element = driver.find_element_by_name("password")
    element.send_keys(cfg.login['pass'])
    element.send_keys(Keys.RETURN)
    driver.get("https://www.barchart.com/options/unusual-activity/stocks")
    print("stocks")
    driver.find_element_by_xpath("//span[contains(.,'download')]").click()
    time.sleep(5)
    driver.get("https://www.barchart.com/options/unusual-activity/etfs")
    print("etfs")
    driver.find_element_by_xpath("//span[contains(.,'download')]").click()
    time.sleep(5)
    driver.get("https://www.barchart.com/options/unusual-activity/indices")
    print("Indices")
    driver.find_element_by_xpath("//span[contains(.,'download')]").click()
    time.sleep(5)
    driver.quit()

def sortData():
    # Open dir where the data is downloaded
    # search for file with .csv 
    # search for etf, stocks, indices
    for f_name in os.listdir(pathOfFilesDled):
        if fnmatch.fnmatch(f_name, '*-etfs-*-*-*-*-*.csv'):
            try:
                shutil.move(pathOfFilesDled + f_name, pathToMoveDLETF)
                print("File Moved: " + f_name)
            except IOError:
                print("Could not move files")
                sys.exit()
        if fnmatch.fnmatch(f_name, '*-indices-*-*-*-*-*.csv'):
            try:
                shutil.move(pathOfFilesDled + f_name, pathToMoveDLIndices)
                print("File Moved: " + f_name)
            except IOError:
                print("Could not move files")
                sys.exit()
        if fnmatch.fnmatch(f_name, '*-stocks-*-*-*-*-*.csv'):
            try:
                shutil.move(pathOfFilesDled + f_name, pathToMoveDLStocks)
                print("File Moved: " + f_name)
            except IOError:
                print("Could not move files")
                sys.exit()

if __name__ == "__main__":
    # dlData()
    # sortData()
    print("Test")
    sys.exit()
        