import datetime
import re

def ns_to_YYYY_MM_DD_HH_MM_SS_ms_µs_ns_format_timestamp(ns):
    us, rem_ns = divmod(ns, 1000)  # microseconds and remaining ns
    epoch = datetime.datetime(1970, 1, 1)
    # datetime accepts only microsecond precision
    dt = epoch + datetime.timedelta(microseconds=us)
    
    return (
        f"{dt.year:04d} year(s) {dt.month:02d} month(s) {dt.day:02d} day(s) "
        f"{dt.hour:02d} hour(s) {dt.minute:02d} minute(s) {dt.second:02d} sec(s) "
        f"{dt.microsecond // 1000:03d} ms {(dt.microsecond % 1000):03d} µs {rem_ns:03d} ns"
    )

def YYYY_MM_DD_HH_MM_SS_ms_µs_ns_format_timestamp_to_ns(year, month, day, hour, minute, second, ms, us, ns):
    dt = datetime.datetime(year, month, day, hour, minute, second, microsecond=ms * 1000 + us)
    epoch = datetime.datetime(1970, 1, 1)
    delta = dt - epoch
    delta_ns = delta.days * 86400 * 1_000_000_000
    delta_ns += delta.seconds * 1_000_000_000
    delta_ns += delta.microseconds * 1_000
    total_ns = delta_ns + ns
    return f"{total_ns} ns"


def parse_timestamp_string(ts_string):
    pattern = (
        r"(?P<year>\d{4}) year\(s\) "
        r"(?P<month>\d{2}) month\(s\) "
        r"(?P<day>\d{2}) day\(s\) "
        r"(?P<hour>\d{2}) hour\(s\) "
        r"(?P<minute>\d{2}) minute\(s\) "
        r"(?P<second>\d{2}) sec\(s\) "
        r"(?P<ms>\d{3}) ms "
        r"(?P<us>\d{3}) µs "
        r"(?P<ns>\d{3}) ns"
    )
    match = re.match(pattern, ts_string)
    if not match:
        raise ValueError("Timestamp string format is invalid")
    parts = match.groupdict()
    return tuple(int(parts[k]) for k in ['year', 'month', 'day', 'hour', 'minute', 'second', 'ms', 'us', 'ns'])

# Test case
ts_in_ns = 1748286178639328861  # example timestamp in nanoseconds
formatted = ns_to_YYYY_MM_DD_HH_MM_SS_ms_µs_ns_format_timestamp(ts_in_ns)
print("Formatted:", formatted)

parts = parse_timestamp_string(formatted)
recovered_ns = YYYY_MM_DD_HH_MM_SS_ms_µs_ns_format_timestamp_to_ns(*parts)
print("Recovered ns:", recovered_ns)

assert int(recovered_ns.replace(" ns", "")) == ts_in_ns
print("Assertion passed.")

"""
Formatted: 2025 year(s) 05 month(s) 26 day(s) 19 hour(s) 02 minute(s) 58 sec(s) 639 ms 328 µs 861 ns
Recovered ns: 1748286178639328861 ns
Assertion passed.
"""