from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Movie (models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    Img = models.ImageField(upload_to='img')
    category = models.CharField(max_length=100)
    trailer_link = models.URLField()

    def __str__(self):
        return self.name

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.movie.name}'
