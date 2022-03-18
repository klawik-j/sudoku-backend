from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"api/ocr", views.OcrViewSet, basename="ocr")
router.register(r"api/solve", views.SolveViewSet, basename="solve")

urlpatterns = [] + router.urls
