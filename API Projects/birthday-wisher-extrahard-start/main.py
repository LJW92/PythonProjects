import datetime as dt
import random
import smtplib
import pandas

my_email = 'lijiaweipython@gmail.com'
password = 'ajnqjljoqbhfhcuu'


def send_birthday_letter():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_to_send,
                            msg=f'Subject:Happy Birthday {name}\n\n{new_letter}'
                            )


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
month_now = today.month
day_now = today.day

data = pandas.read_csv('birthdays.csv')
birthday_dict = data.to_dict(orient='records')
name = ''
for row in birthday_dict:
    if row['month'] == month_now and row['day'] == day_now:
        name = row['name']
        email_to_send = row['email']

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
letter_list = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
if name != '':
    with open(f'letter_templates/{random.choice(letter_list)}') as file_letter:
        letter = file_letter.read()
        new_letter = letter.replace('[NAME]', name)
# 4. Send the letter generated in step 3 to that person's email address.
        send_birthday_letter()
        name = ''
