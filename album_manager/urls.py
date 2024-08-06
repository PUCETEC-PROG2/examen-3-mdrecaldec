# Ingresar tus URLs de la app aquí
from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from album_manager import views



urlpatterns = [
    path('', views.index, name='index'), 
    path('artistas/', views.artist_list, name='artist_list'),
    path('artista/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('artista/nuevo/', views.artist_create, name='artist_create'),
    path('artista/<int:pk>/editar/', views.artist_update, name='artist_update'),
    path('artista/<int:pk>/eliminar/', views.artist_delete, name='artist_delete'),
    path('albumes/', views.album_list, name='album_list'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('album/nuevo/', views.album_create, name='album_create'),
    path('album/<int:pk>/editar/', views.album_update, name='album_update'),
    path('album/<int:pk>/eliminar/', views.album_delete, name='album_delete'),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)