from rest_framework import serializers

from users.models import User


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'invite_code', 'inviter_code',)
