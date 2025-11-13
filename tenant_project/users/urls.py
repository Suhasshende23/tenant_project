from django.urls import path
from tenant_project.users.views import UserCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path("create/", UserCreateView.as_view(), name="create-user"),
    path("token/access/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
