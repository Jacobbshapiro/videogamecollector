from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
CONSOLES = (
    ('PS2', 'Playstation 2'),
    ('Gamecube', 'Gamecube'),
    ('PS3', 'Playstation 3'),
    ('XBOX 360', 'XBOX 360'),
    ('PS4', 'Playstation 4'),
    ('XBOX 1', 'XBOX 1'),
    ('PC', 'Computer')
)

class Player(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('players_detail', kwargs={'pk': self.id})

class Videogame(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    release = models.IntegerField()
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'videogame_id': self.id})

class System(models.Model):
    date = models.DateField('Date of purchase')
    console = models.CharField(
        max_length=8,
        choices=CONSOLES,
        default=CONSOLES[0][0]
    )

    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)

    def __str__(self):
        return f"I got this game on {self.get_console_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

    