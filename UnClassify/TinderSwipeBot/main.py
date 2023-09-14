from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
import time
import os

FB_EMAIL = 'YOUR FACEBOOK LOGIN EMAIL'
FB_PASSWORD = 'YOUR FACEBOOK PASSWORD'

URL = "https://tinder.com/"
chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrom_options)
driver.get(URL)
driver.maximize_window()

time.sleep(2)
accept = driver.find_element(By.XPATH, value='//*[@id="q1388042758"]/div/div[2]/div/div/div[1]/div[1]/button/div['
                                             '2]/div[2]')
accept.click()
login = driver.find_element(By.XPATH, value='//*[@id="q1388042758"]/div/div[1]/div/main/div['
                                            '1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')

time.sleep(2)
login.click()
time.sleep(5)
fb_login = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Login and hit enter
email = driver.driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)

# Delay by 5 seconds to allow page to load.
time.sleep(5)

# Allow location
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

# Disallow notifications
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

# Allow cookies
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()
