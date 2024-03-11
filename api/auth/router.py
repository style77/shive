from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from api.auth.authorization import OAuth2PasswordBearerWithCookie
from api.auth.dependencies import token_validator
from api.users.services import service as user_service
from api.auth.services import service
from api.settings import settings

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token")
async def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    user, authenticated = await user_service.authenticate_user(
        form_data.username, form_data.password
    )
    if not authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

    access_token = service.create_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    refresh_token = service.create_token(
        data={"sub": user.email}, expires_delta=refresh_token_expires
    )

    response.set_cookie(
        key="access_token",
        value=f"{access_token}",
        httponly=True,
        max_age=access_token_expires.seconds,
    )
    response.set_cookie(
        key="refresh_token",
        value=f"{refresh_token}",
        httponly=True,
        max_age=refresh_token_expires.seconds,
    )
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/api/v1/auth/token")


@router.get("/secure-endpoint")
async def secure_endpoint(user: dict = Depends(token_validator)):
    return {"message": "This is a secure endpoint.", "user": user}
