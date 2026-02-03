import pytest
from httpx import AsyncClient
from jose import jwt
from app.core.config import settings

@pytest.mark.anyio
async def test_get_token_success(client: AsyncClient):
    username = "testuser"
    response = await client.post("/v1/get-token", json=username)
    assert response.status_code == 200
    
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    
    # Instead of comparing the full token string (which changes based on time),
    # we decode it and verify the contents.
    token = data["access_token"]
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    
    assert payload["sub"] == username
    assert "exp" in payload

@pytest.mark.anyio
async def test_get_token_empty_username(client: AsyncClient):
    # Testing the empty string behavior discussed earlier
    response = await client.post("/v1/get-token", json="")
    assert response.status_code == 200
    
    data = response.json()
    token = data["access_token"]
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    
    assert payload["sub"] == ""
