from django.contrib import admin

from .models import Team, Game

def complete_games(modeladmin, request, queryset):
    for game in queryset:
        game.has_occurred = True
        game.save()
complete_games.short_description = 'Complete selected games'

def initial_set_record(modeladmin, request, queryset):
    for team in queryset:
        team.tournament_wins = team.total_wins
        team.tournament_losses = team.total_losses
        team.tournament_diff = team.diff
        team.save()
initial_set_record.short_description = 'Set tournament record initial'

def clear_tournament_record(modeladmin, request, queryset):
    for team in queryset:
        team.tournament_wins = 0
        team.tournament_losses = 0
        team.tournament_diff = 0
        team.save()
clear_tournament_record.short_description = 'Clear tournament record'

class GameAdmin(admin.ModelAdmin):
    actions = [complete_games, ]

class TeamAdmin(admin.ModelAdmin):
    actions = [initial_set_record, clear_tournament_record, ]

# Register your models here.
admin.site.register(Team, TeamAdmin)
admin.site.register(Game, GameAdmin)
