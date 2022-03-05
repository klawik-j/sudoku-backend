from django.urls import path

from . import views

urlpatterns = [
    path("api/solve/", views.SolveView.as_view()),
    # path('api/ocr/', views.OCRView.as_view()),
]
