from bs4 import BeautifulSoup
from quotes.models import Quotes
import requests


def data_request():
    r = requests.get('https://quotes.toscrape.com/')
    soup = BeautifulSoup(r.text,"html.parser")
    tags = soup.find_all(class_ = "quote")
    for tag in tags:
        # Crie um dicionario com cada tag
        # Crie um Quote com o dict (dica pode passar como **kwargs)
        Quotes.objects.create(
            content = (tag.find(class_ = "text")).get_text(),
            creator = (tag.find(class_ = "author")).get_text(),
            tags = (tag.find(class_ = "tags")).get_text(),
            
        )

def single_request():
    r = requests.get('https://quotes.toscrape.com/')
    soup = BeautifulSoup(r.text,"html.parser")
    Quotes.objects.create(
        content = (soup.find(class_ = "text")).get_text(),
        creator = (soup.find(class_ = "author")).get_text(),
        tags = (soup.find(class_ = "tags")).get_text(),
    
        
    )
