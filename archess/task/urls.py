from django.conf.urls import url
from . import views
from . import rest_views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^create-task/$', views.CreateTaskView.as_view()),
    url(r'^tasks/(\d+)', views.get_task),
    url(r'^tasks/$', views.TasksView.as_view()),

    url(r'^api/tasks/$', rest_views.TaskList.as_view()),
    url(r'^api/tasks/(\d+)$', rest_views.TaskAPI.as_view()),
]