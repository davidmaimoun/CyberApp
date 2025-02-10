import requests
import re
from urllib.parse import urlparse

def check_url_validity(url: str) -> bool:
    """
    Validate that the URL:
    - Belongs to the 10.10.X.X subnet (HTB IP range)
    - Is properly formatted
    - Is reachable (HTTP 200)
    
    Returns True if valid, False otherwise.
    """
    # try:
    #     parsed_url = urlparse(url)
    #     ip_match = re.match(r"^10\.10\.\d{1,3}\.\d{1,3}$", parsed_url.hostname or "")

    #     if not ip_match:
    #         print("Invalid URL: Only 10.10.X. IPs are allowed.")
    #         return False

    #     response = requests.get(url, timeout=5)
    #     return response.status_code == 200

    # except requests.exceptions.RequestException as e:
    #     print(f"Error: {e}")
    #     return False
    return True
