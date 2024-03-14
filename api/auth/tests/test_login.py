from typing import Generator
import pytest
from jose import jwt
from httpx import AsyncClient

from api.common.tests import create_test_user
from api.settings import settings
from api.users.models import User


@pytest.fixture(scope="module", autouse=True)
async def user():
    yield await create_test_user()


@pytest.mark.anyio
async def test_login_success(client: AsyncClient, user: User):
    response = await client.post(
        "api/v1/auth/token",
        data={"username": user.email, "password": "test"},
    )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert "token_type" in data
    assert data["token_type"] == "bearer"

    payload = jwt.decode(
        data["access_token"], settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )
    assert payload["sub"] == user.email


@pytest.mark.anyio
async def test_login_fail(client: AsyncClient, user: User):
    response = await client.post(
        "api/v1/auth/token",
        data={"username": user.email, "password": "wrongpassword"},
    )

    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Incorrect email or password"


@pytest.mark.anyio
async def test_login_fail_no_user(client: AsyncClient):
    response = await client.post(
        "api/v1/auth/token",
        data={"username": "wrongemail", "password": "wrongpassword"},
    )

    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Incorrect email or password"
