# patent-data-api

Patent search and full-text records sold to AI research agents per query via [Mainlayer](https://mainlayer.fr).

## Overview

Comprehensive patent database API: search millions of patents, retrieve full specifications with claims, and track inventor/assignee data. Pay-per-query.

**API Docs:** https://patent-data-api.example.com/docs

## Pricing

- `/search` — $0.02 per query
- `/patents/{id}` — $0.05 per full record (title, abstract, claims, citations)
- `/patents` — $0.01 per query (list with filters)
- `/health` — FREE

## Agent Example: Patent Intelligence

```python
from mainlayer import MainlayerClient
import httpx

client = MainlayerClient(api_key="sk_test_...")
token = client.get_access_token("patent-data-api")

# Search patents ($0.02)
results = httpx.get(
    "https://patent-data-api.example.com/search",
    params={"q": "machine learning transformer", "limit": 5},
    headers={"X-Mainlayer-Token": token}
).json()

# Get full patent details ($0.05)
full = httpx.get(
    f"https://patent-data-api.example.com/patents/{results[0]['id']}",
    headers={"X-Mainlayer-Token": token}
).json()
print(f"Claims: {len(full['claims'])}")
```

## Endpoints

| Method | Path | Cost | Description |
|--------|------|------|-------------|
| `GET` | `/search` | $0.02 | Full-text search (title, abstract, claims) |
| `GET` | `/patents` | $0.01 | List patents (filter: `assignee`, `class`, `date_from`, `date_to`) |
| `GET` | `/patents/{id}` | $0.05 | Full record: specification, claims, citations, prior art |
| `GET` | `/health` | FREE | Health check |

## Install & Run

```bash
pip install mainlayer httpx
pip install -e ".[dev]"
uvicorn src.main:app --reload
pytest tests/
```

## Environment Variables

```
MAINLAYER_API_KEY      # Your Mainlayer API key
MAINLAYER_RESOURCE_ID  # Resource ID from dashboard
```

📚 [Mainlayer Docs](https://docs.mainlayer.fr) | [mainlayer.fr](https://mainlayer.fr)
