from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login
from crawler.films.models import Movies
from crawler.films.forms import MovieForm

def movies_orderby_header(request, movies): 
    
    if request.GET.get("o"):
        ordenation = request.GET.get("o")
        print(ordenation)
        if len(ordenation.split(".")) > 1:
            for order_element in ordenation.split("."):
                movies = movies.order_by(order_element)
        else:
            movies = movies.order_by(ordenation)  
        print(movies)  
    return movies
    