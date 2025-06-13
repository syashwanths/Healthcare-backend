from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet

router = DefaultRouter()
router.register(r'api/patients', PatientViewSet, basename='patients')

urlpatterns = [
    path('', include(router.urls)),
]
