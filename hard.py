import secrets
import string


def generate_hard_password(length=16):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(all_characters) for i in range(length))
    return password