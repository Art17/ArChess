from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User

from userprofile.forms import ProfileForm


class ProfileView(View):
    def get(self, request, username):
        args = dict()
        args['user'] = User.objects.get(username=username)
        args['current_user'] = request.user
        return render(request, 'user_profile.html', args)


class EditProfileView(View):
    def get(self, request):
        dir_form = ProfileForm()
        args = dict()
        args['form'] = dir_form
        return render(request, 'edit_profile.html', args)

    def post(self, request):
        dir_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if dir_form.is_valid():
            dir_form.save()
            return HttpResponseRedirect('/user/' + request.user.username)
        else:
            return render(request, 'edit_profile.html', {'form': dir_form})

# Create your views here.
