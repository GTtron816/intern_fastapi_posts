from passlib.context import CryptContext
pw_context= CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pw_context.hash(password)

def verify(plain_pass,hash_pass):
    return pw_context.verify(plain_pass,hash_pass)