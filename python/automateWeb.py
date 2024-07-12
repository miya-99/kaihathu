# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

options = Options()
options.use_chromium = True
options.headless = True

service_args = ['--verbose']

browser = webdriver.Edge(
  executable_path='msedgedriver.exe',
  options=options,
  # service_args = service_args,
  # service_log_path=service_log_path,
  # verbose=True
  )

browser.implicitly_wait(10) 
browser.get('{target url}')
   # 省略