from app.core.pagination import PaginatedResponse, PaginationParams


def test_pagination_params_defaults():
    p = PaginationParams()
    assert p.page == 1
    assert p.page_size == 20


def test_paginated_response_serialization():
    data = {"items": [{"id": 1}, {"id": 2}], "total": 2, "page": 1, "page_size": 20, "pages": 1}
    response = PaginatedResponse[dict](**data)
    assert response.total == 2
    assert len(response.items) == 2
