from music.models import Song

def get_current_time():
    from datetime import datetime
    return {"time": datetime.now().strftime("%H:%M:%S")}


def say_hello():
    return {"message": "hello"}

def get_song(query):
    song = Song.objects.filter(title__icontains=query).first()
    if song:
        return {
            "title": song.title,
            "artist": song.artist.name if song.artist else "",
            "file_path": song.audio_url
        }
    return {"error": "Song not found"}