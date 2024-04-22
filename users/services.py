import secrets
import random


def create_otp():
    """
    Создает 6-значиный пароль для входа
    :return: Строка - пароль
    """
    return ''.join(str(random.randint(0, 9)) for _ in range(6))


def create_invite_code():
    """
    Создает 6-значный инвайт код
    :return: Строка - инвайт код
    """
    return secrets.token_hex(3)
