from datetime import timedelta
from fastapi import HTTPException, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from api.auth.services import service
from api.settings import settings
from api.auth.constants import credentials_exception, expired_exception

from api.users.services import service as user_service


class RefreshTokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        if response.status_code == 401:
            refresh_token = request.cookies.get("refresh_token")
            if refresh_token:
                try:
                    new_payload = service.verify_token(
                        refresh_token, credentials_exception, expired_exception
                    )
                    user_email = new_payload.get("sub")
                    user = await user_service.get_user(user_email)
                    if user:
                        request.state.user = user
                        access_token = service.create_token(
                            data={"sub": new_payload["sub"]},
                            expires_delta=timedelta(
                                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
                            ),
                        )
                        new_response = Response(
                            content=response.body,
                            status_code=response.status_code,
                            headers=response.headers,
                        )
                        new_response.set_cookie(
                            key="access_token",
                            value=f"{access_token}",
                            httponly=True,
                            path="/",
                        )
                        return new_response
                except HTTPException:
                    pass
            return response
        return response
