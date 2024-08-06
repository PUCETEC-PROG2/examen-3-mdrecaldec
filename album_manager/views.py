from django.shortcuts import render, get_object_or_404, redirect
from .models import Artist, Album
from .forms import ArtistForm, AlbumForm

def index(request):
    return render(request, 'album_manager/index.html')


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'album_manager/artist_list.html', {'artists': artists})

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'album_manager/artist_detail.html', {'artist': artist})

def artist_create(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm()
    return render(request, 'album_manager/artist_form.html', {'form': form})

def artist_update(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'album_manager/artist_form.html', {'form': form})

def artist_delete(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == "POST":
        artist.delete()
        return redirect('artist_list')
    return render(request, 'album_manager/artist_confirm_delete.html', {'artist': artist})

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_manager/album_list.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album_manager/album_detail.html', {'album': album})

def album_create(request):
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm()
    return render(request, 'album_manager/album_form.html', {'form': form})

def album_update(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            album = form.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_manager/album_form.html', {'form': form})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        album.delete()
        return redirect('album_list')
    return render(request, 'album_manager/album_confirm_delete.html', {'album': album}) #en html se manda una confirm de si se quiere eliminar el album
