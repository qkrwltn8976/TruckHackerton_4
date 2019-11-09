from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


class music(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    like = models.IntegerField()
    album_cover = models.ImageField(upload_to="music/%Y/%m/%d")

    def __str__(self):
        return '{} - {}'.format(self.title, self.artist)


class game(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class musicgame(models.Model):
    music = models.ForeignKey('music', on_delete=models.CASCADE,)
    game = models.ForeignKey('game', on_delete=models.CASCADE,)

    def __str__(self):
        return '{} : {}'.format(str(self.game), str(self.music))


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_score = models.PositiveIntegerField(default=0)
    max_score = models.PositiveIntegerField(default=0)
    current_game = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.user.username
    
    

class success_music(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    music = models.ForeignKey('music', on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(str(self.user), str(self.music))
    

class end_page_picture(models.Model):
    image = models.ImageField(upload_to="fail")
    text = models.CharField(max_length=100)


def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user)

post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)
