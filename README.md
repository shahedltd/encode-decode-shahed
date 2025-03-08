# encode-decode-shahed
encode-decode-shahed is a simple Python package that provides functions for encoding and decoding strings using a basic reversal technique. This package is designed to help you understand the basics of encoding and decoding, and it can be extended to support more complex transformations in the future.
# Features
Encode: Encodes a string by reversing its characters.
Decode: Decodes the string back to the original by reversing it again.
# Installation
To install the package, run:
pip install encode-decode-shahed
# Usage
After installing the package, you can use the encode_text and decode_text functions as shown below:

from encode_decode.encoder_decoder import encode_text, decode_text

# Example data
data = "Hello, PyPI!"

# Encode the data
encoded = encode_text(data)
print(f"Encoded: {encoded}")

# Decode the data
decoded = decode_text(encoded)
print(f"Decoded: {decoded}")
# Example Output:
Encoded: !IPyH ,olleH
Decoded: Hello, PyPI!
# License
This project is licensed under the MIT License - see the LICENSE file for details.
# Author 
Shahed Rahman
# Here is my package url
https://pypi.org/project/encode-decode-shahed/
