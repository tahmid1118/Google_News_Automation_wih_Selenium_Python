import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement
import pyperclip
import openpyxl as excel
import tkinter as tk

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
time.sleep(3)
region = '/html/body/div[4]/header/div[4]/div[2]/div/c-wiz/div/div[7]/span/div'
input_box = WebDriverWait(driver, 500).until(
        EC.presence_of_element_located((By.XPATH, region))
)
input_box.click()
time.sleep(2)

language = '/html/body/div[12]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[1]/input'
input_box = WebDriverWait(driver, 500).until(
        EC.presence_of_element_located((By.XPATH, language))
)
element = 'English (United Kingdom)'
pyperclip.copy(element)
input_box.send_keys(Keys.CONTROL + "v")
input_box.send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_class_name('VfPpkd-vQzf8d').click()
#cancel = '//*[@id="yDmH0d"]/div[13]/div[2]/div/div[2]/button[1]/div[2]'
#input_box = WebDriverWait(driver, 500).until(
 #       EC.presence_of_element_located((By.XPATH, cancel))
#)
#input_box.click()
time.sleep(2)