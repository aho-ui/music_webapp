from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from music.models import (
    User, Artist, Album, Song, Playlist,
    PlaylistSong, ListeningHistory, Like, Recommendation
)
from music.serializers import (
    UserSerializer, ArtistSerializer, AlbumSerializer, SongSerializer,
    PlaylistSerializer, PlaylistSongSerializer, ListeningHistorySerializer,
    LikeSerializer, RecommendationSerializer
)
from django.conf import settings
import openai, json
from datetime import datetime
from music.functions.functions import get_current_time, say_hello, get_song
from music.functions.openai_schema import functions


class BaseAPIView(APIView):
    model = None
    serializer_class = None

    def get(self, request):
        items = self.model.objects.all()
        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BaseDetailView(APIView):
    model = None
    serializer_class = None

    def get_object(self, pk):
        return self.model.objects.get(id=pk)

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = self.serializer_class(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = self.serializer_class(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserListCreateView(BaseAPIView):
    model = User
    serializer_class = UserSerializer

class UserDetailView(BaseDetailView):
    model = User
    serializer_class = UserSerializer

class ArtistListCreateView(BaseAPIView):
    model = Artist
    serializer_class = ArtistSerializer

class ArtistDetailView(BaseDetailView):
    model = Artist
    serializer_class = ArtistSerializer

class AlbumListCreateView(BaseAPIView):
    model = Album
    serializer_class = AlbumSerializer

class AlbumDetailView(BaseDetailView):
    model = Album
    serializer_class = AlbumSerializer

class SongListCreateView(BaseAPIView):
    model = Song
    serializer_class = SongSerializer

class SongDetailView(BaseDetailView):
    model = Song
    serializer_class = SongSerializer

class PlaylistListCreateView(BaseAPIView):
    model = Playlist
    serializer_class = PlaylistSerializer

class PlaylistDetailView(BaseDetailView):
    model = Playlist
    serializer_class = PlaylistSerializer

class PlaylistSongListCreateView(BaseAPIView):
    model = PlaylistSong
    serializer_class = PlaylistSongSerializer

class PlaylistSongDetailView(BaseDetailView):
    model = PlaylistSong
    serializer_class = PlaylistSongSerializer

class ListeningHistoryListCreateView(BaseAPIView):
    model = ListeningHistory
    serializer_class = ListeningHistorySerializer

class LikeListCreateView(BaseAPIView):
    model = Like
    serializer_class = LikeSerializer

class RecommendationListCreateView(BaseAPIView):
    model = Recommendation
    serializer_class = RecommendationSerializer



class TextModalAPIView(APIView):
    def post(self, request):
        user_input = request.data.get("message")
        if not user_input:
            return Response({"error": "No input provided"}, status=400)
        
        chat_history = request.session.get("chat_history", [])
        chat_history.append({"role": "user", "content": user_input})

        openai.api_key = settings.OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history,
            functions= functions,
                function_call="auto"
        )
        
        available_functions = {
        "get_current_time": get_current_time,
        "say_hello": say_hello,
        "get_song":get_song,
        }
        choice = response.choices[0]
        if "function_call" in choice["message"]:
            function_name = choice["message"]["function_call"]["name"]
            arguments_str = choice["message"]["function_call"].get("arguments")

            if function_name in available_functions:
                if arguments_str:
                    arguments = json.loads(arguments_str)
                    result = available_functions[function_name](**arguments)
                else:
                    result = available_functions[function_name]()
                return Response({"function_result": result})

    
        reply = choice["message"]["content"]
        return Response({"reply": reply})


         



        

