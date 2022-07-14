from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Videogame
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
  system_form = SystemForm()
  return render(request, 'videogames/detail.html', {
    'videogame': videogame, 'system_form': system_form
  })

class VideogameCreate(CreateView):
  model = Videogame
  fields = '__all__'

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