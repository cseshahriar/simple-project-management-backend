from django.urls import path, include
from .views import ProjectAPIView

from rest_framework import routers
router = routers.DefaultRouter()
router.register('projects', ProjectAPIView)

urlpatterns = router.urls
