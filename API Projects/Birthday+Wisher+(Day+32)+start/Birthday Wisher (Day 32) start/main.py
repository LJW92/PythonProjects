import smtplib
import datetime as dt
import random

my_email = 'lijiaweipython@gmail.com'
password = 'ajnqjljoqbhfhcuu'


def send_motivation(quote_to_send):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='lijiaweipython@yahoo.com',
                            msg=f'Subject:Motivation of the day\n\n{quote_to_send}'
                            )


working_day = [0, 1, 2, 3, 4]
now = dt.datetime.now()
today = now.weekday()

with open('quotes.txt') as file:
    contents = file.readlines()
    quote = random.choice(contents)

if today in working_day:
    send_motivation(quote)
