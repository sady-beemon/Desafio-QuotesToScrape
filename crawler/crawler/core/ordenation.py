from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login
from crawler.films.models import Movies
from crawler.films.forms import MovieForm

def movies_header_ordenation(request, movies): 
    
    if request.GET.get("input_header_element_rank"):
        movies = movies.order_by(request.GET.get("input_header_element_rank"))
    
    if (request.GET.get("input_header_element_title")):
        movies = movies.order_by(request.GET.get("input_header_element_title"))

    if (request.GET.get("input_header_element_date")):
        movies = movies.order_by(request.GET.get("input_header_element_date"))

    if (request.GET.get("input_header_element_time")):
        movies = movies.order_by(request.GET.get("input_header_element_time"))

    if (request.GET.get("input_header_element_minage")):
        movies = movies.order_by(request.GET.get("input_header_element_minage"))

    if (request.GET.get("input_header_element_score")):
        movies = movies.order_by(request.GET.get("input_header_element_score"))
    
    return movies
    