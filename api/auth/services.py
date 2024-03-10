from datetime import datetime, timedelta
from fastapi import HTTPException

from jose import ExpiredSignatureError, JWTError, jwt
from api.settings import settings


class AuthService:
    def create_token(self, data: dict, expires_delta: timedelta) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = JWTError.encode(
            to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
        )
        return encoded_jwt

    def verify_token(token: str, credentials_exception: HTTPException, expired_exception: HTTPException) -> dict:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            return payload
        except ExpiredSignatureError:
            raise expired_exception
        except JWTError:
            raise credentials_exception


service = AuthService()
