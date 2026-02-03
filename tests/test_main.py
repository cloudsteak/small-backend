import pytest
from httpx import AsyncClient

@pytest.mark.anyio
async def test_health_check(client: AsyncClient):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.anyio
async def test_version(client: AsyncClient):
    response = await client.get("/v1/version")
    assert response.status_code == 200
    data = response.json()
    assert "version" in data
    assert "name" in data

@pytest.mark.anyio
async def test_info(client: AsyncClient):
    response = await client.get("/v1/info")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "operational"
    assert "uptime" in data
    assert "load" in data

@pytest.mark.anyio
async def test_echo(client: AsyncClient):
    message = {"msg": "hello world"}
    response = await client.post("/v1/echo", json=message)
    assert response.status_code == 200
    assert response.json() == message

@pytest.mark.anyio
async def test_read_users_me(client: AsyncClient):
    response = await client.get("/v1/users/me")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "admin"

@pytest.mark.anyio
async def test_create_item(client: AsyncClient):
    new_item = {"title": "Test Item", "description": "Test Description"}
    response = await client.post("/v1/items/", json=new_item)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == new_item["title"]
    assert data["description"] == new_item["description"]
    assert "id" in data

@pytest.mark.anyio
async def test_read_items(client: AsyncClient):
    response = await client.get("/v1/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2  # Based on mock data

@pytest.mark.anyio
async def test_read_item(client: AsyncClient):
    # Test existing item
    response = await client.get("/v1/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

    # Test non-existent item
    response = await client.get("/v1/items/999")
    assert response.status_code == 404
