from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('main', views.main_page),
    path('registration', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('friends', views.friends),
    path('user/<int:user_id>', views.profile),
    path('add_friend/<int:user_id>', views.add_friend), 
    path('remove_friend/<int:user_id>', views.remove_friend)
    
    
]