from django.urls import path
from music.views import (
    UserListCreateView, UserDetailView,
    ArtistListCreateView, ArtistDetailView,
    AlbumListCreateView, AlbumDetailView,
    SongListCreateView, SongDetailView,
    PlaylistListCreateView, PlaylistDetailView,
    PlaylistSongListCreateView, PlaylistSongDetailView,
    ListeningHistoryListCreateView,
    LikeListCreateView,
    RecommendationListCreateView
)

urlpatterns = [
   
    path("users/", UserListCreateView.as_view()),
    path("users/<str:pk>/", UserDetailView.as_view()),
    
    path("artists/", ArtistListCreateView.as_view()),
    path("artists/<str:pk>/", ArtistDetailView.as_view()),

    path("albums/", AlbumListCreateView.as_view()),
    path("albums/<str:pk>/", AlbumDetailView.as_view()),
    
    path("songs/", SongListCreateView.as_view()),
    path("songs/<str:pk>/", SongDetailView.as_view()),
    
    path("playlists/", PlaylistListCreateView.as_view()),
    path("playlists/<str:pk>/", PlaylistDetailView.as_view()),
    
    path("playlist-songs/", PlaylistSongListCreateView.as_view()),
    path("playlist-songs/<str:pk>/", PlaylistSongDetailView.as_view()),
   
    path("history/", ListeningHistoryListCreateView.as_view()),
    
    path("likes/", LikeListCreateView.as_view()),
   
    path("recommendations/", RecommendationListCreateView.as_view()),
]
