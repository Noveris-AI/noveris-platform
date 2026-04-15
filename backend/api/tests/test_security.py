from app.core.security import hash_password, verify_password


def test_hash_and_verify_password():
    plain = "SuperSecret123!"
    hashed = hash_password(plain)
    assert hashed != plain
    assert verify_password(plain, hashed) is True
    assert verify_password("wrong", hashed) is False
