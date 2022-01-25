import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement
import pyperclip
import openpyxl as excel

driver = webdriver.Chrome("D:\chromedriver.exe")

driver.maximize_window()

driver.get("https://news.google.com/")

driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]').click()
time.sleep(1)
featured_topic = '/html/body/div[4]/header/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[2]'
search_box = WebDriverWait(driver, 500).until(
EC.presence_of_element_located((By.XPATH, featured_topic))
)
search_box.click()

driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]').click()
time.sleep(1)
letest_news = '/html/body/div[4]/header/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[2]/div/div/div[4]/div/div/div/div[2]'
search_box = WebDriverWait(driver, 500).until(
EC.presence_of_element_located((By.XPATH, latest_news))
)
latest_news.click()
