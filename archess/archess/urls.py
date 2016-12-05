"""archess URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import rest_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.home),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^signup/$', views.SignupView.as_view()),
    url(r'^logout/$', views.logout_view),

    url(r'^play-with-computer/$', views.play_chess),
    url(r'^play-here/$', views.play_chess),

    url(r'^api/users/$', rest_views.UsersAPI.as_view()),
    url(r'^api/users/(\d+)/$', rest_views.UserAPI.as_view()),

    url(r'^', include('userprofile.urls')),
    url(r'^', include('task.urls')),
    url(r'^', include('chessgame.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)