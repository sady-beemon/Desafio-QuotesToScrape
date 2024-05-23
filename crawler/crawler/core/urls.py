from django.urls import path
from crawler.core import views

urlpatterns = [
    
    path('login/', views.login_page, name = 'login_page'),
    path('home/movies/', views.movies_page, name = 'movies_page'),
    path('home/quotes/', views.quotes_page, name = 'quotes_page'),
    path('create_account/', views.create_account, name = 'create_account'),
    path('', views.first_page, name = 'first_page'),
    
]