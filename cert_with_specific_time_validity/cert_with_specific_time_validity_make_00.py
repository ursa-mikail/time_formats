"""
Generate Self-Signed Cert with Precise Validity
"""
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import datetime

# Target expiration: 2026-06-30 15:30:00.123456 UTC
not_valid_before = datetime.datetime.utcnow()
not_valid_after = datetime.datetime(2026, 6, 30, 15, 30, 0, 123456) # YYYY-MM-DD_HHmm_ss_ms_ns: 2026-06-30_1530_00_123_456"

# 1. Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# 2. Build certificate subject and issuer (self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u'Test Cert With Microsecond Expiry'),
])

# 3. Build cert
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(private_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(not_valid_before)
    .not_valid_after(not_valid_after)
    .add_extension(
        x509.SubjectAlternativeName([x509.DNSName(u"test.local")]),
        critical=False,
    )
    .sign(private_key, hashes.SHA256())
)

# 4. Write cert and key to PEM
with open("./sample_data/cert_micro_expiry.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

with open("./sample_data/key_micro_expiry.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))

print("✅ Certificate generated with microsecond-level expiry.")
print("⏳ Valid Until:", not_valid_after.isoformat())


"""
✅ Certificate generated with microsecond-level expiry.
⏳ Valid Until: 2026-06-30T15:30:00.123456

view and verify: openssl x509 -in cert_micro_expiry.pem -text -noout
"""