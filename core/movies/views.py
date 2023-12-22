#from django.shortcuts import render
from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Movie, UserRating
from .serializers import MovieSerializer, UserRatingSerializer, UserRatingShortSerializer


# Create your views here.
class MovieView(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MovieDetailView(APIView):

    def get_movie(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return None
        
    # def get_user_ratings(self, pk):
    #     try:
    #         return UserRating.objects.filter(movie=pk)
    #     except UserRating.DoesNotExist:
    #         return None
        
    def get(self, request, pk):
        movie = self.get_movie(pk)
        if movie:
            #user_ratings = self.get_user_ratings(pk)

            movie_serializer = MovieSerializer(movie)
            # user_ratings_serializer = UserRatingSerializer(user_ratings, many=True)

            # response_data = {
            #     "Movie": movie_serializer.data,
            #     "User Ratings": user_ratings_serializer.data
            # }
            
            return Response(movie_serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        movie = self.get_movie(pk)
        if movie:
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class MovieRatingsView(APIView):

    def get_movie(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return None
        
    def get_user_ratings(self, pk):
        try:
            return UserRating.objects.filter(movie=pk)
        except UserRating.DoesNotExist:
            return None
        
    def get(self, request, pk):
        movie = self.get_movie(pk)
        if movie:
            user_ratings = self.get_user_ratings(pk)

            movie_data = {
                "id": movie.id,
                "title": movie.title,
                "imdb_rating": movie.imdb_rating,
                "user_rating_avg": movie.user_rating_avg
            }

            user_ratings_serializer = UserRatingShortSerializer(user_ratings, many=True)
            user_ratings_data = user_ratings_serializer.data

            response_data = {
                "Movie": movie_data,
                "User Ratings": user_ratings_data
            }
            
            return Response(response_data)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, pk): # TEST THIS
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        request.data['movie'] = pk

        serializer = UserRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Calculate average user rating for the movie # TEST THIS
            average_rating = UserRating.objects.filter(movie=movie).aggregate(avg_rating=Avg('user_rating'))['avg_rating']
            movie.user_rating_avg = average_rating
            movie.save()  # Update the movie with the new average rating
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)