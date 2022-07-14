# Generated by Django 4.0.4 on 2022-07-13 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Rating Date')),
                ('console', models.CharField(choices=[('PS2', 'Playstation 2'), ('Gamecube', 'Gamecube'), ('PS3', 'Playstation 3'), ('XBOX 360', 'XBOX 360'), ('PS4', 'Playstation 4'), ('XBOX 1', 'XBOX 1'), ('PC', 'Computer')], default='PS2', max_length=8)),
                ('videogame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.videogame')),
            ],
        ),
    ]
