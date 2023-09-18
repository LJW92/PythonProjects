from bs4 import BeautifulSoup
import requests
from formSender import FormSender

HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                  'Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}
response = requests.get(url="https://zango.com.au/rent/search/?property_class=rental&listing_type=lease"
                            "&address_suburb=Dickson,%202602,%20ACT|City,%202601,%20ACT|Gungahlin,%202912,"
                            "%20ACT|Lyneham,%202602,"
                            "%20ACT&surrounding=true&bathrooms__gte=2&parking__gte=2&price__lte=750&order_by=price"
                            "&features=Dishwasher&property_status_groups=current,underOffer,"
                            "includePrivate&bathrooms__lte=2&parking__lte=2&filters=1&page=1&view_as=list",
                        headers=HEADER)
soup = BeautifulSoup(response.text, "html.parser")
link_found = soup.select("article div div a")
link_list = []
for link in link_found:
    try:
        link_buffer = link['href']
    except KeyError:
        continue
    else:
        if "agencies" in link_buffer or link_buffer in link_list or "agents" in link_buffer:
            continue
        else:
            link_list.append(link_buffer)


address_found = soup.select("article div div div div h3")
address_list = []
for address in address_found:
    address_list.append(address.text)

price_found = soup.select("article div div div div a h4")
price_list = []
for price in price_found:
    price_tag = price.text
    price_tag = price_tag.replace("pw", " ")
    price_tag = price_tag.replace("/", " ")
    price_tag = price_tag.replace("$", " ")
    price_list.append(price_tag.split(" ")[1])

bedroom_found = soup.select(".icon-bed ~ span")
bedroom_list = []
for beds in bedroom_found:
    bedroom_list.append(beds.text)

type_found = soup.select(".lytDK span")
type_list = []
for types in type_found:
    type_list.append(types.getText())

sender = FormSender(type_list, bedroom_list, address_list, price_list, link_list)
for i in range(len(link_list)):
    sender.send_data(i)


