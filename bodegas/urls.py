from django.urls import path, include
from rest_framework import routers
from bodegas import views
from .views import BodegaProductoListCreateView, BodegaProductoRetrieveUpdateDestroyView, regionAPI, BodegasCreate


router = routers.DefaultRouter()
router.register(r'bodegas', views.BodegasView, 'bodegas')


urlpatterns = [
    path('api/', include(router.urls)),
    path('bodega-producto/', BodegaProductoListCreateView.as_view(), name='bodega-producto-list'),
    path('bodega-producto/<int:pk>/', BodegaProductoRetrieveUpdateDestroyView.as_view(), name='bodega'),
    path('region/', regionAPI.as_view(), name="regiones"),
    path('create-bodega', BodegasCreate.as_view(), name="create-bodega"),
]
