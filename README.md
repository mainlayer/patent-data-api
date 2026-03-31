# patent-data-api
![CI](https://github.com/mainlayer/patent-data-api/actions/workflows/ci.yml/badge.svg)

Patent search and full-text patent records for AI agents — billed per query via Mainlayer.

## Install

```bash
pip install mainlayer httpx
```

## Quickstart

```python
import httpx

response = httpx.get(
    "https://your-api.com/search",
    headers={"X-Mainlayer-Token": "your-token"},
    params={"q": "neural network attention"}
)
print(response.json())
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/patents` | List patents (filter by class, assignee) |
| `GET` | `/patents/{id}` | Full patent detail with claims |
| `GET` | `/search?q=` | Full-text search across title, abstract, claims |
| `GET` | `/health` | Health check |

All data endpoints require `X-Mainlayer-Token` header.

## Running locally

```bash
pip install -e ".[dev]"
uvicorn src.main:app --reload
```

## Running tests

```bash
pytest tests/
```

## Environment variables

| Variable | Description |
|----------|-------------|
| `MAINLAYER_API_KEY` | Your Mainlayer API key |
| `MAINLAYER_RESOURCE_ID` | The resource ID for this API |

📚 [mainlayer.fr](https://mainlayer.fr)
