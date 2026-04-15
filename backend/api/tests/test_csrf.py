from app.core.csrf import generate_csrf_token, validate_csrf_token


def test_csrf_token_lifecycle():
    token = generate_csrf_token()
    assert isinstance(token, str)
    assert validate_csrf_token(token) is True


def test_csrf_invalid_token():
    assert validate_csrf_token("invalid-token") is False
