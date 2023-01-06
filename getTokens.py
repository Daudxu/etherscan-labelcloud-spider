from selenium import webdriver
# import json
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import numpy as np

header = ['lableName', 'typeName', "url"]
# header = ['name','age']
data = [{'lableName':'suliang','typeName':'21'},
        {'lableName':'xiaoming','typeName':'22'},
        {'lableName':'xiaohu','typeName':'25'}]

csvData = []

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

def isTokens(accounts):
   if(accounts.find("Tokens") == 0):
      return True
   else:
      return False   

driver = webdriver.Chrome(service=s,options=options)
try:
   driver.get('https://cn.etherscan.com/labelcloud')
   time.sleep(3)
   driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
   time.sleep(2)
   rows = driver.find_elements(By.CSS_SELECTOR, 'div.row.mb-3 > div')
   print("============")
   for elm in rows:
      lableName = elm.find_element(By.TAG_NAME, "button").__getattribute__('text')
      menu = elm.find_elements(By.CSS_SELECTOR, 'div.dropdown-menu > a')
      for aElm in menu:
         menuName = aElm.get_attribute("textContent")
         menuLink = aElm.get_attribute("href")
         if(isTokens(menuName)):
            a = np.array({"lableName":lableName,"typeName": menuName, "url":menuLink})
            c = np.append(csvData, a)
            csvData = c
   print("============")
   print(len(csvData))
   print(csvData)

   with open ('tokens.csv','w',encoding='utf-8',newline='') as fp:
      writer =csv.DictWriter(fp,header)
      writer.writeheader()
      writer.writerows(csvData)
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

