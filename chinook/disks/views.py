from django.shortcuts import render, get_object_or_404
from .models import Album, Track
from django.db.models import Q

def album_list(request):
    """Affiche la liste des albums, avec un champ de recherche élargi"""
    query = request.GET.get('q', '')

    if query:
        albums = Album.objects.filter(
            Q(title__icontains=query) | Q(artist__name__icontains=query)
        )
    else:
        albums = Album.objects.all()

    return render(request, 'disks/album_list.html', {'albums': albums, 'query': query})


def album_detail(request, album_id):
    """Affiche les morceaux d'un album avec les détails"""
    album = get_object_or_404(Album, pk=album_id)
    tracks = Track.objects.filter(album=album)
    return render(request, 'disks/album_detail.html', {'album': album, 'tracks': tracks})

def home(request):
    return render(request, 'index.html') 