# music/factories.py
import factory
from factory.mongoengine import MongoEngineFactory
from music.models import User, Artist, Album, Song, Playlist, PlaylistSong, ListeningHistory, Like, Recommendation
import random
from datetime import datetime, timedelta

class UserFactory(MongoEngineFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    country = factory.Faker("country")
    is_active = True
    is_staff = factory.Faker("boolean")


class ArtistFactory(MongoEngineFactory):
    class Meta:
        model = Artist

    name = factory.Faker("name")
    bio = factory.Faker("paragraph")


class AlbumFactory(MongoEngineFactory):
    class Meta:
        model = Album

    title = factory.Faker("sentence", nb_words=2)
    release_date = factory.Faker("date_this_decade")
    artist = factory.SubFactory(ArtistFactory)


class SongFactory(MongoEngineFactory):
    class Meta:
        model = Song

    title = factory.Faker("sentence", nb_words=3)
    duration = factory.Faker("random_int", min=120, max=420)
    audio_url = factory.Faker("url")
    genre = factory.Iterator(["Pop", "Rock", "Jazz", "Classical", "Hip-hop"])
    album = factory.SubFactory(AlbumFactory)
    artist = factory.SubFactory(ArtistFactory)


class PlaylistFactory(MongoEngineFactory):
    class Meta:
        model = Playlist

    title = factory.Faker("sentence", nb_words=2)
    user = factory.SubFactory(UserFactory)
    is_public = factory.Faker("boolean")
    share_link = factory.Faker("url")


class PlaylistSongFactory(MongoEngineFactory):
    class Meta:
        model = PlaylistSong

    playlist = factory.SubFactory(PlaylistFactory)
    song = factory.SubFactory(SongFactory)
    position = factory.Sequence(lambda n: n + 1)


class ListeningHistoryFactory(MongoEngineFactory):
    class Meta:
        model = ListeningHistory

    user = factory.SubFactory(UserFactory)
    song = factory.SubFactory(SongFactory)
    played_at = factory.LazyFunction(lambda: datetime.utcnow() - timedelta(days=random.randint(0, 30)))


class LikeFactory(MongoEngineFactory):
    class Meta:
        model = Like

    user = factory.SubFactory(UserFactory)
    song = factory.SubFactory(SongFactory)


class RecommendationFactory(MongoEngineFactory):
    class Meta:
        model = Recommendation

    user = factory.SubFactory(UserFactory)
    song = factory.SubFactory(SongFactory)
    source = factory.Iterator([choice[0] for choice in Recommendation.SOURCE_CHOICES])
    score = factory.Faker("pyfloat", left_digits=1, right_digits=2, positive=True)
