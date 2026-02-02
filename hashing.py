from passlib.context import CryptContext

pwd_context = CryptContext(schemes = ["pbkdf2_sha256"], deprecated = "auto")

class Hash:
    def pbkdf2_sha256(password: str) -> str:
        return pwd_context.hash(password)