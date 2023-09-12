from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"
chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrom_options)
driver.get(URL)
driver.maximize_window()

cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')
money = driver.find_element(By.XPATH, value='//*[@id="money"]')
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 60 * 60 * 10  # 5 minutes from now
while True:
    timeout_inner_loop = time.time() + 5
    if time.time() > timeout:
        break
    else:
        while True:
            if time.time() > timeout_inner_loop:
                break
            else:
                cookie.click()

    money_str = money.text.replace(",", "")
    money_int = int(money_str)
    all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    item_prices = []
    for price in all_prices:
        element_text = price.text
        if element_text != "":
            cost = int(element_text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)

    cookie_upgrades = {}
    for n in range(len(item_prices)):
        cookie_upgrades[item_prices[n]] = item_ids[n]

    affordable_upgrades = {}
    for cost, id in cookie_upgrades.items():
        if money_int > cost:
            affordable_upgrades[cost] = id
    try:
        highest_price_affordable_upgrade = max(affordable_upgrades)
    except ValueError:
        continue
    else:
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element(By.ID, value=to_purchase_id).click()
