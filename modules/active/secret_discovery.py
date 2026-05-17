import re
import httpx

from core.logging.logger import logger

SECRET_PATTERNS = {
    "api_key": r'(?i)(api[_-]?key|apikey)["\']?\s*[:=]\s*["\']([a-zA-Z0-9\-_]+)',
    "jwt": r'eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+'
}

class SecretDiscovery:

    def __init__(self, base_url):
        self.base_url = base_url

    def run(self):

        logger.info("Starting secret discovery")

        findings = []

        try:
            response = httpx.get(self.base_url, timeout=10)

            content = response.text

            for secret_type, pattern in SECRET_PATTERNS.items():

                matches = re.findall(pattern, content)

                for match in matches:
                    findings.append({
                        "type": secret_type,
                        "value": str(match)
                    })

        except Exception:
            logger.error("Secret discovery failed")

        return findings
