from django.urls import path, include
from rest_framework import routers
from productos import views


router = routers.DefaultRouter()
router.register(r'libros', views.LibrosView, 'libros')


urlpatterns = [
    path('api/', include(router.urls))
]
