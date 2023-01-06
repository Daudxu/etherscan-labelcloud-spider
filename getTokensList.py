from selenium import webdriver
# import json
# from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import numpy as np
import codecs
import csv
import re
import math

header = ['labelName', "address", "addressLink", "tokenName", "tokenNameLink"]

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
   if(accounts.find("Accounts") == 0):
      return True
   else:
      return False

def getData(labelName):
      labelData = []
      trRows = driver.find_elements(By.CSS_SELECTOR, 'tbody > tr')
      for elm in trRows:
            tdRow = elm.find_elements(By.TAG_NAME, 'td')
            if len(tdRow) == 6:
               address = tdRow[1].find_element(By.TAG_NAME, "a").get_attribute('text')    
               addressLink = tdRow[1].find_element(By.TAG_NAME, "a").get_attribute('href')    
               tokenName = tdRow[2].find_element(By.TAG_NAME, "a").get_attribute('text') 
               tokenNameLink = tdRow[1].find_element(By.TAG_NAME, "a").get_attribute('href') 
               print(address)
               a = np.array({"labelName":labelName, "address":address, "addressLink":addressLink, "tokenName": tokenName , "tokenNameLink":tokenNameLink})
               labelData = np.append(labelData, a)
      return labelData

def saveData(labelName, data):
         with open ("./labelcloud/"+labelName+'.csv','w',encoding='utf-8',newline='') as fp:
                writer =csv.DictWriter(fp,header)
                writer.writeheader()
                writer.writerows(data)
                print("Finish Done")

try:
   driver.get('https://cn.etherscan.com/labelcloud')
   a = input("enter")
   # 设置登录态
   driver.add_cookie({'name': 'etherscan_userid','value':'xudan'})
   driver.add_cookie({'name': 'etherscan_pwd','value':'4792:Qdxb:kAl5dq9QnbrN3OxZFxuZnHQBcXDgRiLPAh4qslPrI/0='})
   driver.add_cookie({'name': 'etherscan_autologin','value': 'True'})
   driver.add_cookie({'name': '_pk_ses.10.1f5c','value': '1'})
   driver.add_cookie({'name': '_pk_id.10.1f5c','value': 'ca79f049ddc3dd47.1672822063.'})
   driver.add_cookie({'name': '__stripe_mid','value': '1a324d7d-a5dd-4d7e-9a58-f81f60f6ad787259ab'})
   driver.add_cookie({'name': '__cf_bm','value': 'ZnFT6s.oztCGMeFNuzJvpbT4UGm.L1Nw5RfSVTnSxXk-1672885917-0-ARUSsUwJKiexo6Dp06qFUCcms3QMfUZ/wLdycGip+dxrZI76cvNmhWbBMNxkZCea9hp1ptkhAJVQO+LEhfZWeW16nJRcepK914jvl2B1xpFFYxRbggVUGwEDeKFihNGzf7wV6yP7ys0HSJwrekGw09g='})
   driver.add_cookie({'name': 'ASP.NET_SessionId','value': 'qqou3ohtv3iuj0cxoyqsw2re'})
   # 刷新页面
   driver.refresh()

   with codecs.open('./tokens.csv', encoding='utf-8-sig') as f:
      for row in csv.reader(f, skipinitialspace=True):
        print("runner:"+row[2])
        url = row[2]
        driver.get(url+"?size=100&start=0")
        time.sleep(3)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        labelNameStr = row[0].replace('/', '-')
        labelNameStrQue = labelNameStr.replace('?', '-')
        labelName = ''.join([i for i in labelNameStrQue if not i.isdigit()])
        tokenCount = re.findall(r'[(](.*?)[)]',row[1])
        dataCount = int(tokenCount[0])
        if dataCount > 100:
            pageSize = dataCount / 100
            pageSize = math.ceil(pageSize)
            mergeDate = []
            for item in range(pageSize):
            #    print(item)
                pageLimt = int(item)*100
                pageUrl = url+"?size=100&start="+ str(pageLimt)
                driver.get(pageUrl)
                time.sleep(3)
                print("=========")
                print(pageUrl)
                resData = getData(labelName)
                mergeDate = np.concatenate((mergeDate, resData))   
                print("=========")
            saveData(labelName, mergeDate)
        else:
            resData = getData(labelName)
            saveData(labelName, resData)
                   
   driver.quit()
finally:
   driver.quit()
print("dene")