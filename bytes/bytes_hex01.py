
hex_data = 'abcdef'

print(bytearray.fromhex(hex_data))
print(bytes.fromhex(hex_data))
hex_bytes = bytes.fromhex(hex_data)

print(bytes.hex(hex_bytes))

