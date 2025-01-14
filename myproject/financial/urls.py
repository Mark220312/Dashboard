from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FinancialMovementViewSet
from . import views

router = DefaultRouter()
router.register(r'movements', FinancialMovementViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('api/categories/', views.categories, name='categories'),
]