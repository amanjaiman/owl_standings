from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Team, Game
from .serializers import *

from datetime import datetime
import json

@api_view(['GET'])
def teams(request):
    data = Team.objects.all().order_by('-playoff_points', '-diff')
    serializer = TeamSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def teams_ordered(request):
    data = Team.objects.all().order_by('pk')
    serializer = TeamSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def teams_by_region(request, region):
    data = Team.objects.filter(region=region).order_by('-playoff_points', '-diff')
    serializer = TeamSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def week(request):
    current_week = (int(datetime.now().strftime("%W"))-14)%52
    games = Game.objects.filter(week=current_week)
    if len(games) != 0:
        current_tournament = games[0].tournament
    else:
        current_tournament = ""
    return_dict = {"week": current_week, "tournament": current_tournament}

    return Response(json.dumps(return_dict))

@api_view(['GET'])
def games(request, week):
    try:
        games = Game.objects.filter(week=week)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = GameSerializer(games, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def games_by_tournament(request):
    current_week = (int(datetime.now().strftime("%W"))-14)%52
    games = Game.objects.filter(week=current_week)
    if len(games) != 0:
        current_tournament = games[0].tournament
    else:
        current_tournament = ""

    games = Game.objects.filter(tournament=current_tournament, has_occurred=False).order_by('date_time')
    serializer = GameSerializer(games, context={'request': request}, many=True)

    return Response(serializer.data)
    
#@api_view(['GET'])
#def head_to_head(request, team1, team2, tournament):
#    games = Game.objects.filter(tournament=tournament, has_occurred=True)
#    for game in games:
#        teams = game.teams.all()
#        t1 = Team.objects.get(name=team1)
#        t2 = Team.objects.get(name=team2)
#        if t1 in teams and t2 in teams:
#            if 
#            return Response(json.dumps({"headtohead": True}))
#
#    return Response(json.dumps({"headtohead": 0}))