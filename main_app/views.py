from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from . models import Videogame, Player
from . forms import SystemForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def videogames_index(request):
  videogames = Videogame.objects.all()
  return render(request, 'videogames/index.html', { 'videogames': videogames })

def videogames_detail(request, videogame_id):
  videogame = Videogame.objects.get(id=videogame_id)
  id_list = videogame.players.all().values_list('id')
  players_videogame_doesnt_have = Player.objects.exclude(id__in=id_list)
  system_form = SystemForm()
  return render(request, 'videogames/detail.html', {
    'videogame': videogame, 'system_form': system_form, 'players': players_videogame_doesnt_have
  })

def assoc_player(request, videogame_id, player_id):
  Videogame.objects.get(id=videogame_id).players.add(player_id)
  return redirect('detail', videogame_id=videogame_id)

class VideogameCreate(CreateView):
  model = Videogame
  fields = ['name', 'genre', 'description', 'release']

class VideogameUpdate(UpdateView):
  model = Videogame
  fields = ['genre', 'description', 'release']

class VideogameDelete(DeleteView):
  model = Videogame
  success_url = '/videogames/'

def add_system(request, videogame_id):
  form = SystemForm(request.POST)
  if form.is_valid():
    new_system = form.save(commit=False)
    new_system.videogame_id = videogame_id
    new_system.save()
  return redirect('detail', videogame_id=videogame_id)

class PlayerList(ListView):
  model = Player

class PlayerDetail(DetailView):
  model = Player

class PlayerCreate(CreateView):
  model = Player
  fields = '__all__'

class PlayerUpdate(UpdateView):
  model = Player
  fields = ['name', 'number']

class PlayerDelete(DeleteView):
  model = Player
  success_url = '/players/'