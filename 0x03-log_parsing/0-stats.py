#!/usr/bin/python3
import sys


def print_stats(file_size, status_codes):
    """Print the accumulated metrics"""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


file_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue

        try:
            # Update the total file size
            file_size += int(parts[-1])

            # Update the status code count if it's valid
            status_code = parts[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1

        except ValueError:
            continue

        # Increment the line count
        line_count += 1

        # Every 10 lines, print the statistics
        if line_count % 10 == 0:
            print_stats(file_size, status_codes)

except KeyboardInterrupt:
    # Print the statistics when interrupted
    print_stats(file_size, status_codes)
    raise

# Print the final statistics after the loop ends
print_stats(file_size, status_codes)
