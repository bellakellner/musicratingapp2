#musicapp/serializers.py

from rest_framework import serializers
from .models import Artist, Rating,User



class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id','song','artist')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('username','song','rating')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
