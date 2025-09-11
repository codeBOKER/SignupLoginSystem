from django.urls import path
from account.views import UsersList, UserDetail
urlpatterns = [
    path('', UsersList.as_view(), name='users'),
    path('<int:pk>', UserDetail.as_view(), name='user'),
]