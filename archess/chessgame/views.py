from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ChessGame


def create_game(request):
    game = ChessGame.objects.create(author=request.user)
    game.save()
    return HttpResponseRedirect('/games/' + str(game.id) + '/')


def game(request, id):
    game = ChessGame.objects.get(id=id)
    args = dict()
    args['path'] = '/games/'
    if request.user == game.author:
        return render(request, 'play_chess.html', args)

# Create your views here.
