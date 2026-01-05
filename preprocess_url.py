from urllib.parse import urlparse
import socket
import torch
import re

# Check if the URL uses an IP address instead of a domain
def has_ip(url):
    try:
        host = urlparse(url).netloc
        socket.inet_aton(host)
        return 1
    except:
        return 0

def preprocess_url(url):
    parsed = urlparse(url)
    hostname = parsed.netloc
    path = parsed.path

    features = [
        has_ip(url),                                  # 1. Have_IP
        1 if '@' in url else 0,                        # 2. Have_At
        len(url),                                      # 3. URL_Length
        path.count('/'),                               # 4. URL_Depth
        1 if '//' in url.replace('://', '') else 0,    # 5. Redirection
        1 if 'https' in parsed.netloc else 0,          # 6. https_Domain
        1 if 'tinyurl' in url or 'bit.ly' in url else 0, # 7. TinyURL
        1 if '-' in hostname else 0,                   # 8. Prefix/Suffix
        1,                                             # 9. DNS_Record (placeholder)
        1000,                                          # 10. Web_Traffic (placeholder)
        1,                                             # 11. Domain_Age (placeholder)
        1,                                             # 12. Domain_End (placeholder)
        0,                                             # 13. iFrame (placeholder)
        0,                                             # 14. Mouse_Over (placeholder)
        0,                                             # 15. Right_Click (placeholder)
        0,                                             # 16. Web_Forwards (placeholder)
        1 if re.search(r'https?://\d+\.\d+\.\d+\.\d+', url) else 0,  # 17. IP_in_URL
        1 if re.search(r'login|signin|account', url.lower()) else 0, # 18. Sensitive_Keyword
        1 if len(hostname.split('.')) > 3 else 0,                     # 19. Subdomain_Count
        1 if re.match(r'https?://[^/]*\.[a-z]{2,}/.*[=]{1}', url) else 0  # 20. Query_String_Present
    ]

    return torch.tensor(features, dtype=torch.float32)
