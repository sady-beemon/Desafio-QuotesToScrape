from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from crawler.films.models import Movies
from crawler.quotes.models import Quotes
from crawler.films.forms import MovieForm
from crawler.quotes.forms import QuotesForm

from crawler.films.actions import data_request_movie
from crawler.quotes.actions import data_request_quotes


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

def movies_edit(request, pk):

    movie = get_object_or_404(Movies, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            messages.success(request, "Pagina atualizada com sucesso")
            return redirect('movies_page')
        else:
            return render(request, 'movies_edit.html', {'form': form})
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies_edit.html', {'form': form})

def movies_new(request):

    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            messages.success(request, "Pagina atualizada com sucesso")
            return redirect('movies_page')
        else:
            return render(request, 'movies_new.html', {'form': form})
    else:
        form = MovieForm()
    return render(request, 'movies_new.html', {'form': form})

def movies_run_crawler(request):
    data_request_movie(request)
    messages.success(request, "Todos os top 250 filmes adcionados com sucesso.")
    return redirect('movies_page')




@login_required(login_url="/login/")
def quotes_page(request):
    quotes = Quotes.objects.order_by('content').only
    return render(request, 'quotes_page.html', {'quotes' : quotes})

def quotes_edit(request, pk):

    quote = get_object_or_404(Quotes, pk=pk)
    if request.method == "POST":
        form = QuotesForm(request.POST, instance=quote)
        if form.is_valid():
            quote = form.save()
            messages.success(request, "Item atualizado com sucesso")
            return redirect('quotes_page')
        else:
            return render(request, 'quotes_edit.html', {'form': form})
    else:
        form = QuotesForm(instance=quote)
    return render(request, 'quotes_edit.html', {'form': form})

def quotes_new(request):

    if request.method == "POST":
        form = QuotesForm(request.POST)
        if form.is_valid():
            quote = form.save()
            messages.success(request, "Item atualizado com sucesso")
            return redirect('quotes_page')
        else:
            return render(request, 'quotes_new.html', {'form': form})
    else:
        form = QuotesForm()
    return render(request, 'quotes_new.html', {'form': form})

def quotes_run_crawler(request):
    data_request_quotes()
    messages.success(request, "quotes adcionados com sucesso.")
    return redirect('quotes_page')