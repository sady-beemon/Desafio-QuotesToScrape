from django.urls import path

from crawler.quotes.actions import data_request

urlpatterns = [
    path('add_quote/', data_request, name='add_quote') ,
]