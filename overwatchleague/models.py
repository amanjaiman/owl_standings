from django.db import models

class Team(models.Model):
    location = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=100)
    region = models.CharField(max_length=20)

    playoff_points = models.IntegerField(default=0)
    total_wins = models.IntegerField(default=0)
    total_losses = models.IntegerField(default=0)
    diff = models.IntegerField(default=0)
    
    tournament_wins = models.IntegerField(default=0)
    tournament_losses = models.IntegerField(default=0)
    tournament_diff = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Game(models.Model):
    game_number = models.IntegerField(default=0)
    date_time = models.DateField()
    teams = models.ManyToManyField(Team, related_name='teams')
    has_occurred = models.BooleanField(default=False)

    region = models.CharField(max_length=20, default=None, null=True)
    
    week = models.IntegerField(default=0)
    tournament = models.CharField(max_length=50, default=None, null=True)

    winning_team = models.ForeignKey(Team, default=None, null=True, on_delete=models.CASCADE, related_name='winning_team')
    losing_team = models.ForeignKey(Team, default=None, null=True, on_delete=models.CASCADE, related_name='losing_team')

    map_diff = models.IntegerField(default=0)

    def __str__(self):
        if self.teams.exists():
            return ' vs. '.join([a.name for a in self.teams.all()])
        else:
            return " Game "+str(self.game_number)