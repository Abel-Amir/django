from django.contrib import admin
from django.urls import path
from . views import *
urlpatterns = [
    path("url_1/",aizirek_1),
    path("url_2/",aizirek_2),
    path("url_3/",aizirek_3)
]
