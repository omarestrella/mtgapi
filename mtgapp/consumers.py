from django.http import HttpResponse

from channels import Group
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http

from mtgapp import models


@channel_session_user_from_http
def game_connect(message, game_id):
    try:
        game = models.Game.objects.get(id=game_id)
    except models.Game.DoesNotExist:
        message.reply_channel.send({
            'error': 'no game'
        })
        return
    Group('users').add(message.reply_channel)


def game_disconnect(message):
    Group('users').discard(message.reply_channel)


def ws_consumer(message):
    message.reply_channel.send({
        'text': message.content['text']
    })
