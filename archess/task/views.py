from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import TaskCreationForm
from .models import Task


class CreateTaskView(View):
    def get(self, request):
        task_form = TaskCreationForm()
        args = dict()
        args['form'] = task_form
        return render(request, 'create_task.html', args)

    def post(self, request):
        task_form = TaskCreationForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.author = request.user
            task.save()
            return HttpResponseRedirect('/task/' + str(task.id))
        else:
            return render(request, 'edit_profile.html', {'form': task_form})


def get_task(request, id):
    if request.method == 'GET':
        task = Task.objects.get(id=id)
        args = dict()
        args['task'] = task
        return render(request, 'task.html', args)
