import time

from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserAuthSerializer
from users.services import create_otp, create_invite_code


class GenerateCodeView(APIView):
    """
    Контролер для получения или создания нового пользователя при попытке входа и генерации OTP
    """
    serializer_class = UserAuthSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Производит поиск по БД, в случае, если пользователя, с введенным номером телефона не существует, то создает
        нового, генерирует одноразовый код (и имитирует его отправку на номер телефона пользователю) после чего,
        перенаправляет пользователя на страницу ввода кода
        """
        phone = request.POST.get('phone')
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            user = User.objects.create_user(phone=phone)

        otp = create_otp()
        user.invite_code = create_invite_code()
        user.otp = otp
        user.save()

        time.sleep(2)
        print('Ваш код для входа:', otp)

        return HttpResponseRedirect(redirect_to=reverse('users:auth_user', args=(user.pk,)))
