import secrets

from itsdangerous import BadSignature, TimestampSigner

from app.core.config import settings

_signer = TimestampSigner(settings.csrf_secret)


def generate_csrf_token() -> str:
    token = secrets.token_urlsafe(32)
    return _signer.sign(token).decode("utf-8")


def validate_csrf_token(token: str) -> bool:
    try:
        _signer.unsign(token, max_age=3600)
        return True
    except BadSignature:
        return False
