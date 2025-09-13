from django.urls import path, include
from account.views import UsersList, UserDetail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('', UsersList.as_view(), name='users'),
    path('<int:pk>', UserDetail.as_view(), name='user'),
    path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
]