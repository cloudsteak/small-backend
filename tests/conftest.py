import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
from typing import AsyncGenerator

@pytest.fixture
def anyio_backend():
    return "asyncio"

@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://testserver"
    ) as ac:
        yield ac
