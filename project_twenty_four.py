from bs4 import BeautifulSoup
import requests
import pyttsx3
url = "https://otakumode.com/news/anime"
get = requests.get(url).text
soup = BeautifulSoup(get,"html.parser")
news = soup.find_all("div",attrs={"class":"p-article-list__body"})

for new in news[8:]:
    print(f"{new.text}\n")
