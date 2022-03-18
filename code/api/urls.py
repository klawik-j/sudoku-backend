from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"ocr", views.OcrViewSet, basename="ocr")

urlpatterns = [] + router.urls
