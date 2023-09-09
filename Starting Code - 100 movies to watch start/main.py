import requests
from bs4 import BeautifulSoup
import urllib.request

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all(name='h3', class_='title')
movies = []
for title in titles:
    movies.append(title.getText())
movies.reverse()


with open('movies.txt', mode='w', encoding='utf-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")



