from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from crawler.films.models import Movies
from crawler.quotes.models import Quotes


def first_page(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login_page.html')

def create_account(request):
    return render(request, 'create_account.html')

@login_required(login_url="/login/")
def movies_page(request):
    movies = Movies.objects.order_by('rank').only
    return render(request, 'movies_page.html', {'movies' : movies})

@login_required(login_url="/login/")
def quotes_page(request):
    quotes = Quotes.objects.order_by('content').only
    return render(request, 'quotes_page.html', {'quotes' : quotes})