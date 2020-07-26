
from django.urls import path
from loggedinuser import views


urlpatterns = [
    path('', views.userhome),
    path('json',views.Post_list.as_view())
]
