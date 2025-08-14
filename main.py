from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import numpy as np

#options = Options()
"""options.add_argument('--user-data-dir=/users/al/chrome3')
options.add_argument('--profile-directory=Profile 2')
options.add_argument('--lang=ja')"""
#path = r'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

driver = webdriver.Chrome()#options=options)

#sleep(2000)

driver.get("https://www.minecraft.net/ja-jp/msaprofile/mygames/editprofile")

time.sleep(3.5)

print(driver.find_element(By.XPATH, "//a[contains(text(), 'サインイン')][@aria-label='Microsoft でサインインする']"))
driver.find_element(By.XPATH, "//a[contains(text(), 'サインイン')][@aria-label='Microsoft でサインインする']").click()
#element = driver.find_element(By.XPATH, "//a[contains(text(), 'サインイン')]")
#action = webdriver.common.action_chains.ActionChains(driver)
#action.move_to_element_with_offset(element, 5, 5)
#action.click()

#.click()

time.sleep(2)

driver.find_element(By.XPATH, "//input[@type='email']").send_keys("ytakada_dc@yahoo.co.jp\n")
driver.find_element(By.XPATH, "//input[@type='email']").send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(), 'その他のサインイン方法')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(), 'パスワードを使用する')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Gatag0to")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH, "//button[contains(text(), 'はい')]").click()
time.sleep(5)

for j in range(10000000000):
    driver.get("https://www.minecraft.net/ja-jp/msaprofile/mygames/editprofile")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//input[@class='MCR_TextInput_Input']").send_keys("KAMI_kousei")
    driver.find_element(By.XPATH, "//span[contains(text(), 'プロフィール名を変更')]").click()
    time.sleep(2 ** np.random.uniform(-5, 4))
    time.sleep(0.5)
#html_source = driver.page_source
#print(html_source.split("プロフィール名"))

driver.quit()
