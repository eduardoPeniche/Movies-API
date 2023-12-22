from rest_framework import serializers

from .models import Movie, UserRating

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRating
        fields = '__all__'

class UserRatingShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRating
        fields = "user_name", "user_rating"