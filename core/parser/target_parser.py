from urllib.parse import urlparse
import ipaddress

class TargetParser:

    def __init__(self, raw_target):
        self.raw_target = raw_target.strip()

    def normalize(self):

        target = self.raw_target

        if not target.startswith(("http://", "https://")):
            target = f"http://{target}"

        parsed = urlparse(target)

        hostname = parsed.hostname or ""
        port = parsed.port

        scheme = parsed.scheme or "http"

        base_url = f"{scheme}://{hostname}"

        if port:
            base_url += f":{port}"

        return {
            "raw": self.raw_target,
            "scheme": scheme,
            "host": hostname,
            "port": port,
            "domain": hostname,
            "base_url": base_url,
            "path": parsed.path,
            "fragment": parsed.fragment,
            "is_local": self._is_local(hostname),
            "is_private_ip": self._is_private_ip(hostname)
        }

    def _is_local(self, hostname):

        return hostname in [
            "localhost",
            "127.0.0.1"
        ]

    def _is_private_ip(self, hostname):

        try:
            ip = ipaddress.ip_address(hostname)
            return ip.is_private
        except Exception:
            return False
