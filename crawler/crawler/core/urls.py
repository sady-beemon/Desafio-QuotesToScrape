from django.urls import path
from crawler.core import views

urlpatterns = [
    
    path('home/movies/', views.movies_page, name = 'movies_page'),
    path('home/movies/<int:pk>_edit/', views.movies_edit, name = 'movies_edit'),
    path('home/movies/new/', views.movies_new, name = 'movies_new'),
    path('home/movies/crawler/', views.movies_run_crawler, name = 'movies_run_crawler'),

    path('home/quotes/', views.quotes_page, name = 'quotes_page'),
    path('home/quotes/<int:pk>_edit/', views.quotes_edit, name = 'quotes_edit'),
    path('home/quotes/new/', views.quotes_new, name = 'quotes_new'),
    path('home/quotes/crawler/', views.quotes_run_crawler, name = 'quotes_run_crawler'),

    path('create_account/', views.create_account, name = 'create_account'),
    path('login/', views.login_page, name = 'login_page'),
    path('', views.first_page, name = 'first_page'),
    
]