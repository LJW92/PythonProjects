from bs4 import BeautifulSoup
import requests
import smtplib

my_email = 'lijiaweipython@gmail.com'
password = 'ajnqjljoqbhfhcuu'

PRODUCT_URL = "https://www.amazon.com.au/Philips-Technology-Champagne-HD9870-20/dp/B09T656FPB/ref" \
              "=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=xJ3oN&content-id=amzn1.sym.a9ee0d91-6c12-4994-a4cb-a9802f05e73c" \
              "%3Aamzn1.symc.409c7fce-cbd2-4cf4-a6cb-824c258c8778&pf_rd_p=a9ee0d91-6c12-4994-a4cb-a9802f05e73c" \
              "&pf_rd_r=3A7QNSX0TW20WPTX3EE9&pd_rd_wg=IDUbt&pd_rd_r=c790c0bb-73c2-4056-b02c-02d90e706451&pd_rd_i" \
              "=B09T656FPB"

HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                  'Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

response = requests.get(PRODUCT_URL, headers=HEADER)
Amazon_web = response.text
soup = BeautifulSoup(Amazon_web, "lxml")
price = soup.find(name="span", class_="a-price-whole")
price = price.getText().split('.')[0]

if int(price) < 300:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f'Philips Premium Air Fryer XXL with Smart Sensing Technology HD9870/20 (White), '
                                f'price now ${price}'
                            )

