from django.conf.urls import url
from . import views


urlpatterns = [
    url('^create-task/$', views.CreateTaskView.as_view()),
]