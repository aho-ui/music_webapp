import os
import sys
import django
from mongoengine import connect

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

django.setup()

from music.models import Song, Artist


def get_or_create_artist(name):
    artist = Artist.objects(name=name).first()
    if not artist:
        artist = Artist(name=name)
        artist.save()
    return artist



artist2 = get_or_create_artist("Justin Timberlake")
song2 = Song(
    title="Can't Stop the Feeling",
    duration=236,
    audio_url="http://localhost:8000/media/cant_stop_the_feeling.mp3",
    genre="Pop",
    artist=artist2
)
song2.save()


artist3 = get_or_create_artist("Bruno Mars & Mark Ronson")
song3 = Song(
    title="Uptown Funk",
    duration=269,
    audio_url="http://localhost:8000/media/uptown_funk.mp3",
    genre="Funk",
    artist=artist3
)
song3.save()

print("All songs added!")
