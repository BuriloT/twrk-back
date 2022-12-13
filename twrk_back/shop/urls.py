from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router_v1 = DefaultRouter()
router_v1.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router_v1.urls))
]
