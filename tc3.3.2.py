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

driver.get("https://news.google.com/")

weatherF = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/aside/c-wiz/div/div[1]/div/footer/div/div[2]/button'
input_box = WebDriverWait(driver, 500).until(
EC.presence_of_element_located((By.XPATH, weatherF))
)
input_box.click()
time.sleep(1)


