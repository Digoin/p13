"""This module is used to specify the urls accessible to the user."""
from django.urls import path

from . import views

APP_NAME = 'authentication'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
