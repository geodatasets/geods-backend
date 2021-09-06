from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .viewsets import PorjectViewSet

router_vistas = DefaultRouter()
router_vistas.register(r'projects',PorjectViewSet)

urlpatterns = [
    path("",include(router_vistas.urls) ),
]