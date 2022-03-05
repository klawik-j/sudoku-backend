from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"account", viewset=views.AccountViewSet, basename="account")

urlpatterns = [] + router.urls
