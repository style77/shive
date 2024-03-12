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
        """

    response = await client.post("/graphql/", json={"query": mutation})

    assert response.status_code == 200
    data = response.json()

    assert "errors" not in data
    assert "data" in data
    assert "createUser" in data["data"]
