from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
URL = "https://en.wikipedia.org/wiki/Main_Page"
# Keep Chrome browser open after program finishes
chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrom_options)
driver.get(URL)
driver.maximize_window()
# element = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# element.click()

# element = driver.find_element(By.LINK_TEXT, value='Commons')
# element.click()
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


