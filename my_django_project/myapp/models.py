# myapp/models.py
from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField()
    popularity = models.IntegerField(default=0) 
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='movies/', default='movies/default.jpg')
    trailer = models.FileField(upload_to='trailers/', blank=True, null=True)
    
    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='actors/', default='actors/default.jpg')

    def __str__(self):
        return self.name

class MovieActor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.actor.name} as {self.role_name} in {self.movie.title}"
    
class Comment(models.Model):
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email

class Rank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')