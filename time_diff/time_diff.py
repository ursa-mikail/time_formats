import time
from datetime import datetime

def format_timestamp(ts):
    dt = datetime.fromtimestamp(ts)
    ns_total = int((ts - int(ts)) * 1_000_000_000)
    ms = ns_total // 1_000_000
    us = (ns_total // 1_000) % 1_000
    ns_last_2 = (ns_total // 10) % 100

    return dt.strftime(f"%Y-%m-%d_%H%M_%S_{ms:03d}_{us:03d}_{ns_last_2:02d}")

# Start
start = time.time_ns()
start_sec = start / 1_000_000_000
start_fmt = format_timestamp(start_sec)

time.sleep(5)

# End
end = time.time_ns()
end_sec = end / 1_000_000_000
end_fmt = format_timestamp(end_sec)

# Difference
delta_ns = end - start
delta_sec = delta_ns / 1_000_000_000
delta_ms = (delta_ns // 1_000_000) % 1000
delta_us = (delta_ns // 1_000) % 1000
delta_ns_last_2 = (delta_ns // 10) % 100
delta_int_sec = delta_ns // 1_000_000_000

# Output
print("Start formatted :", start_fmt)
print("End formatted   :", end_fmt)
print()

print("⏱ Full Range Time Difference:")
print(f"-> Human Format Delta : 0000-00-00_0000_{delta_int_sec:02d}_{delta_ms:03d}_{delta_us:03d}_{delta_ns_last_2:02d}")
print(f"-> Epoch Format Delta : {delta_sec:.9f} seconds")

