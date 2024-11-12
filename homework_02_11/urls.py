from django.urls import path

from homework_02_11.views import get_homework_02_11

urlpatterns = [
    path('', get_homework_02_11, name='homework_02_11'),
]