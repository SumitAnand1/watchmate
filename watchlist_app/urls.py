from django.urls import path, include
from watchlist_app.views import Movie_list , Movie_detail

urlpatterns = [
    path('list/', Movie_list, name='movie-list'),
    path('<int:pk>', Movie_detail, name='movie-details')
]
