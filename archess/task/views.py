from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import TaskCreationForm


class CreateTaskView(View):
    def get(self, request):
        task_form = TaskCreationForm()
        args = dict()
        args['form'] = task_form
        return render(request, 'create_task.html', args)

    def post(self, request):
        task_form = TaskCreationForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return HttpResponseRedirect('/task/' + request.user.username)
        else:
            return render(request, 'edit_profile.html', {'form': task_form})

# Create your views here.
