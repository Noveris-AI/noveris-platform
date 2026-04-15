import time

import redis

from app.core.config import settings

_redis_client: redis.Redis | None = None


def _get_redis() -> redis.Redis:
    global _redis_client
    if _redis_client is None:
        _redis_client = redis.from_url(settings.redis_url, decode_responses=True)
    return _redis_client


def check_rate_limit(key: str, max_requests: int, window_seconds: int) -> bool:
    """Return True if request is allowed, False if rate limited."""
    r = _get_redis()
    now = time.time()
    window_start = now - window_seconds

    pipe = r.pipeline()
    # Remove old entries outside the window
    pipe.zremrangebyscore(key, 0, window_start)
    # Count current entries in window
    pipe.zcard(key)
    # Add current request
    pipe.zadd(key, {str(now): now})
    # Expire the key after the window
    pipe.expire(key, window_seconds)
    results = pipe.execute()

    current_count = results[1]
    return current_count < max_requests
