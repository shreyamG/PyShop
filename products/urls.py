from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    # path('login/', auth_views.LoginView.as_view(), name = 'login')
]