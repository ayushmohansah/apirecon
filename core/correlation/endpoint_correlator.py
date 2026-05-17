class EndpointCorrelator:

    @staticmethod
    def correlate(*sources):

        correlated = {}

        for source in sources:

            if not source:
                continue

            for item in source:

                url = item.get("url") or item.get("path")

                if not url:
                    continue

                if url not in correlated:
                    correlated[url] = {
                        "sources": [],
                        "data": item
                    }

                correlated[url]["sources"].append(
                    item.get("source", "unknown")
                )

        return correlated
