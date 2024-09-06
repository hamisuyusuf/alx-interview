#!/usr/bin/env python3
"""
UTF-8 encoding is variable-width
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    return: True if valid UTF-8 encoding, False otherwise
    """

    num_bytes = 0

    # Masks for checking the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Check only the 8 least significant bits of each integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Count the number of leading
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7) != 0:  # 1-byte character (0xxxxxxx)
                return False
        else:
            # Check that the byte starts with 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
