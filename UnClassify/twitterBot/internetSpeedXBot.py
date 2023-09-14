from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

SPEED_TEST_URL = "https://www.speedtest.net/"
X_URL = "https://twitter.com/"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrom_options = webdriver.ChromeOptions()
        self.chrom_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrom_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                 '1]/a/span[4]').click()
        timeout = 0
        while timeout < 45:
            time.sleep(1)
            if timeout % 5 == 0:
                print(f"{timeout} seconds passed")
            timeout += 1
        down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                        '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div['
                                                        '2]/span').text
        up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                      '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                      '2]/div/div[2]/span').text
        self.driver.quit()
        self.down = float(down)
        self.up = float(up)
        return [self.down, self.up]

    def tweet_at_provider(self, email: str, password: str):
        time.sleep(2)
        driver = webdriver.Chrome(self.chrom_options)
        driver.get(X_URL)
        driver.maximize_window()
        driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div['
                                            '1]/div/div[3]/div[5]/a/div').click()
        time.sleep(2)
        login_user = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div['
                                                         '2]/div[2]/div/div/div[2]/div[2]/div/div/div/div['
                                                         '5]/label/div/div[2]/div/input')
        login_user.send_keys(email)
        login_user.send_keys(Keys.ENTER)

        time.sleep(2)

        login_password = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div['
                                                             '2]/div[2]/div/div/div[2]/div[2]/div['
                                                             '1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        login_password.send_keys(password)
        login_password.send_keys(Keys.ENTER)
        tweet = f"Hey my Internet Provider, my internet speed is {self.down}Mbps down/ {self.up}Mbps up."
        post_div = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                       '2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div['
                                                       '1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div['
                                                       '2]/div/div/div/div/label/div[1]/div/div/div/div/div/div['
                                                       '2]/div/div/div/div')
        post_div.send_keys(tweet)
        driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                            '1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div['
                                            '2]/div/div/div[2]/div[3]/div/span/span').click()

        print("post has been sent")
