from fastapi import Request, HTTPException
from api.auth.services import service
from api.auth.constants import credentials_exception, expired_exception
from api.users.services import service as user_service


async def token_validator(request: Request):
    access_token = request.cookies.get("access_token")
    refresh_token = request.cookies.get("refresh_token")

    if access_token:
        try:
            payload = service.verify_token(
                access_token, credentials_exception, expired_exception
            )
            user = await user_service.get_user(payload["sub"])
            if user:
                request.state.user = user
                return payload
            raise credentials_exception
        except HTTPException as e:
            if e.detail == "Token expired" and refresh_token:
                raise expired_exception
            raise e
    else:
        raise credentials_exception
