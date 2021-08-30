from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.authentication import views

urlpatterns = [
    path('api/register', views.RegisterUserView.as_view()),
    path('api/login', TokenObtainPairView.as_view()),
    path('api/refresh_token', TokenRefreshView.as_view()),
    path('api/is_verified', views.IsVerifiedView.as_view()),
]
