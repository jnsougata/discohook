import hashlib
import secrets


def compare_password(local: str, remote: str) -> bool:
    return secrets.compare_digest(hashlib.sha256(local.encode()).hexdigest(), remote)
