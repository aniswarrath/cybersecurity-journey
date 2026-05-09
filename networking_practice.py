# Networking Practice — May 9, 2026
# Concepts: DNS lookup, socket connections, network scanning

import socket

# DNS lookup — find IP of any domain
def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        return f"{domain} → {ip}"
    except socket.gaierror:
        return f"{domain} → not found"

# Test DNS lookups
domains = ["google.com", "razorpay.com", "github.com"]
for domain in domains:
    print(dns_lookup(domain))