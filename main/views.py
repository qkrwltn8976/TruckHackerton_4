from django.shortcuts import render


def home(request):
	return render(request, 'main/home.html')


def select_game(request):
    return render(request, 'main/select_game.html')


def start_game(request):
    return render(request, 'main/start_game.html')
# Create your views here.
