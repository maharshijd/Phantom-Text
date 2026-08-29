import streamlit as st
st.set_page_config(
    page_title="PHANTOMTEXT",
    page_icon="👻",
    layout="wide"
)
ZERO = "\u200b"
ONE = "\u200c"

def encode(message, cover):
    data = message.encode("utf-8")
    bits = ""
    for i in data:
        binary = bin(i)[2:].zfill(8)
        bits = bits + binary
    encoded = ""
    for bit in bits:
        if bit == "0":
            encoded = encoded + ZERO
        else:
            encoded = encoded + ONE
    final = cover[0] + encoded + cover[1:]
    return final

def decode(cipher):
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
    decoded_bytes = bytearray()
    for i in range(0, len(decoded_bits), 8):
        byte = decoded_bits[i:i+8]
        value = int(byte, 2)
        decoded_bytes.append(value)

    return decoded_bytes.decode("utf-8")

cover = "👻👻👻"
message = "Hi"

result = encode(message, cover)

print(result)
print(repr(result))

original = decode(result)

print(original)