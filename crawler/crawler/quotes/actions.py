from django.http import HttpResponseRedirect
from django.contrib import messages
from crawler.quotes.models import Quotes
from bs4 import BeautifulSoup

import requests


def data_request_quotes(request):

    page_number = 1
    soup = get_page_content(page_number)

    while "No quotes found!" not in soup.get_text():
        
        tags_on_page = soup.find_all(class_ = "quote")
        for tag in tags_on_page:
            Quotes.objects.get_or_create(
                content = (tag.find(class_ = "text")).get_text(),
                creator = (tag.find(class_ = "author")).get_text(),
                tags = (tag.find(class_ = "tags")).get_text(),
            )
    
        page_number += 1
        soup = get_page_content(page_number)
    messages.success(request,"Dados adicionados com sucesso.")
    return HttpResponseRedirect(request.headers['Referer'])
    

def get_page_content(page_number):
    r = requests.get(f'https://quotes.toscrape.com/page/{page_number}')
    soup = BeautifulSoup(r.text,"html.parser")
    return soup


"""
    Para cada pagina obter todos os elementos com a classe 'Quote'.
    Caso a pagina exiba o texto 'No quotes found!' significa que coletamos todas as frases.
"""