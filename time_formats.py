from datetime import datetime
import time

# Current time in various formats
now = datetime.now()

# Format examples
formats = [
    "%Y-%m-%d %H:%M:%S",        # 2024-11-30 18:32:35
    "%Y-%m-%d_%H%M_%S",         # 2024-11-30_18_32_35
    "%a %b %d %H:%M:%S %Z %Y",  # Sat Nov 30 18:32:35 PST 2024
    "%Y%m%d%H%M%S",             # 20241130183235
    "%I:%M:%S %p",              # 06:32:35 PM
    "%Y-%m-%dT%H:%M:%S",        # 2024-11-30T18:32:35  // ISO 8601
    "%a, %d %b %Y %H:%M:%S %z", # RFC 2822 format
    "%Y-%m-%d %H:%M:%S.%f",     # With microseconds (e.g., 2024-12-01 02:39:29.123456)

    "%Y-%m-%dT%H:%M:%S%z",      # ISO 8601 with UTC offset
    "%c",                       # Sat Nov 30 18:32:35 2024
    "%U",                       # Week number
    "%j",                       # Day of the year
    "%x",                       # 11/30/24 # Locale-specific date format
    "%X",                       # 18:32:35
    "%F",                       # 2024-11-30
    "%A, %B %d, %Y",            # Full weekday name, full month, day, and year
    "%Y-%m-%d %H:%M:%S %Z",     # Date, time with timezone
    "%I:%M:%S %p",              # 12-hour time with AM/PM
    
    "%Y-%m-%d %H:%M:%S.%f",     # Includes microseconds
]

# Print formatted times
for fmt in formats:
    print(f"{fmt}: {now.strftime(fmt)}")
print('==============================================================')

# Unix timestamp (seconds since Unix epoch)
unix_timestamp = int(time.time())
print(f"Unix timestamp: {unix_timestamp}")

# Current time in seconds, including microseconds (float)
current_time_seconds = time.time()
# Getting microseconds (fractional part of time.time())
microseconds = int((current_time_seconds % 1) * 1_000_000)

# High resolution performance counter (for nanoseconds)
perf_counter = time.perf_counter()
nanoseconds = int(perf_counter * 1_000_000_000)

# Get the current time with microseconds using datetime
current_datetime = datetime.now()
current_time_with_micro = current_datetime.strftime(formats[-1])  # Includes microseconds

# Display results
print(f"Current time in microseconds: {current_time_with_micro}")
print(f"Current time in seconds (including microseconds): {current_time_seconds}")
print(f"Microseconds part: {microseconds}")
print(f"High-resolution time in nanoseconds: {nanoseconds}")

"""
%Y-%m-%d %H:%M:%S: 2024-12-01 02:54:09
%Y-%m-%d_%H%M_%S: 2024-12-01_0254_09
%a %b %d %H:%M:%S %Z %Y: Sun Dec 01 02:54:09  2024
%Y%m%d%H%M%S: 20241201025409
%I:%M:%S %p: 02:54:09 AM
%Y-%m-%dT%H:%M:%S: 2024-12-01T02:54:09
%a, %d %b %Y %H:%M:%S %z: Sun, 01 Dec 2024 02:54:09 
%Y-%m-%d %H:%M:%S.%f: 2024-12-01 02:54:09.457075
%Y-%m-%dT%H:%M:%S%z: 2024-12-01T02:54:09
%c: Sun Dec  1 02:54:09 2024
%U: 48
%j: 336
%x: 12/01/24
%X: 02:54:09
%F: 2024-12-01
%A, %B %d, %Y: Sunday, December 01, 2024
%Y-%m-%d %H:%M:%S %Z: 2024-12-01 02:54:09 
%I:%M:%S %p: 02:54:09 AM
%Y-%m-%d %H:%M:%S.%f: 2024-12-01 02:54:09.457075
==============================================================
Unix timestamp: 1733021649
Current time in microseconds: 2024-12-01 02:54:09.466985
Current time in seconds (including microseconds): 1733021649.466842
Microseconds part: 466841
High-resolution time in nanoseconds: 7922770628677
"""