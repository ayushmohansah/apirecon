import httpx
from core.logging.logger import logger

GRAPHQL_PATHS = [
    "/graphql",
    "/graphiql",
    "/api/graphql",
    "/query"
]

GRAPHQL_INDICATORS = [
    "errors",
    "data",
    "graphql"
]

class GraphQLScanner:

    def __init__(self, base_url):
        self.base_url = self._normalize(base_url)

    def _normalize(self, value):
        return value.rstrip("/")

    def _is_valid_graphql(self, response):

        if response.status_code >= 400:
            return False

        content_type = response.headers.get("content-type", "")

        if "json" not in content_type.lower():
            return False

        body = response.text.lower()

        return any(indicator in body for indicator in GRAPHQL_INDICATORS)

    def run(self):

        findings = []

        logger.info("Starting GraphQL discovery")

        for path in GRAPHQL_PATHS:

            url = f"{self.base_url}{path}"

            try:
                response = httpx.post(
                    url,
                    json={"query": "{__typename}"},
                    timeout=5
                )

                if self._is_valid_graphql(response):

                    findings.append({
                        "url": url,
                        "status_code": response.status_code,
                        "source": "graphql"
                    })

                    logger.info(f"Valid GraphQL endpoint discovered: {url}")

            except Exception:
                continue

        return findings
