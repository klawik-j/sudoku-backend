from django.urls import path, include
from . import views

urlpatterns = [
    path('api/solve/', views.SolveView.as_view()),
    path('api/ocr/', views.OCRView.as_view()),
]