from encode_decode.encoder_decoder import encode_text, decode_text

# Your data to encode and decode
original_data = "Hello World"

# Encoding the data
encoded_data = encode_text(original_data)
print(f"Encoded Data: {encoded_data}")

# Decoding the data
decoded_data = decode_text(encoded_data)
print(f"Decoded Data: {decoded_data}")
