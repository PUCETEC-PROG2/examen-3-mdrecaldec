from django import forms
from .models import Artist, Album

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'country_of_origin']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'release_year', 'genre', 'artist', 'cover']