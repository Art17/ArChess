from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.models import User

from userprofile.forms import ProfileForm

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfileView(View):
    def get(self, request, username):
        args = dict()
        args['watched_user'] = User.objects.get(username=username)
        args['user'] = request.user
        return render(request, 'user_profile.html', args)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
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
