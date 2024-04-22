from django.urls import path

from users.apps import UsersConfig
from users.views import GenerateCodeView

app_name = UsersConfig.name

urlpatterns = [
    path('auth/', GenerateCodeView.as_view(), name='auth'),
]
