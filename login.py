#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 14:26:05 2018

@author: launy
"""

import requests
import getpass
import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver =selenium.webdriver.Firefox(executable_path='/usr/bin/geckodriver')
driver.get("https://qwifi.qc.cuny.edu/guest/qc-web-login.php?_browser=1")


username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

username.send_keys("username")
password.send_keys("password")

driver.find_element_by_id("ID_form66f3c09a_weblogin_submit").click()
driver.quit()