from httpx import AsyncClient
import pytest


@pytest.mark.anyio
async def test_create_user(client: AsyncClient):
    mutation = """
        mutation createUser {
            createUser(email: "test@test.com", username: "test", fullName: "Test Test", password: "test") {
                __typename
                ... on CreateUserFailUsernameExists {
                    suggestedAlternatives
                    errorMessage
                }
                ... on CreateUserFailOther {
                    errorMessage
                }
                ... on CreateUserSuccess {
                    user {
                        id
                        username
                        email
                        fullName
                    }
                }
            }
        }
        """  # noqa: E501

    response = await client.post("/graphql/", json={"query": mutation})

    assert response.status_code == 200
    data = response.json()

    assert "errors" not in data
    assert "data" in data
    assert "createUser" in data["data"]
    assert data["data"]["createUser"]["__typename"] == "CreateUserSuccess"
    assert data["data"]["createUser"]["user"]["username"] == "test"


@pytest.mark.anyio
async def test_create_user_fail_username_exists(client: AsyncClient):
    mutation = """
        mutation createUser {
            createUser(email: "test@test.com", username: "test", fullName: "Test Test", password: "test") {
                __typename
                ... on CreateUserFailUsernameExists {
                    suggestedAlternatives
                    errorMessage
                }
                ... on CreateUserFailOther {
                    errorMessage
                }
                ... on CreateUserSuccess {
                    user {
                        id
                        username
                        email
                        fullName
                    }
                }
            }
        }
        """  # noqa: E501

    response = await client.post("/graphql/", json={"query": mutation})

    assert response.status_code == 200
    data = response.json()

    assert "errors" not in data
    assert "data" in data
    assert "createUser" in data["data"]
    assert data["data"]["createUser"]["__typename"] == "CreateUserFailUsernameExists"
    assert data["data"]["createUser"]["errorMessage"] == "Username already exists."


@pytest.mark.anyio
async def test_create_user_fail_email_exists(client: AsyncClient):
    mutation = """
        mutation createUser {
            createUser(email: "test@test.com", username: "test1", fullName: "Test Test", password: "test") {
                __typename
                ... on CreateUserFailUsernameExists {
                    suggestedAlternatives
                    errorMessage
                }
                ... on CreateUserFailOther {
                    errorMessage
                }
                ... on CreateUserSuccess {
                    user {
                        id
                        username
                        email
                        fullName
                    }
                }
            }
        }
        """  # noqa: E501

    response = await client.post("/graphql/", json={"query": mutation})

    assert response.status_code == 200
    data = response.json()

    assert "errors" not in data
    assert "data" in data
    assert "createUser" in data["data"]
    assert data["data"]["createUser"]["__typename"] == "CreateUserFailOther"
    assert data["data"]["createUser"]["errorMessage"] == "Email already exists."
