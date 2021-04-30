# Generated by Django 3.2 on 2021-04-28 01:40

from django.db import migrations
from ..models import Team

def update_teams(apps, schema_editor):
    with open("overwatchleague\\migrations\\teams.txt") as f:
        for line in f.readlines():
            team_data = line.split(" ")
            team = Team.objects.get(name=team_data[0])
            team.playoff_points = team_data[1]
            team.total_wins = team_data[2]
            team.total_losses = team_data[3]
            team.diff = team_data[4]
            team.mm_wins = team_data[2]
            team.mm_losses = team_data[3]
            team.mm_diff = team_data[4]
            team.save()

class Migration(migrations.Migration):

    dependencies = [
        ('overwatchleague', '0010_auto_20210427_1849'),
    ]

    operations = [
        migrations.RunPython(update_teams),
    ]