from rest_framework import serializers
from .models import Team, Game

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team 
        fields = (
            'pk', 'location', 'name', 'logo', 'region',  'playoff_points', 'total_wins', 'total_losses', 'diff', 'tournament_wins', 'tournament_losses', 'tournament_diff'
        )

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game 
        fields = (
            'pk', 'game_number', 'date_time', 'teams', 'has_occurred', 'region', 'week', 'tournament', 'winning_team', 'losing_team', 'map_diff'
        )