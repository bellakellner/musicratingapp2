from django.contrib import admin
from .models import User, Artist, Rating, Song

# Register your models here.
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')

admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Rating)
admin.site.register(Song,SongAdmin)
