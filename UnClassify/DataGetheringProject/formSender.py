from selenium import webdriver
from selenium.webdriver.common.by import By
import time

SHEET_URL = "https://docs.google.com/forms/d/e/1FAIpQLScEsjOxeIkM_2kEAEdjM4oR8JOxaUcpZ3jE8e9GNXpylXnpTg/viewform"


class FormSender:

    def __init__(self, types, bedrooms, addresses, prices, links):
        self.types = types
        self.bedrooms = bedrooms
        self.addresses = addresses
        self.prices = prices
        self.links = links

    def send_data(self, i):
        driver = webdriver.Chrome()
        driver.get(SHEET_URL)
        driver.maximize_window()
        time.sleep(2)
        data_list = [self.types[i], self.bedrooms[i], self.addresses[i], self.prices[i], self.links[i]]
        for i in range(5):
            element = driver.find_element(By.XPATH, value=f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{i+1}]/div/div/div[2]/div/div[1]/div/div[1]/input')
            element.send_keys(data_list[i])
            time.sleep(2)
        driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
        time.sleep(2)


