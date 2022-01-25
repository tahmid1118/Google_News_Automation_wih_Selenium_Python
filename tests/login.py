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
import unittest
from pages.loginpage import Loginpage


class Logintest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("D:\chromedriver.exe")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://news.google.com/")
        login = Loginpage(driver)
        login.signin_button()
        time.sleep(1)
        login.enter_email('ts.qups@gmail.com')
        time.sleep(1)
        login.next_button()
        time.sleep(2)
        login.enter_password('tahmid630!')
        time.sleep(1)
        login.click_login()

    @classmethod
    def 

