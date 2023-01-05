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

header = ['labelName', 'tabType', "address", "nameTag"]

s = Service(r"E:/webroot/etherscan-labelcloud-spider/b/chromedriver.exe")

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

labelName = "uniswap-01"

def isAccounts(accounts):
   # print("accounts:"+ accounts )
   # print(accounts.find("Accounts"))
   if(accounts.find("Accounts") == 0):
      return True
   else:
      return False

def getData(labelName, tabType):
      labelData = []
      trRows = driver.find_elements(By.CSS_SELECTOR, 'tbody > tr')
      for elm in trRows:
            tdRow = elm.find_elements(By.TAG_NAME, 'td')
            if len(tdRow) == 4:
               address = tdRow[0].find_element(By.TAG_NAME, "a").get_attribute('text')    
               print(address)    
               nameTag = tdRow[1].text
               a = np.array({"labelName":labelName, "tabType":tabType, "address":address, "nameTag": nameTag})
               labelData = np.append(labelData, a)
      return labelData


try:

   url = "https://etherscan.io/accounts/label/uniswap?subcatid=0&size=10000&start=30000&col=1&order=asc"
   
   driver.get(url)
   driver.add_cookie({'name': 'etherscan_userid','value':'xudan'})
   driver.add_cookie({'name': 'etherscan_pwd','value':'4792:Qdxb:kAl5dq9QnbrN3OxZFxuZnHQBcXDgRiLPAh4qslPrI/0='})
   driver.add_cookie({'name': 'etherscan_autologin','value': 'True'})
   driver.add_cookie({'name': '_pk_ses.10.1f5c','value': '1'})
   driver.add_cookie({'name': '_pk_id.10.1f5c','value': 'ca79f049ddc3dd47.1672822063.'})
   driver.add_cookie({'name': '__stripe_mid','value': '1a324d7d-a5dd-4d7e-9a58-f81f60f6ad787259ab'})
   driver.add_cookie({'name': '__cf_bm','value': 'ZnFT6s.oztCGMeFNuzJvpbT4UGm.L1Nw5RfSVTnSxXk-1672885917-0-ARUSsUwJKiexo6Dp06qFUCcms3QMfUZ/wLdycGip+dxrZI76cvNmhWbBMNxkZCea9hp1ptkhAJVQO+LEhfZWeW16nJRcepK914jvl2B1xpFFYxRbggVUGwEDeKFihNGzf7wV6yP7ys0HSJwrekGw09g='})
   driver.add_cookie({'name': 'ASP.NET_SessionId','value': 'qqou3ohtv3iuj0cxoyqsw2re'})
   driver.refresh()



   print("正在获取:"+url+" 数据...")
   
   tabType = "Others"
   labelData = getData(labelName, tabType)
   with open ("./labelcloud/"+labelName+'.csv','w',encoding='utf-8',newline='') as fp:
      writer =csv.DictWriter(fp,header)
      writer.writeheader()
      writer.writerows(labelData)
      print("完成存储")
     
     
   driver.quit()
finally:
   driver.quit()
print("dene")

