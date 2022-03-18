from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"ocr", views.OcrViewSet, basename="ocr")

urlpatterns = [
    path("api/solve/", views.SolveView.as_view()),
] + router.urls
