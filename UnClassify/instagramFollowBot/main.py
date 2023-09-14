from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

SIMILAR_ACCOUNT = "buzzfeedtasty"
USERNAME = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)


class InstaFollower:

    def __init__(self, option):
        self.driver = webdriver.Chrome(option)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(By.NAME, value="username")
        password = self.driver.find_element(By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        self.driver.maximize_window()
        time.sleep(2)
        followers = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div['
                                                             '1]/div[1]/div[2]/div['
                                                             '2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        try_time = 0
        while try_time < 5:
            try:
                modal = self.driver.find_element(By.XPATH, value='/html/body/div[5]/div[1]/div/div['
                                                                 '2]/div/div/div/div/div['
                                                                 '2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div['
                                                                 '2]/div/div')
            except NoSuchElementException:
                time.sleep(2)
                try_time += 1
                print(f"unable to get element try time remains {10 - try_time}")
            else:
                for i in range(10):
                    self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                    time.sleep(2)
                print("element found, process completed")
                try_time = 5

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._acan")
        print(all_buttons)
        follower_number = len(all_buttons)
        for num in range(1, follower_number):
            print(f'following {num}')
            follower_button = self.driver.find_element(By.XPATH, f"/html/body/div[5]/div[1]/div/div["
                                                                 f"2]/div/div/div/div/div[2]/div/div/div[2]/div["
                                                                 f"2]/div/div[{num}]/div/div/div/div[3]/div/button")
            follower_button.click()
            time.sleep(3)


bot = InstaFollower(chrom_options)
bot.login()
bot.find_followers()
bot.follow()
