
from ProductInventory import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from . import views

router = DefaultRouter()
# ProductCreateViewSet
router.register('create-product', views.ProductCreateViewSet, basename='create_product')


urlpatterns = [
    path('api/product/', include(router.urls)),

    
]
