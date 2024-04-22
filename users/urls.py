from django.urls import path

from users.apps import UsersConfig
from users.views import GenerateCodeView, AuthUserView, UserRetrieveAPIView, UserUpdateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('auth/', GenerateCodeView.as_view(), name='auth'),
    path('auth/<int:pk>/', AuthUserView.as_view(), name='auth_user'),
    path('profile/', UserRetrieveAPIView.as_view(), name='user_profile'),
    path('add_code/', UserUpdateAPIView.as_view(), name='user_add_code'),
]
