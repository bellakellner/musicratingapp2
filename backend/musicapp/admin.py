from django.contrib import admin
from .models import  Artist, Rating, User

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id','song', 'artist')
class RatingsAdmin(admin.ModelAdmin):
    display = ('song','username','rating')
class UserAdmin(admin.ModelAdmin):
    display = ('username','password')

admin.site.register(Artist,ArtistAdmin)
admin.site.register(Rating,RatingsAdmin)
admin.site.register(User,UserAdmin)
