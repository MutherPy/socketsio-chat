from fernet import Fernet, InvalidToken
import typing as t


def encrypt_path(path: str, key: bytes) -> str:
    f = Fernet(key)
    encrypted_path = f.encrypt(path)
    return encrypted_path.decode('utf-8')


def decrypt_path(e_path: t.Union[str, bytes], key: bytes) -> t.Union[str, None]:
    f = Fernet(key)
    if not isinstance(e_path, bytes):
        e_path = bytes(e_path, encoding='utf-8')
    try:
        decrypted_path = f.decrypt(e_path)
        return decrypted_path.decode('utf-8')
    except InvalidToken:
        return None
