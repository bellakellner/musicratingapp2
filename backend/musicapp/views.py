from django.shortcuts import render
from .models import User, Artist, Rating, Song
from rest_framework import viewsets
from .serializers import UserSerializer,ArtistSerializer,RatingSerializer,SongSerializer

# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ArtistView(viewsets.ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

class RatingView(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

class SongView(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
