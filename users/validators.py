from rest_framework.exceptions import ValidationError

from users.models import User


class UserDoesNotExistValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        try:
            User.objects.get(invite_code=tmp_value)
        except User.DoesNotExist:
            raise ValidationError('Введен неверный инвайт код')
