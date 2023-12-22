from django.urls import path
from .views import MovieView, MovieDetailView, MovieRatingsView

urlpatterns = [
    path('', MovieView.as_view(),  name='movies-db'),
    path('/<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
    path('/<int:pk>/ratings', MovieRatingsView.as_view(), name='movie-ratings'),
]