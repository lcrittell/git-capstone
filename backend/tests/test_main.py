from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "MTG Pack Return API"
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok"
    }


def test_pack_prices():
    response = client.get("/api/pack-prices")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 3
    assert data[0]["set"] == "Example Set"
    assert data[0]["pack_price"] == 4.99
    assert data[0]["average_card_value"] == 7.50
    assert data[0]["estimated_return"] == 7.50