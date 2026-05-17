import httpx
from core.logging.logger import logger

COMMON_SWAGGER_PATHS = [
    "/swagger",
    "/swagger.json",
    "/openapi.json",
    "/api-docs",
    "/v2/api-docs",
    "/swagger/index.html"
]

class SwaggerScanner:

    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def run(self):

        findings = []

        logger.info("Starting Swagger/OpenAPI discovery")

        for path in COMMON_SWAGGER_PATHS:

            url = f"{self.base_url}{path}"

            try:
                response = httpx.get(url, timeout=5)

                if response.status_code < 400:

                    findings.append({
                        "url": url,
                        "status_code": response.status_code,
                        "content_type": response.headers.get("content-type", "")
                    })

                    logger.info(f"Swagger/OpenAPI discovered: {url}")

            except Exception:
                continue

        return findings
