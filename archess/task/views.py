from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views import View
from .forms import TaskCreationForm, TaskSearchForm
from .models import Task


@method_decorator(login_required(login_url='/login/'), name='dispatch')
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
            return HttpResponseRedirect('/tasks/' + str(task.id))
        else:
            return render(request, 'edit_profile.html', {'form': task_form})


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class TasksView(View):
    def get(self, request):
        args = dict()
        args['form'] = TaskSearchForm()
        return render(request, 'tasks.html', args)


@login_required(login_url='/login/')
def get_task(request, id):
    if request.method == 'GET':
        task = Task.objects.get(id=id)
        args = dict()
        args['task'] = task
        return render(request, 'task.html', args)
