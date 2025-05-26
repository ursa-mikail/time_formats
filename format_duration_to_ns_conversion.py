import datetime
import re

def ns_to_YYYY_MM_DD_HH_MM_SS_ms_µs_ns_format_duration(ns):
    # Get total microseconds (datetime.timedelta supports microseconds)
    total_us, ns_rem = divmod(ns, 1_000)

    # Get total milliseconds and remaining microseconds
    total_ms, us = divmod(total_us, 1_000)

    # Create timedelta from total milliseconds
    td = datetime.timedelta(milliseconds=total_ms)

    # Extract days, seconds
    days = td.days
    seconds = td.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)

    # Break down days into years and months approx (30.44 days/month, 365.25 days/year)
    years = days // 365
    days %= 365
    months = days // 30
    days %= 30

    return (
        f"{years:04d} year(s) {months:02d} month(s) {days:02d} day(s) "
        f"{hours:02d} hour(s) {minutes:02d} minute(s) {secs:02d} sec(s) "
        f"{(total_ms % 1000):03d} ms {us:03d} µs {ns_rem:03d} ns"
    )

def YYYY_MM_DD_HH_MM_SS_ms_µs_ns_format_duration_to_ns(year, month, day, hour, minute, second, ms, us, ns):
    # Approximations: 1 year = 365 days, 1 month = 30 days
    total_days = year * 365 + month * 30 + day
    total_seconds = total_days * 86400 + hour * 3600 + minute * 60 + second
    total_ns = total_seconds * 1_000_000_000 + ms * 1_000_000 + us * 1_000 + ns
    return f"{int(total_ns)} ns"


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

    # Extract and convert all parts to integers
    parts = match.groupdict()
    return tuple(int(parts[k]) for k in ['year', 'month', 'day', 'hour', 'minute', 'second', 'ms', 'us', 'ns'])

# Example
ts_str = "1970 year(s) 05 month(s) 08 day(s) 14 hour(s) 25 minute(s) 10 sec(s) 980 ms 000 µs 000 ns"
print(parse_timestamp_string(ts_str))
print(YYYY_MM_DD_HH_MM_SS_ms_µs_ns_format_duration_to_ns(1970, 5, 8, 14, 25, 10, 980, 0, 0))

# Example
duration_in_ns = 10469539104980
duration_in_YYYY_MM_DD_HH_MM_SS_ms_µs_ns = ns_to_YYYY_MM_DD_HH_MM_SS_ms_µs_ns_format_duration(duration_in_ns)
print(duration_in_YYYY_MM_DD_HH_MM_SS_ms_µs_ns)

time_elements = parse_timestamp_string(duration_in_YYYY_MM_DD_HH_MM_SS_ms_µs_ns)
recovered_time_in_ns = YYYY_MM_DD_HH_MM_SS_ms_µs_ns_format_duration_to_ns(*time_elements) # Use the unpacking operator *
print(recovered_time_in_ns)

recovered_time_in_ns = recovered_time_in_ns.replace(" ns", "")
assert duration_in_ns == int(recovered_time_in_ns)

print(f"Original: {duration_in_ns} ns")
print(f"Recovered: {recovered_time_in_ns} ns")

"""
(1970, 5, 8, 14, 25, 10, 980, 0, 0)
62139623110980000000 ns
0000 year(s) 00 month(s) 00 day(s) 02 hour(s) 54 minute(s) 29 sec(s) 539 ms 104 µs 980 ns
10469539104980 ns
Original: 10469539104980 ns
Recovered: 10469539104980 ns
"""
