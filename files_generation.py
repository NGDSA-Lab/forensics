import os

original = """ {YOUR_FLAG_HERE}
"""
original_bytes = original.encode()

# Generate random bytes for file1
file1 = os.urandom(len(original_bytes))

# Create file2 by XORing original with file1
file2 = bytes([a ^ b for a, b in zip(original_bytes, file1)])

# Save file1 as HEX (so it can be used as a CyberChef key)
with open("file1.hex", "w") as f:
    f.write(file1.hex())  # Hex format

# Save file2 as raw binary
with open("file2.bin", "wb") as f:
    f.write(file2)
