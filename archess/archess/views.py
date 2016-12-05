from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from django.views import View
from django.contrib import auth
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from chessgame.models import ChessGame


def home(request):
    games = ChessGame.objects.all()
    args = dict()
    args['games'] = games
    return render(request, 'home.html', args)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def play_chess(request):
    args = dict()
    args['path'] = request.path
    return render(request, 'play_chess.html', args)

class LoginView(View):
    def get(self, request):
        args = dict()
        args['form'] = AuthenticationForm()
        args['user'] = request.user
        return render(request, 'login.html', args)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = auth.authenticate(username=username, password=password)
            if user is None:
                form.add_error('username', 'Invalid username')
                form.add_error('password', 'Invalid password')
                print(username)
                print(password)
                return render(request, 'login.html', {'form': form})
            else:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html', {'form': form})


class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'signup.html', {'form': form})