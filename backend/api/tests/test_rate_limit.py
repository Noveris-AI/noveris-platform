from app.core.rate_limit import check_rate_limit


def test_rate_limit_allows_under_limit():
    key = "test:rate:allow"
    # First 5 requests should pass
    for _ in range(5):
        assert check_rate_limit(key, max_requests=5, window_seconds=60) is True


def test_rate_limit_blocks_over_limit():
    key = "test:rate:block"
    # 6th request should be blocked
    for _ in range(5):
        check_rate_limit(key, max_requests=5, window_seconds=60)
    assert check_rate_limit(key, max_requests=5, window_seconds=60) is False
