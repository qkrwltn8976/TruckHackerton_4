from main.models import *
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = game
        fields = ['name']


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = music
        fields = ['id', 'title', 'artist', 'like', 'album_cover']


class MusicGameSerializer(serializers.ModelSerializer):
    music = MusicSerializer()

    class Meta:
        model = musicgame
        fields = ['music']
