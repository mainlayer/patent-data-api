"""
Patent Data API

Patent search and detailed patent records sold to AI agents per query via Mainlayer.
"""

from __future__ import annotations

import os
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException, Header, Query
from mainlayer import MainlayerClient

from .patents_db import (
    get_patent_by_id,
    search_patents,
    get_patents_by_assignee,
)
from .models import PatentSummary, PatentDetail, SearchResult

app = FastAPI(
    title="Patent Data API",
    description="Patent search and full-text patent records — billed per query via Mainlayer.",
    version="1.0.0",
)

ml = MainlayerClient(api_key=os.environ.get("MAINLAYER_API_KEY", ""))
RESOURCE_ID = os.environ.get("MAINLAYER_RESOURCE_ID", "")


async def require_payment(x_mainlayer_token: str = Header(...)):
    access = await ml.resources.verify_access(RESOURCE_ID, x_mainlayer_token)
    if not access.authorized:
        raise HTTPException(
            status_code=402,
            detail={
                "error": "payment_required",
                "message": "This endpoint is billed per query. Get access at mainlayer.fr",
                "payment_url": "https://mainlayer.fr",
            },
        )
    return access


@app.get("/patents")
async def list_patents(
    patent_class: Optional[str] = Query(None, description="Filter by CPC/IPC class code (e.g. G06N)"),
    assignee: Optional[str] = Query(None, description="Filter by assignee name (partial match)"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    _access=Depends(require_payment),
):
    """List patents with optional filters. Returns patent summaries."""
    # Use search_patents with a broad query to get all, then filter
    query = patent_class if patent_class else ""
    all_patents = search_patents(query=query, patent_class=patent_class)

    if assignee:
        all_patents = [p for p in all_patents if assignee.lower() in (p.assignee if hasattr(p, "assignee") else p.get("assignee", "")).lower()]

    total = len(all_patents)
    start = (page - 1) * page_size
    page_results = all_patents[start : start + page_size]

    def _serialize(p):
        return p.model_dump() if hasattr(p, "model_dump") else p

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "results": [_serialize(p) for p in page_results],
        "sampled_at": datetime.utcnow().isoformat() + "Z",
    }


@app.get("/patents/{patent_id}")
async def get_patent(
    patent_id: str,
    _access=Depends(require_payment),
):
    """Get full patent details including claims and description."""
    data = get_patent_by_id(patent_id)
    if data is None:
        raise HTTPException(status_code=404, detail=f"Patent '{patent_id}' not found")
    return data.model_dump() if hasattr(data, "model_dump") else data


@app.get("/search")
async def search(
    q: str = Query(..., description="Full-text search query across title, abstract, and claims"),
    patent_class: Optional[str] = Query(None, description="Filter by CPC/IPC class code"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    _access=Depends(require_payment),
):
    """
    Full-text patent search across titles, abstracts, and claim text.
    Returns ranked results matching the query.
    """
    results = search_patents(query=q, patent_class=patent_class)
    total = len(results)
    start = (page - 1) * page_size
    page_results = results[start : start + page_size]

    def _serialize(p):
        return p.model_dump() if hasattr(p, "model_dump") else p

    return {
        "query": q,
        "total": total,
        "page": page,
        "page_size": page_size,
        "results": [_serialize(p) for p in page_results],
        "sampled_at": datetime.utcnow().isoformat() + "Z",
    }


@app.get("/health")
async def health():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}
