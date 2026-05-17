import httpx

from core.logging.logger import logger

WAF_SIGNATURES = {
    "cloudflare": ["cloudflare", "cf-ray"],
    "akamai": ["akamai"],
    "imperva": ["imperva", "incapsula"],
    "aws": ["x-amzn-requestid"],
    "kong": ["kong"]
}

class WAFDetector:

    def __init__(self, base_url):
        self.base_url = base_url

    def run(self):

        logger.info("Starting WAF/CDN detection")

        findings = []

        try:
            response = httpx.get(self.base_url, timeout=10)

            headers = str(response.headers).lower()

            for vendor, signatures in WAF_SIGNATURES.items():

                for signature in signatures:

                    if signature in headers:

                        findings.append({
                            "vendor": vendor,
                            "signature": signature
                        })

        except Exception:
            logger.error("WAF detection failed")

        return findings
