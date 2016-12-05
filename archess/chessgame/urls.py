from django.conf.urls import url
from . import views


urlpatterns = [
    url('^create-game/$', views.create_game),
    url('^games/(\d+)', views.game),
]