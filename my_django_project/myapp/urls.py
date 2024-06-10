# myapp/urls.py
from django.urls import path
from . import views
from .views import actor_detail, actors_list, add_to_watchlist, comment, home, movie_detail, register, remove_from_watchlist, search, search_suggestions, user_login, user_logout, watchlist

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('movie/<int:id>/', views.movie_detail, name='movie_detail'),
    path('comment/<int:movie_id>/', views.comment, name='comment'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('watchlist/add/', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/remove/<int:movie_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('search/', views.search, name='search'),
    path('search_suggestions/', views.search_suggestions, name='search_suggestions'),
    path('actors/', views.actors_list, name='actors_list'),
    path('actor/<int:id>/', views.actor_detail, name='actor_detail'),
]
