from django.urls import path, include
from . import views

urlpatterns = [
    path('solve/', views.index),
]