from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time


options = Options()
options.add_argument(r"user-data-dir=C:\Users\Suppo\AppData\Local\Google\Chrome\User Data\profile 4")
# options.add_argument("--kiosk") # This will maximize window like F11
options.add_experimental_option("excludeSwitches", ["enable-automation"])
s = Service(r"C:\chromedriver.exe")
driver = Chrome(service=s, options=options)

driver.execute_script("window.open('http://radiusdesk2.cloudconnexions.ca:81/');")
time.sleep(5)
# username = driver.find_element(By.NAME, "username")
username = driver.find_element(by=By.ID, value='textfield-1013-inputEl')
# username.send_keys('raman')
print(username)
# password = driver.find_element_by_name('pass')
# password.send_keys('Xidex2o2o')
#
# form = driver.find_element('loginForm')
# form.submit()


# driver.quit() # Close windows
