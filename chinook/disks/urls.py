from django.urls import path
from . import views

urlpatterns = [
    path('albums/', views.album_list, name='album_list'),
    path('albums/<int:album_id>/', views.album_detail, name='album_detail'),
]
