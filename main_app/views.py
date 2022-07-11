from django.shortcuts import render
from django.http import HttpResponse

class Videogame:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, genre, description, release):
    self.name = name
    self.breed = genre
    self.description = description
    self.release = release

videogames = [
  Videogame('NBA Street', 'sports', 'NBA Street is a basketball video game of three-on-three street basketball. Aside from the basic structure of basketball, players try to collect trick points, which are scored through the use of almost every basketball game maneuver such as faking out defenders, shot blocking, diving for the ball, and dunking.', 2001),
  Videogame('Need For Speed, Underground 2', 'racing', 'Underground 2 is the first game in the series to feature an open world, where players can drive freely around and explore the city, unlocking areas by winning races.', 2004),
  Videogame('Skate 3', 'sports', 'Skate 3 is a skateboarding extreme sports game set in an open world place and played from a third-person perspective.', 2010),
  Videogame('NFL Street', 'sports', 'NFL Street is a series of sports video games developed by EA Tiburon and published by Electronic Arts. It combines the talent and big names of the NFL with the atmosphere of street football.', 2004)
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello Players</h1>')

def about(request):
    return render(request, 'about.html')

def videogames_index(request):
    return render(request, 'videogames/index.html', { 'videogames': videogames })