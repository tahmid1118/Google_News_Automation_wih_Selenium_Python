import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement
import pyperclip
import openpyxl as excel
import tkinter as t

driver = webdriver.Chrome("D:\chromedriver.exe")

driver.maximize_window()
email = 'ts.qups@gmail.com'
password = 'tahmid630!'

driver.get("https://news.google.com/")
driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[3]/div[1]/a').click()

search_email = '//*[@id="identifierId"]'
input_box = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.XPATH, search_email))
)
time.sleep(1)

pyperclip.copy(email)

input_box.send_keys(Keys.CONTROL + "v")
input_box.send_keys(Keys.ENTER)
time.sleep(5)

search_password = '//*[@id="password"]/div[1]/div/div[1]/input'
input_box = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.XPATH, search_password))
)
time.sleep(1)

pyperclip.copy(password)

input_box.send_keys(Keys.CONTROL + "v")
input_box.send_keys(Keys.ENTER)
time.sleep(1)
covid = '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div/div[5]/div[2]/a/div[2]/span'
input_box = WebDriverWait(driver, 500).until(
EC.presence_of_element_located((By.XPATH, covid))
)
input_box.click()
time.sleep(1)
savelater = '//*[@id="tabCAQqEAgAKgcICjCcuZcLMI_irgMwpbnMBg"]/div/div/main/c-wiz/div/div/main/div[1]/div[1]/div/div[2]/article/div/menu/div/div'
input_box = WebDriverWait(driver, 500).until(
EC.presence_of_element_located((By.XPATH, savelater))
)
input_box.click()
time.sleep(1)
