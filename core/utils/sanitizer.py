import re
from urllib.parse import urlparse

def sanitize_target(target):

    parsed = urlparse(target)

    hostname = parsed.netloc or parsed.path

    hostname = hostname.replace(":", "_")

    hostname = re.sub(r'[^a-zA-Z0-9_.-]', '_', hostname)

    return hostname
