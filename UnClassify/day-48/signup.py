from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "http://secure-retreat-92358.herokuapp.com/"
chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrom_options)
driver.get(URL)
driver.maximize_window()

element = driver.find_element(By.NAME, value="fName")
element.send_keys("Jeffrey")
element = driver.find_element(By.NAME, value="lName")
element.send_keys("Lee")
element = driver.find_element(By.NAME, value="email")
element.send_keys("123456@gmail.com")
element = driver.find_element(By.CSS_SELECTOR, value="form button")
element.click()
