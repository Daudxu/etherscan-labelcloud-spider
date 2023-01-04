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
import codecs
import csv

header = ['lableName', 'typeName', "url"]
# header = ['name','age']
data = [{'lableName':'suliang','typeName':'21'},
        {'lableName':'xiaoming','typeName':'22'},
        {'lableName':'xiaohu','typeName':'25'}]

csvData = [
   "https://cn.etherscan.com/accounts/label/alchemist-coin",
   "https://cn.etherscan.com/accounts/label/alchemix-finance",
   "https://cn.etherscan.com/accounts/label/allbit",
]

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

driver = webdriver.Chrome(service=s,options=options)

def isAccounts(accounts):
   # print("accounts:"+ accounts )
   # print(accounts.find("Accounts"))
   if(accounts.find("Accounts") == 0):
      return True
   else:
      return False

def getData():
      # print("abc")
      trRows = driver.find_elements(By.CSS_SELECTOR, 'tbody > tr')
      for elm in trRows:
            tdRow = elm.find_elements(By.TAG_NAME, 'td')
            # print(len(tdRow))
            if len(tdRow) == 4:
               address = tdRow[0].find_element(By.TAG_NAME, "a").get_attribute('text')        
               addressDetailsLink = tdRow[0].find_element(By.TAG_NAME, "a").get_attribute('href')
               nameTag = tdRow[1].text
               balance = tdRow[2].text
               txnCount = tdRow[3].text
               print("============")
               print("address: " +address+ " addressDetailsLink: " +addressDetailsLink+ "nameTag: " + nameTag + " balance" + balance + "txnCount" + txnCount )
               print("============")


try:
   # salary = input('请输入1：') 
   # print('run...' + salary )
   with codecs.open('./information.csv', encoding='utf-8-sig') as f:
      for row in csv.reader(f, skipinitialspace=True):
         
         print(row[2])
         driver.get(row[2]+"?size=10000")
         driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
         time.sleep(3)

      # # driver.get('https://cn.etherscan.com/accounts/label/airdrop-hunter?size=100')
      # # driver.get('https://cn.etherscan.com/accounts/label/balancer?subcatid=1&size=5000')
      # # driver.get('https://cn.etherscan.com/accounts/label/0x-protocol?subcatid=1&size=5000')


         rows = driver.find_elements(By.CSS_SELECTOR, 'ul.nav.nav-custom.nav-borderless.nav_tabs > li')
         if (len(rows) > 0):
         #  for elm in rows:
            print("执行获取多tab数据")
            for i in range(len(rows)):
               if(i == 0):
                  print("走到第一步...")
                  getData()
               elif(i == 1):
                  print("走到第二步...")
                  driver.get(row[2]+'?subcatid=3-0&size=10000')
                  time.sleep(5)
                  getData()
               elif(i == 2):
                  print("走到第三步...")
                  driver.get(row[2]+'?subcatid=2&size=10000')
                  time.sleep(5)
                  getData()
            print(1111)
            # driver.quit()
         else:
            print("执行获取无tab数据")
            getData()
   driver.quit()
finally:
   driver.quit()
print("dene")

