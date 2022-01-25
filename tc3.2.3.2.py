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

more = '//*[@id="ow25"]'
input_box = WebDriverWait(driver, 500).until(
EC.presence_of_element_located((By.XPATH, more))
)
input_box.click()
time.sleep(2)

gotoindependent = '//*[@id="yDmH0d"]/div[12]/div/div/span[2]/div[3]/div/div'
input_box = WebDriverWait(driver, 500).until(
EC.presence_of_element_located((By.XPATH, gotoindependent))
)
input_box.click()


