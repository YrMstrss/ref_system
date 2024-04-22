import re

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    """Менеджер для создания пользователя"""

    use_in_migrations = True

    def _create_user(self, phone, **extra_fields):
        pattern = r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
        if not phone:
            raise ValueError('У пользователя должно быть указан номер телефона')
        if re.match(pattern, phone) is None:
            raise ValueError('Проверьте номер телефона')
        user = self.model(email=self.normalize_email(phone), **extra_fields)
        user.save()

        return user

    def create_user(self, email, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, **extra_fields)
