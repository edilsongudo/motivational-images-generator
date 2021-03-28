import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


def generate_key(password_provided):
    password = password_provided.encode()
    salt = b'Do\xdbw>\xc4\x99\xea/\xc4~j\xe2\x86\x16M'
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt,
                     iterations=100000, backend=default_backend())

    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key.decode()


def encrypt(message, key):
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted.decode()


def decrypt(encrypted, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    return decrypted.decode()


print(help(encrypt))
