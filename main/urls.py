from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'main'

urlpatterns = [
	path('', views.home, name="home"),
	path('select_game', views.select_game, name="select_game"),
	path('start_game/<str:gamename>/', views.start_game, name="start_game"),
	path('music_list_of_game/<str:gamename>/', views.music_list_of_game, name='music_list_of_game'),
	path('end_game/<int:score>/', views.end_game, name='end_game')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
