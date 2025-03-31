from django.shortcuts import render, get_object_or_404
from .models import Album, Track

def album_list(request):
    """Affiche la liste des albums, avec un champ de recherche"""
    query = request.GET.get('q', '')  
    if query:
        albums = Album.objects.filter(title__icontains=query) 
    else:
        albums = Album.objects.all()  

    return render(request, 'disks/album_list.html', {'albums': albums, 'query': query})

def album_detail(request, album_id):
    """Affiche les morceaux d'un album avec les détails"""
    album = get_object_or_404(Album, pk=album_id)
    tracks = Track.objects.filter(album=album)
    return render(request, 'disks/album_detail.html', {'album': album, 'tracks': tracks})
