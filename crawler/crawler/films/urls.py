from django.urls import path
from crawler.films.actions import data_request_movie

urlpatterns = [
    path('add_movie/', data_request_movie, name='add_movie') ,
]