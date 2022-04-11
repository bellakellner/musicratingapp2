from django.contrib import admin
from .models import User, Artist, Rating, Song

# Register your models here.
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('song', 'artist')
class RatingsAdmin(admin.ModelAdmin):
    display = ('rating')

admin.site.register(User,UserAdmin)
admin.site.register(Artist,ArtistAdmin)
admin.site.register(Rating,RatingsAdmin)
admin.site.register(Song,SongAdmin)
