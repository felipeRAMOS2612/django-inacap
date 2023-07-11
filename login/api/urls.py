from django.urls import path
from . import views
from .views import *
from rest_framework_simplejwt import views as jwt_views

from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenObtainPairView
)

urlpatterns = [
    path('register/', UserRegister.as_view()),
    path('login/', UserLogin.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', UserLogout.as_view()),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(),name='token_verify'),
    path('token/get/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
]