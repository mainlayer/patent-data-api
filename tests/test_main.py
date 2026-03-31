"""Tests for the Patent Data API."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def mock_mainlayer():
    access_granted = MagicMock(authorized=True)
    access_denied = MagicMock(authorized=False)

    mock_ml = MagicMock()
    mock_ml.resources.verify_access = AsyncMock(return_value=access_granted)

    with patch("src.main.ml", mock_ml):
        yield mock_ml, access_granted, access_denied


@pytest.fixture()
def client(mock_mainlayer):
    from src.main import app
    return TestClient(app)


def test_list_patents_requires_token(client):
    resp = client.get("/patents")
    assert resp.status_code == 422


def test_list_patents_with_invalid_token_returns_402(client, mock_mainlayer):
    mock_ml, _, access_denied = mock_mainlayer
    mock_ml.resources.verify_access = AsyncMock(return_value=access_denied)

    resp = client.get("/patents", headers={"X-Mainlayer-Token": "bad"})
    assert resp.status_code == 402
    assert resp.json()["detail"]["error"] == "payment_required"


def test_list_patents_success(client):
    resp = client.get("/patents", headers={"X-Mainlayer-Token": "valid"})
    assert resp.status_code == 200
    data = resp.json()
    assert "results" in data
    assert "total" in data


def test_get_patent_not_found(client):
    resp = client.get("/patents/nonexistent-xyz", headers={"X-Mainlayer-Token": "valid"})
    assert resp.status_code == 404


def test_get_patent_known_id(client):
    resp = client.get("/patents/US11234567", headers={"X-Mainlayer-Token": "valid"})
    assert resp.status_code in (200, 404)
    if resp.status_code == 200:
        data = resp.json()
        assert "title" in data
        assert "abstract" in data


def test_search_requires_q(client):
    resp = client.get("/search", headers={"X-Mainlayer-Token": "valid"})
    assert resp.status_code == 422


def test_search_returns_results(client):
    resp = client.get("/search", headers={"X-Mainlayer-Token": "valid"}, params={"q": "neural network"})
    assert resp.status_code == 200
    data = resp.json()
    assert "results" in data
    assert data["query"] == "neural network"


def test_search_pagination(client):
    resp = client.get(
        "/search",
        headers={"X-Mainlayer-Token": "valid"},
        params={"q": "patent", "page": 1, "page_size": 3},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert len(data["results"]) <= 3


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"
