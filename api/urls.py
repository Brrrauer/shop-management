from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet) # Crear rutas para los productos a partir de su ViewSet

urlpatterns=[
    path('', include(router.urls))
]