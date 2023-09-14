import os
from internetSpeedXBot import InternetSpeedTwitterBot

PROMISED_DOWN = 55
PROMISED_UP = 20
X_EMAIL = os.environ.get("EMAIL")
X_PASSWORD = os.environ.get("PASSWORD")

x_bot = InternetSpeedTwitterBot()

down_up_speed = x_bot.get_internet_speed()

if down_up_speed[0] < PROMISED_DOWN or down_up_speed[1] < PROMISED_UP:
    x_bot.tweet_at_provider(X_EMAIL, X_PASSWORD)





