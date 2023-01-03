from selenium import webdriver
import json
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
s = Service(r"C:/Users/dan/Desktop/spider/chromedriver.exe")

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

d = webdriver.Chrome(service=s,options=options)
try:
   d.get('https://cn.etherscan.com/labelcloud')
   title = d.title
   jsonString = '{"title": "%s"}' % title
   file = open('data.json', 'w')
   file.write(jsonString)
   file.close()
   d.quit()
finally:
   d.quit()
print("dene")

#  获取labelcloud 页面数据
def getLabelcloudList():
    print("获取labelcloud 页面数据")
#  获取accounts 页面数据
def getDetails():
    print("获取accounts 页面数据")
