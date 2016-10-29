from django.conf.urls import url
from . import views


urlpatterns = [
    url('^user/(\w+)/$', views.ProfileView.as_view()),
    url('^profile/edit', views.EditProfileView.as_view())
]