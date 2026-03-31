from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date


class PatentSummary(BaseModel):
    id: str
    title: str
    assignee: str
    inventors: List[str]
    filing_date: date
    grant_date: Optional[date]
    patent_class: str
    abstract: str


class PatentClaim(BaseModel):
    number: int
    text: str
    claim_type: str  # independent | dependent


class PatentDetail(PatentSummary):
    claims: List[PatentClaim]
    description: str
    priority_date: Optional[date]
    publication_number: str
    country: str
    status: str  # granted | pending | expired | abandoned
    forward_citation_count: int
    backward_citation_count: int


class Citation(BaseModel):
    patent_id: str
    title: str
    assignee: str
    filing_date: date
    relationship: str  # forward | backward


class CitationResponse(BaseModel):
    patent_id: str
    forward_citations: List[Citation]
    backward_citations: List[Citation]
    total_forward: int
    total_backward: int


class SearchResult(BaseModel):
    total: int
    page: int
    page_size: int
    results: List[PatentSummary]


class PatentClass(BaseModel):
    code: str
    name: str
    description: str
    subclasses: List[str]


class CategoriesResponse(BaseModel):
    total: int
    categories: List[PatentClass]


class PaymentRequired(BaseModel):
    error: str = "payment_required"
    message: str
    cost_usd: float
    payment_url: str


class MainlayerPaymentInfo(BaseModel):
    resource_id: str
    cost_usd: float
    description: str
