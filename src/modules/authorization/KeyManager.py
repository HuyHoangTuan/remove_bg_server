import secrets

def generateKey():
    return secrets.token_hex(16)

