from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import game, musicgame
from main.serializers import MusicGameSerializer


def home(request):
	return render(request, 'main/home.html')


def select_game(request):
    games = game.objects.all()
    context = {'games': games}
    return render(request, 'main/select_game.html', context)


def start_game(request, gamename):
    context = {'gamename': gamename}
    return render(request, 'main/start_game.html', context)

@api_view(['POST'])
def music_list_of_game(request, gamename):
    if request.method == 'POST':
        gamename = game.objects.filter(name=gamename)
        music_list = musicgame.objects.filter(game=gamename[0]).order_by('?')
        serializer = MusicGameSerializer(music_list, many=True)
        return Response(serializer.data)