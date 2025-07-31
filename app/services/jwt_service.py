from dotenv import load_dotenv
import jwt
import os
from datetime import datetime, timedelta, timezone

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def create_access_token(user_id: int, email: str, expires_delta: timedelta = timedelta(days=3)):
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {
        "exp": expire,
        "user_id": user_id,
        "email": email,
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None