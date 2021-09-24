from django.urls import path

from .views import (
    RegistrationAPIView,
    LoginAPIView,
    UserForgotPasswordAPIView
    )
from rest_framework_simplejwt import views as jwt_views
app_name = 'authentication'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('users/forgot-pass/', UserForgotPasswordAPIView.as_view()),
   
]





