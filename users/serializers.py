from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from users.models import User


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', )


class UserSerializer(serializers.ModelSerializer):
    invited_users = SerializerMethodField()

    class Meta:
        model = User
        fields = ('phone', 'invite_code', 'inviter_code', 'invited_users')

    def get_invited_users(self, instance):
        try:
            return User.objects.get(inviter_code=instance.invite_code)
        except User.DoesNotExist:
            return None
