from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from users.views.user_views import (
    MyTokenObtainPairView,
    RegisterUserAPIView,
    UserDetailAPI,
)


urlpatterns = [
    # User Registration
    path("register/", RegisterUserAPIView.as_view(), name="register"),
    # JWT Login
    path("", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    # JWT Token Refresh
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Get User Details
    path("get-details/", UserDetailAPI.as_view(), name="get-details"),
]
