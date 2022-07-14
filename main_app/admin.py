from django.contrib import admin
from . models import Videogame, System, Player

# Register your models here.
admin.site.register(Videogame)
admin.site.register(System)
admin.site.register(Player)