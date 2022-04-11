from django.shortcuts import render
from .models import  Artist, Rating, User
from rest_framework import viewsets
from .serializers import ArtistSerializer,RatingSerializer, UserSerializer
# Create your views here.


class ArtistView(viewsets.ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

class RatingView(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
