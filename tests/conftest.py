import pytest
from track import factory


@pytest.fixture
async def client(test_client):
    app = await factory.make_app()
    return await test_client(app)
