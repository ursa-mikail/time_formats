#!pip install pycryptodome
"""
X.509 certificates use the following formats:
For dates before the year 2050: UTC Time – YYMMDDHHMMSSZ
For dates from 2050 onward: Generalized Time – YYYYMMDDHHMMSSZ

Option to calculate the same for timeformat YYYY-MM-DD_HHmm_ss_ms_ns
"""
import datetime
import ssl
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def read_cert_lifespan(cert_path):
    with open(cert_path, "rb") as f:
        cert_data = f.read()
    
    cert = x509.load_pem_x509_certificate(cert_data, default_backend())
    
    not_before = cert.not_valid_before
    not_after = cert.not_valid_after
    now = datetime.datetime.utcnow()

    remaining = not_after - now
    total_lifespan = not_after - not_before

    print("Certificate Subject:", cert.subject.rfc4514_string())
    print("Valid From:", not_before)
    print("Valid Until:", not_after)
    print("Total Lifespan:", total_lifespan)
    print("Time Remaining:", remaining if remaining.total_seconds() > 0 else "Expired")

def parse_custom_time(timestr):
    # Expected format: YYYY-MM-DD_HHmm_ss_ms_ns
    try:
        parts = timestr.split("_")
        date_part = parts[0]
        hourmin = parts[1]
        sec = int(parts[2])
        ms = int(parts[3])
        ns = int(parts[4])

        dt = datetime.datetime.strptime(date_part + hourmin, "%Y-%m-%d%H%M")
        dt = dt.replace(second=sec, microsecond=(ms * 1000 + ns // 1000))
        return dt
    except Exception as e:
        raise ValueError(f"Invalid time format: {e}")

def compare_to_custom_time(cert_path, custom_timestr):
    with open(cert_path, "rb") as f:
        cert_data = f.read()

    cert = x509.load_pem_x509_certificate(cert_data, default_backend())
    not_before = cert.not_valid_before
    not_after = cert.not_valid_after
    custom_time = parse_custom_time(custom_timestr)

    if custom_time < not_before:
        status = "Not yet valid"
    elif custom_time > not_after:
        status = "Expired"
    else:
        time_left = not_after - custom_time
        status = f"Valid - Time remaining from custom timestamp: {time_left}"

    print(f"Custom Time: {custom_time}")
    print(f"Certificate Status at that time: {status}")

# Example usage:
cert_path = "./sample_data/cert_micro_expiry.pem" # "./sample_data/cert.pem"
read_cert_lifespan(cert_path)
compare_to_custom_time(cert_path, "2026-06-30_1530_00_123_456")

"""
Certificate Subject: CN=Test Cert With Microsecond Expiry
Valid From: 2025-06-27 19:44:21
Valid Until: 2026-06-30 15:30:00
Total Lifespan: 367 days, 19:45:39
Time Remaining: 367 days, 19:44:53.100411
Custom Time: 2026-06-30 15:30:00.123000
Certificate Status at that time: Expired

For general testing: !openssl req -x509 -newkey rsa:2048 -keyout test_key.pem -out "./sample_data/cert.pem" -days 10 -nodes -subj "/CN=Test Cert"

"""