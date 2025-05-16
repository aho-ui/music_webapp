from rest_framework import serializers
from music.models import (
    User, Artist, Album, Song, Playlist,
    PlaylistSong, ListeningHistory, Like, Recommendation
)

# -------------------
# User Serializer
# -------------------
class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    country = serializers.CharField()

    def create(self, validated_data):
        return User(**validated_data).save()

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# -------------------
# Artist Serializer
# -------------------
class ArtistSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    bio = serializers.CharField(allow_blank=True)

    def create(self, validated_data):
        return Artist(**validated_data).save()

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# -------------------
# Album Serializer
# -------------------
class AlbumSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    release_date = serializers.DateField()
    artist = serializers.CharField()  # pass artist id

    def create(self, validated_data):
        artist = Artist.objects.get(id=validated_data['artist'])
        validated_data['artist'] = artist
        return Album(**validated_data).save()

    def update(self, instance, validated_data):
        if 'artist' in validated_data:
            validated_data['artist'] = Artist.objects.get(id=validated_data['artist'])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# -------------------
# Song Serializer
# -------------------
class SongSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    duration = serializers.IntegerField()
    audio_url = serializers.URLField()
    genre = serializers.CharField()
    album = serializers.CharField(required=False, allow_null=True)
    artist = serializers.CharField()

    def create(self, validated_data):
        artist = Artist.objects.get(id=validated_data['artist'])
        validated_data['artist'] = artist
        if 'album' in validated_data and validated_data['album']:
            validated_data['album'] = Album.objects.get(id=validated_data['album'])
        else:
            validated_data['album'] = None
        return Song(**validated_data).save()

    def update(self, instance, validated_data):
        if 'artist' in validated_data:
            validated_data['artist'] = Artist.objects.get(id=validated_data['artist'])
        if 'album' in validated_data:
            validated_data['album'] = Album.objects.get(id=validated_data['album']) if validated_data['album'] else None
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# -------------------
# Playlist Serializer
# -------------------
class PlaylistSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    user = serializers.CharField()
    is_public = serializers.BooleanField()
    share_link = serializers.URLField(allow_blank=True)

    def create(self, validated_data):
        validated_data['user'] = User.objects.get(id=validated_data['user'])
        return Playlist(**validated_data).save()

    def update(self, instance, validated_data):
        if 'user' in validated_data:
            validated_data['user'] = User.objects.get(id=validated_data['user'])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# -------------------
# PlaylistSong Serializer
# -------------------
class PlaylistSongSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    playlist = serializers.CharField()
    song = serializers.CharField()
    position = serializers.IntegerField()

    def create(self, validated_data):
        validated_data['playlist'] = Playlist.objects.get(id=validated_data['playlist'])
        validated_data['song'] = Song.objects.get(id=validated_data['song'])
        return PlaylistSong(**validated_data).save()

    def update(self, instance, validated_data):
        if 'playlist' in validated_data:
            validated_data['playlist'] = Playlist.objects.get(id=validated_data['playlist'])
        if 'song' in validated_data:
            validated_data['song'] = Song.objects.get(id=validated_data['song'])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# -------------------
# ListeningHistory Serializer
# -------------------
class ListeningHistorySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField()
    song = serializers.CharField()
    played_at = serializers.DateTimeField()

    def create(self, validated_data):
        validated_data['user'] = User.objects.get(id=validated_data['user'])
        validated_data['song'] = Song.objects.get(id=validated_data['song'])
        return ListeningHistory(**validated_data).save()

# -------------------
# Like Serializer
# -------------------
class LikeSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField()
    song = serializers.CharField()

    def create(self, validated_data):
        validated_data['user'] = User.objects.get(id=validated_data['user'])
        validated_data['song'] = Song.objects.get(id=validated_data['song'])
        return Like(**validated_data).save()

# -------------------
# Recommendation Serializer
# -------------------
class RecommendationSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField()
    song = serializers.CharField()
    source = serializers.CharField()
    score = serializers.FloatField()

    def create(self, validated_data):
        validated_data['user'] = User.objects.get(id=validated_data['user'])
        validated_data['song'] = Song.objects.get(id=validated_data['song'])
        return Recommendation(**validated_data).save()
