from django.urls import path, include
from . import views

urlpatterns = [
    path('solve/', views.SolveView.as_view()),
    path('ocr/', views.OCRView.as_view()),
]