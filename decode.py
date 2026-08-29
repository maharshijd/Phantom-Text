import hashlib

ZERO = "\u200b"
ONE = "\u200c"

def decode(cipher, key):
    hidden = ""
    for char in cipher:
        if char == ZERO or char == ONE:
            hidden += char

    decoded_bits = ""
    for char in hidden:
        if char == ZERO:
            decoded_bits += "0"
        else:
            decoded_bits += "1"

    if len(decoded_bits) % 8 != 0:
        return None

    decoded_bytes = bytearray()
    for i in range(0, len(decoded_bits), 8):
        byte = decoded_bits[i:i+8]
        decoded_bytes.append(int(byte, 2))

    key_hash = hashlib.sha256(key.encode("utf-8")).digest()

    decrypted = bytearray()
    for i, byte in enumerate(decoded_bytes):
        decrypted.append(byte ^ key_hash[i % len(key_hash)])

    if len(decrypted) < 8:
        return None

    if decrypted[:8] == key_hash[:8]:
        try:
            return decrypted[8:].decode("utf-8")
        except UnicodeDecodeError:
            return None
    else:
        return None