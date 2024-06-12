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
    movies = Movies.objects.all()

    year_filter_get = request.GET.get("year_picker")
    score_filter_get = request.GET.get("score_picker")
    search_field_get = request.GET.get("search_field")
    minage_selector = request.GET.get("minage_selector")

    if year_filter_get:    
        year_filter_start, year_filter_end  = year_filter_get.split(" - ")
        if year_filter_start and year_filter_end:
            gte_lte = {
                'date__gte': year_filter_start,
                'date__lte': year_filter_end,
            }

            movies = movies.filter(**gte_lte)

    if score_filter_get:
        score_filter_start, score_filter_end  = score_filter_get.split(" - ")
        if score_filter_start and score_filter_end:
            gte_lte = {
                'score__gte': score_filter_start,
                'score__lte': score_filter_end,
            }

            movies = movies.filter(**gte_lte)

    if search_field_get:
        movies = movies.filter(title__icontains=search_field_get)

    if minage_selector:
        movies = movies.filter(minage=minage_selector)

    return render(request, 'movies_page.html', {'movies' : movies.order_by('rank')})


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

def movies_delete(request, pk):
    movie = get_object_or_404(Movies, pk=pk)
    if request.method == "POST":
        movie.delete()
        messages.success(request, "Filme deletado com sucesso")
        return redirect('movies_page')
    return render(request,'movies_delete.html')



@login_required(login_url="/login/")
def quotes_page(request):

    search_field_get = request.GET.get("search_field")
    creator_selector = request.GET.get("creator_selector")

    creators = []
    quotes = Quotes.objects.all().order_by('content')
    for quote in quotes:
        if quote.creator not in creators:
            creators.append({'creator' : quote.creator})


    if search_field_get:
        quotes = quotes.filter(content__icontains=search_field_get)

    if creator_selector:
        quotes = quotes.filter(creator=creator_selector)
    
    return render(request, 'quotes_page.html', {'quotes' : quotes, 'creators' : creators})

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

def quotes_delete(request, pk):
    quote = get_object_or_404(Quotes, pk=pk)
    if request.method == "POST":
        quote.delete()
        messages.success(request, "Quote deletado com sucesso")
        return redirect('quotes_page')
    return render(request,'quotes_delete.html')