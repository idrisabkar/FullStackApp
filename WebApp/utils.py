from passlib.hash import pbkdf2_sha256


def encrypt(p_password: str):
    return pbkdf2_sha256.hash(p_password)


def verified(p_password, h_password):
    if pbkdf2_sha256.verify(p_password, h_password):
        return True
    else:
        return False
# Passwords do not match
