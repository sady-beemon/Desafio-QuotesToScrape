from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages

from crawler.films.models import Movies
from crawler.films.forms import MovieForm
from crawler.quotes.models import Quotes
from crawler.quotes.forms import QuotesForm

from crawler.films.actions import data_request_movie
from crawler.quotes.actions import data_request_quotes
from crawler.core.ordenation import movies_header_ordenation


def first_page(request):
    
    return redirect("login_page")

def login_page(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if request.method == "POST":
        if user is not None:
            login(request, user)
            return redirect("movies_page")
        else:
            messages.error(request, "Login ou senha invalidos")
    return render(request, 'login_page.html')

def create_account(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if request.method == "POST":
        if username and password is not None:
            if password == request.POST.get("confirmPassword"):
                user = User.objects.create_user(username, "", password)
                return render(request, 'login_page.html')
        else:
            messages.error(request, "Login ou senha invalidos")
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


    if request.POST.get("action_selector") == "delete_selected":
        if request.POST.get("checkbox") and request.POST.get("action_selector"):
            selected_movies = request.POST.getlist("checkbox")
            if request.POST.get("selectAll"):
                selected_movies = []
                for movie in movies:
                    selected_movies.append(movie.pk)
            return render(request, 'movies_templates/movies_action_confirm.html',{'items' : selected_movies})
        
        
    if request.POST.get("confirm_action"):
        movies = Movies.objects.filter(id__in=request.POST.getlist("selected_item"))
        movies.delete()
        return redirect('movies_page')  

    movies = movies_header_ordenation(request, movies)
    paginator = Paginator(movies, 100)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'movies_templates/movies_page.html', {'page_obj' : page_obj})


def movies_edit(request, pk):

    movie = get_object_or_404(Movies, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            if request.POST.get("save_new"):
                movie = form.save()
                form = MovieForm()
                messages.success(request, "Pagina atualizada com sucesso")
                return redirect("movies_new")
            elif  request.POST.get("save_stay"):
                movie = form.save()
                messages.success(request, "Pagina atualizada com sucesso")
                return render(request, 'movies_templates/movies_edit.html', {'form': form})
            movie = form.save()
            messages.success(request, "Pagina atualizada com sucesso")
            return redirect('movies_page')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies_templates/movies_edit.html', {'form': form})

def movies_actionconfirm(request):
    
    from IPython import embed; embed(header='')

    for itempk in request.POST.get("item"):
        movie = get_object_or_404(Movies, pk=itempk)
        movie.delete
    return redirect('movies_page')  
      


def movies_new(request):

    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            if request.POST.get("save_new"):
                movie = form.save()
                form = MovieForm()
                messages.success(request, "Pagina atualizada com sucesso")
                return render(request, 'movies_templates/movies_new.html', {'form': form})
            elif  request.POST.get("save_stay"):
                movie = form.save()
                messages.success(request, "Pagina atualizada com sucesso")
                return render(request, 'movies_templates/movies_edit.html', {'form': form})
            movie = form.save()
            messages.success(request, "Pagina atualizada com sucesso")
            return redirect('movies_page')
    else: 
        form = MovieForm()
    return render(request, 'movies_templates/movies_new.html', {'form': form})

def movies_run_crawler(request):
    data_request_movie(request)
    return redirect('movies_page')

def movies_delete(request, pk):
    movie = get_object_or_404(Movies, pk=pk)
    if request.method == "POST":
        movie.delete()
        messages.success(request, "Filme deletado com sucesso")
        return redirect('movies_page')
    return render(request,'movies_templates/movies_delete.html')



@login_required(login_url="/login/")
def quotes_page(request):

    search_field_get = request.GET.get("search_field")
    creator_selector = request.GET.get("creator_selector")

    creators = []
    quotes = Quotes.objects.all().order_by('content')
    for quote in quotes:
        if ({'creator' : quote.creator}) not in creators:
            creators.append({'creator' : quote.creator})


    if search_field_get:
        quotes = quotes.filter(content__icontains=search_field_get)

    if creator_selector:
        quotes = quotes.filter(creator=creator_selector)


    if request.POST.get("action_selector") == "delete_selected":
        if request.POST.get("checkbox"):
            print("olright")
            selected_quotes = request.POST.getlist("checkbox")
            return render(request, 'quotes_templates/quotes_action_confirm.html',{'items' : selected_quotes})
        
        
    if request.POST.get("confirm_action"):
        quotes = Quotes.objects.filter(id__in=request.POST.getlist("selected_item"))
        quotes.delete()
        return redirect('quotes_page')  
    
    paginator = Paginator(quotes.order_by('content'), 100)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'quotes_templates/quotes_page.html', {'page_obj' : page_obj, 'creators' :creators})

def quotes_edit(request, pk):

    quote = get_object_or_404(Quotes, pk=pk)
    if request.method == "POST":
        form = QuotesForm(request.POST, instance=quote)
        if form.is_valid():
            if request.POST.get("save_new"):
                quote = form.save()
                form = QuotesForm()
                messages.success(request, "Pagina atualizada com sucesso")
                return redirect("quotes_new")
            elif  request.POST.get("save_stay"):
                quote = form.save()
                messages.success(request, "Pagina atualizada com sucesso")
                return render(request, 'quotes_templates/quotes_edit.html', {'form': form})
            quote = form.save()
            messages.success(request, "Pagina atualizada com sucesso")
            return redirect('quotes_page')
    else:
        form = QuotesForm(instance=quote)
    return render(request, 'quotes_templates/quotes_edit.html', {'form': form})

def quotes_new(request):

    if request.method == "POST":
        form = QuotesForm(request.POST)
        if form.is_valid():
            if request.POST.get("save_new"):
                quote = form.save()
                form = QuotesForm()
                messages.success(request, "Pagina atualizada com sucesso")
                return redirect("quotes_new")
            elif  request.POST.get("save_stay"):
                quote = form.save()
                messages.success(request, "Pagina atualizada com sucesso")
                return render(request, 'quotes_templates/quotes_edit.html', {'form': form})
            quote = form.save()
            messages.success(request, "Pagina atualizada com sucesso")
            return redirect('quotes_page')
    else:
        form = QuotesForm()
    return render(request, 'quotes_templates/quotes_new.html', {'form': form})

def quotes_run_crawler(request):
    data_request_quotes(request)
    return redirect('quotes_page')

def quotes_delete(request, pk):
    quote = get_object_or_404(Quotes, pk=pk)
    if request.method == "POST":
        quote.delete()
        messages.success(request, "Quote deletado com sucesso")
        return redirect('quotes_page')
    return render(request,'quotes_templates/quotes_delete.html')