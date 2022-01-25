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
showurl = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div[3]/div/div/article/div/menu/span[1]/div'
input_box = WebDriverWait(driver, 500).until(
EC.presence_of_element_located((By.XPATH, showurl))
)
input_box.click()
time.sleep(1)

shareurl = '//*[@id="yDmH0d"]/div[12]/div[2]/div/div/div[3]/div[2]/div[1]/button/span'
input_box = WebDriverWait(driver, 500).until(
EC.presence_of_element_located((By.XPATH, shareurl))
)
input_box.click()
root = tk.Tk()
root.withdraw()
d = root.clipboard_get()
print(d)
time.sleep(1)
driver.execute_script(f"window.open('{d}');")
