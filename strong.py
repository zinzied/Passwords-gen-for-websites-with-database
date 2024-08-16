import secrets
import string

def generate_strong_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(all_characters) for i in range(length))
    return password