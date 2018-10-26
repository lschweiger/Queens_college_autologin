#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import requests
import getpass
import selenium 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
options = Options()
options.set_headless(headless=True)
driver =selenium.webdriver.Firefox(firefox_options=options,executable_path='/usr/bin/geckodriver')
driver.get("https://qwifi.qc.cuny.edu/guest/qc-web-login.php?_browser=1")


username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

username.send_keys("username")
password.send_keys("password")

driver.find_element_by_id("ID_form66f3c09a_weblogin_submit").click()
driver.quit()
