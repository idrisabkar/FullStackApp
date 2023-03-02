from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password):
    return pwd_context.hash(password)


def verified(c_password, h_password):
    return pwd_context.verify(c_password, h_password)
