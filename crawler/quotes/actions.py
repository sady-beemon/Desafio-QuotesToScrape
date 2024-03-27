from bs4 import BeautifulSoup
from quotes.models import Quotes
import requests


def data_request():
    r = requests.get('https://quotes.toscrape.com/')
    soup = BeautifulSoup(r.text,"html.parser")
    tags = soup.find_all(class_ = "quote")
    for tag in tags:
        Quotes.objects.create(
            content = (tag.find(class_ = "text")).get_text(),
            creator = (tag.find(class_ = "author")).get_text(),
            tags = (tag.find(class_ = "tags")).get_text(),
        )