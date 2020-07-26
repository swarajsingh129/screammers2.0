from django.conf.urls import url
from authen.views import User_login
from django.urls import path
from authen import views


urlpatterns = [
    path('', views.home),
    path('signup', views.signup, name='signup'),
    path('login', views.User_login),
    path('logout', views.User_logout),
    url(r'^ajax/check_usrnam/$', views.check_usrnam),
]
