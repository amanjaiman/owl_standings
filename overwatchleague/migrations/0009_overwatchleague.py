# Generated by Django 3.2 on 2021-04-27 21:41

from django.db import migrations
from ..models import Game

def create_data(apps, schema_editor):
    games = Game.objects.all()
    for game in games:
        if game.week in [1, 2, 3]:
            game.tournament = "May Melee"
        elif game.week in [6, 7, 8]:
            game.tournament = "June Joust"
        elif game.week in [11, 12, 13]:
            game.tournament = "Summer Showdown"
        else:
            game.tournament = "Countdown Cup"
        game.save()

class Migration(migrations.Migration):

    dependencies = [
        ('overwatchleague', '0008_alter_game_tournament'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
