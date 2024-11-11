from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RiskCalculationViewSet

router = DefaultRouter()
router.register(r'risk-calculation', RiskCalculationViewSet, basename='risk_calculation')

urlpatterns = [
    path('', include(router.urls)),
]
