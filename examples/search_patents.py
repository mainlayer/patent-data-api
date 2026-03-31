"""
Example: AI agent searching and retrieving patent data.

Usage:
    MAINLAYER_TOKEN=your-token python examples/search_patents.py
"""

import os
import httpx

BASE_URL = os.environ.get("PATENT_API_URL", "http://localhost:8000")
TOKEN = os.environ.get("MAINLAYER_TOKEN", "your-mainlayer-token-here")

HEADERS = {"X-Mainlayer-Token": TOKEN}


def search_patents(query: str, patent_class: str | None = None):
    params = {"q": query, "page_size": 5}
    if patent_class:
        params["patent_class"] = patent_class

    resp = httpx.get(f"{BASE_URL}/search", headers=HEADERS, params=params)

    if resp.status_code == 402:
        print("Payment required:", resp.json()["detail"]["message"])
        return []

    resp.raise_for_status()
    data = resp.json()
    print(f"Search '{query}': {data['total']} results\n")
    for p in data["results"][:5]:
        inventors = ", ".join(p.get("inventors", [])[:2])
        print(f"  [{p['id']}] {p['title'][:70]}")
        print(f"    Assignee: {p['assignee']}  |  Filed: {p.get('filing_date', 'N/A')}")
        print(f"    Inventors: {inventors}")
        print()
    return data["results"]


def get_patent_detail(patent_id: str):
    resp = httpx.get(f"{BASE_URL}/patents/{patent_id}", headers=HEADERS)

    if resp.status_code == 404:
        print(f"Patent {patent_id} not found")
        return
    if resp.status_code == 402:
        print("Payment required:", resp.json()["detail"]["message"])
        return

    resp.raise_for_status()
    p = resp.json()
    print(f"Patent: {p['id']}")
    print(f"  Title: {p['title']}")
    print(f"  Assignee: {p['assignee']}")
    print(f"  Status: {p.get('status', 'N/A')}  |  Class: {p.get('patent_class', 'N/A')}")
    print(f"  Abstract: {p['abstract'][:200]}…")
    claims = p.get("claims", [])
    if claims:
        print(f"  Claim 1: {claims[0]['text'][:150]}…")


def list_patents_by_class(patent_class: str):
    resp = httpx.get(
        f"{BASE_URL}/patents",
        headers=HEADERS,
        params={"patent_class": patent_class, "page_size": 5},
    )

    if resp.status_code == 402:
        print("Payment required:", resp.json()["detail"]["message"])
        return

    resp.raise_for_status()
    data = resp.json()
    print(f"\nPatents in class '{patent_class}': {data['total']} found")
    for p in data["results"][:3]:
        print(f"  {p['id']}: {p['title'][:60]}…")


if __name__ == "__main__":
    results = search_patents("neural network attention mechanism")
    if results:
        get_patent_detail(results[0]["id"])
    list_patents_by_class("G06N")
