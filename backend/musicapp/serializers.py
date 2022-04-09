#musicapp/serializers.py

from rest_framework import serializers
from .models import User, Artist, Rating, Song

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('song','artist')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','username','song','rating')

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id','artist','song','genre')
        
