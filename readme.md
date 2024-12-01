# time_formats

This project provides a collection of common and custom time formats that can be easily used in Python. It covers a variety of standard date and time representations, ranging from simple `YYYY-MM-DD` formats to more detailed ones such as ISO 8601 with timezone information and Unix timestamps with milliseconds.

## Supported Formats

The following are the supported time formats:

### 1. Basic Date and Time Formats:
- **`%Y-%m-%d %H:%M:%S`** — `2024-12-01 02:39:29`
- **`%a %b %d %H:%M:%S %Z %Y`** — `Sat Dec 01 02:39:29 PST 2024`
- **`%Y%m%d%H%M%S`** — `20241201023929`
- **`%I:%M:%S %p`** — `02:39:29 AM`
- **`%Y-%m-%dT%H:%M:%S`** — `2024-12-01T02:39:29`
- **`%c`** — `Sat Dec 01 02:39:29 2024`
- **`%x`** — `12/01/24` (Locale-specific date format)

### 2. Week and Day Formats:
- **`%U`** — Week number of the year (Sunday as first day, 00 to 53)
- **`%W`** — Week number of the year (Monday as first day, 00 to 53)
- **`%V`** — ISO 8601 week number (00 to 53)

### 3. Timezone Formats:
- **`%Z`** — Time zone abbreviation (e.g., `PST`, `UTC`)
- **`%z`** — UTC offset (e.g., `+0000`, `-0800`)

### 4. Advanced Formats:
- **`%Y-%m-%dT%H:%M:%S%z`** — ISO 8601 with UTC offset (`2024-12-01T02:39:29-0800`)
- **`%a, %d %b %Y %H:%M:%S %z`** — RFC 2822 format (`Sat, 01 Dec 2024 02:39:29 -0800`)

### 5. Precision Formats:
- **`%f`** — Microseconds (`2024-12-01 02:39:29.123456`)
- **`int(time.time() * 1000)`** — Unix timestamp in milliseconds (`1732978355123`)

