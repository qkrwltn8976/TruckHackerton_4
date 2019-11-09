from django.shortcuts import render
from main.models import game, musicgame

from main.serializers import MusicGameSerializer

def home(request):
	return render(request, 'main/home.html')


def select_game(request):
    return render(request, 'main/select_game.html')


def start_game(request, gamename):
    if request.method == 'GET':
        gamename = game.objects.filter(name=gamename)
        music_list = musicgame.objects.filter(game=gamename[0])
        serializer = MusicGameSerializer(music_list, many=True)
        music_list = serializer.data
        context = {'music_list': music_list}
    return render(request, 'main/start_game.html', context)

