from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artist_images/', blank=True, null=True)

    

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='album_covers/', null=True, blank=True)

    def __str__(self):
        return self.title
