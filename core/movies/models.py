from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    year = models.IntegerField()
    run_time = models.IntegerField()
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(10)])
    user_rating_avg = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(10)], default=None, null=True)
    on_streaming = models.BooleanField(default=None, null=True)
    box_office_world = models.DecimalField(max_digits=15, decimal_places=2)
    storyline_ai_api = models.TextField(blank=True, null=True)

class UserRating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])