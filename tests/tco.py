import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement
import pyperclip
import openpyxl as excel
from pages.loginpage import Loginpage
from pages.homepage import Homepage
import unittest

class TCC(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("D:\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://news.google.com/")

    def test_case(self):
        driver = self.driver
        tec = Homepage(driver)
        tec.goto_featured_topic()
        time.sleep(2)

