from selenium import webdriver
# import json
# from bs4 import BeautifulSoup
# import sys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# import csv
# import numpy as np

s = Service(r"E:/webroot/etherscan-labelcloud-spider/chromedriver.exe")

options = Options()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--disable-extentions') 
# options.add_argument("--proxy-server='direct://'")
# options.add_argument('--proxy-bypass-list=*')
options.add_argument('--start-maximized')
options.add_argument('--disable-gpu')
options.add_argument('--no--sandbox')
options.add_argument('--log-level=3')

def isAccounts(accounts):
   # print("accounts:"+ accounts )
   # print(accounts.find("Accounts"))
   if(accounts.find("Accounts") == 0):
      return True
   else:
      return False   

driver = webdriver.Chrome(service=s,options=options)
try:
#    driver.get('https://cn.etherscan.com/accounts/label/balancer?subcatid=1&size=100000&start=0&col=1&order=asc')
   driver.get('https://cn.etherscan.com/accounts/label/0x-protocol-ecosystem?subcatid=undefined&size=100&start=0&col=1&order=asc')
#    salary = input('请输入1：') 
#    print('run...' + salary )
   time.sleep(3)
   driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
   time.sleep(2)
   rows = driver.find_elements(By.CSS_SELECTOR, 'ul.nav.nav-custom.nav-borderless.nav_tabs > li')
   if (len(rows) > 0):
      print("执行获取多tab数据")
    #   获取 TAB 名称数量以及 url
   else:
      trRows = driver.find_elements(By.CSS_SELECTOR, 'tbody > tr')
      for trDoc in trRows:
        tdRow = trDoc.find_elements(By.CSS_SELECTOR, 'td')

      #   for tdDoc in tdRow:
      #       str =  tdDoc.text
      #       str1 =  tdDoc.find_elements(By.CSS_SELECTOR, 'a').__getattribute__("href")
        # address = tdRow[0].text
        # link = tdRow[0].find_elements(By.CSS_SELECTOR, 'a').__getattribute__("inerHTML")
        # print("抓取没有tab 数据")
        # print("address:" + address )
            # print(str1)

   print("============")
   print(len(rows))
   print("============")

   driver.quit()
finally:
   driver.quit()
print("dene")

#  获取labelcloud 页面数据
def getLabelcloudList():
    print("获取labelcloud 页面数据")
#  获取accounts 页面数据
def getDetails():
    print("获取accounts 页面数据")

