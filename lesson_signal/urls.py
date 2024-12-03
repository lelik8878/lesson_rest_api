
from django.urls import path

from lesson_signal.views import get_sun


urlpatterns = [
    path('', get_sun),
]
