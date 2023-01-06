from seleniumbase import Driver
from seleniumbase import page_actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = Driver(uc=True)
wait = WebDriverWait(driver, 20)
url = 'https://cn.etherscan.com/tokens/label/0x-protocol'
driver.get(url)
# time.sleep(10)
rows =  driver.find_elements(By.CSS_SELECTOR, 'tbody > tr')
print(len(rows))
# wait.until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(password)
print("You're in!! enjoy")
