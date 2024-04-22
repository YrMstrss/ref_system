import secrets
import random


def create_otp():
    return ''.join(str(random.randint(0, 9)) for _ in range(6))


def create_invite_code():
    return secrets.token_hex(3)
