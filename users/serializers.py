from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField

from users.models import User
from users.validators import UserDoesNotExistValidator


class UserAuthSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для входа
    """
    class Meta:
        model = User
        fields = ('phone', )


class UserSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для просмотра профиля пользователя
    """
    invited_users = SerializerMethodField()

    class Meta:
        model = User
        fields = ('phone', 'invite_code', 'inviter_code', 'invited_users')

    def get_invited_users(self, instance):
        try:
            return [user.phone for user in User.objects.all() if user.inviter_code == instance.invite_code]
        except User.DoesNotExist:
            return None


class UserAddInviteCodeSerializer(UserSerializer):
    """
    Сериалайзер для введения инвайт кода
    """
    class Meta:
        model = User
        fields = ('inviter_code',)
        validators = [
            UserDoesNotExistValidator(field='inviter_code')
        ]

    def update(self, instance, validated_data):
        if not instance.inviter_code:
            if validated_data['inviter_code'] == instance.invite_code:
                raise ValidationError('Вы не можете ввести свой инвайт код')
            super().update(instance, validated_data)
            return instance
        else:
            raise ValidationError('Вы уже вводили инвайт код')
