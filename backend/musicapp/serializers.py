#musicapp/serializers.py

from rest_framework import serializers
from .models import User, Artist, Rating, Song

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
