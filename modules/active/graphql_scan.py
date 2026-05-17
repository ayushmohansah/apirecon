import httpx
from core.logging.logger import logger

GRAPHQL_PATHS = [
    "/graphql",
    "/graphiql",
    "/api/graphql",
    "/query"
]

class GraphQLScanner:

    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

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

                if response.status_code < 500:

                    findings.append({
                        "url": url,
                        "status_code": response.status_code
                    })

                    logger.info(f"Potential GraphQL endpoint discovered: {url}")

            except Exception:
                continue

        return findings
