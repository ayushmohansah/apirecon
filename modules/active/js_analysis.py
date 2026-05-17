import re
import httpx

from core.logging.logger import logger

class JavaScriptAnalyzer:

    ENDPOINT_REGEX = [
        r'"(/api/[^"]+)"',
        r"'(/api/[^']+)'",
        r'https?://[^\s\"\']+'
    ]

    def __init__(self, base_url):
        self.base_url = base_url

    def run(self):

        logger.info("Starting JavaScript intelligence analysis")

        findings = []

        try:
            response = httpx.get(self.base_url, timeout=10)

            script_urls = re.findall(
                r'<script[^>]+src=["\']([^"\']+)["\']',
                response.text
            )

            for script in script_urls:

                if script.startswith("/"):
                    script = self.base_url.rstrip("/") + script

                try:
                    js_response = httpx.get(script, timeout=10)

                    content = js_response.text

                    for pattern in self.ENDPOINT_REGEX:

                        matches = re.findall(pattern, content)

                        for match in matches:
                            findings.append({
                                "source": "javascript",
                                "url": match
                            })

                except Exception:
                    continue

        except Exception:
            logger.error("JavaScript analysis failed")

        return findings
