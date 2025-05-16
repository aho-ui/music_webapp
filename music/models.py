import mongoengine as me

class User(me.Document):
    username = me.StringField(required=True, unique=True, max_length=150)
    email = me.EmailField(required=True, unique=True)
    password = me.StringField(required=True, max_length=128)
    country = me.StringField()
    is_active = me.BooleanField(default=True)
    is_staff = me.BooleanField(default=False)

    def __str__(self):
        return self.username

class Artist(me.Document):
    name = me.StringField(required=True, max_length=255)
    bio = me.StringField()

    def __str__(self):
        return self.name

class Album(me.Document):
    title = me.StringField(required=True, max_length=255)
    release_date = me.DateField()
    artist = me.ReferenceField(Artist, reverse_delete_rule=me.CASCADE)

    def __str__(self):
        return self.title

class Song(me.Document):
    title = me.StringField(required=True, max_length=255)
    duration = me.IntField()  # seconds
    audio_url = me.URLField()
    genre = me.StringField()
    album = me.ReferenceField(Album, null=True)
    artist = me.ReferenceField(Artist, required=True)

    def __str__(self):
        return self.title

class Playlist(me.Document):
    title = me.StringField(required=True, max_length=255)
    user = me.ReferenceField(User, required=True)
    is_public = me.BooleanField(default=False)
    share_link = me.URLField()

    def __str__(self):
        return self.title

class PlaylistSong(me.Document):
    playlist = me.ReferenceField(Playlist, required=True)
    song = me.ReferenceField(Song, required=True)
    position = me.IntField()

    meta = {
        'indexes': [
            {'fields': ('playlist', 'song'), 'unique': True}
        ]
    }

class ListeningHistory(me.Document):
    user = me.ReferenceField(User, required=True)
    song = me.ReferenceField(Song, required=True)
    played_at = me.DateTimeField(required=True)

class Like(me.Document):
    user = me.ReferenceField(User, required=True)
    song = me.ReferenceField(Song, required=True)

    meta = {
        'indexes': [
            {'fields': ('user', 'song'), 'unique': True}
        ]
    }

class Recommendation(me.Document):
    SOURCE_CHOICES = (
        ("daily_mix", "Daily Mix"),
        ("radio", "Radio"),
        ("ai", "AI"),
        ("manual", "Manual"),
        ("trending", "Trending"),
    )

    user = me.ReferenceField(User, required=True)
    song = me.ReferenceField(Song, required=True)
    source = me.StringField(choices=SOURCE_CHOICES)
    score = me.FloatField()
