from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('videogames/', views.videogames_index, name='index'),
    path('videogames/<int:videogame_id>/', views.videogames_detail, name='detail'),
    path('videogames/create/', views.VideogameCreate.as_view(), name='videogames_create'),
    path('videogames/<int:pk>/update/', views.VideogameUpdate.as_view(), name='videogames_update'),
    path('videogames/<int:pk>/delete/', views.VideogameDelete.as_view(), name='videogames_delete'),
    path('videogames/<int:videogame_id>/add_system/', views.add_system, name='add_system'),
    path('videogames/<int:videogame_id>/assoc_player/<int:player_id>/', views.assoc_player, name='assoc_player'),
    path('players/', views.PlayerList.as_view(), name='players_index'),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name='players_detail'),
    path('players/create/', views.PlayerCreate.as_view(), name='players_create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='players_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='players_delete'),
]
