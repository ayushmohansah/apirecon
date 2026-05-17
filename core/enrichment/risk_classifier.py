class RiskClassifier:

    @staticmethod
    def classify(endpoint):

        url = endpoint.get("url", "")

        if any(keyword in url.lower() for keyword in [
            "admin",
            "internal",
            "debug",
            "private"
        ]):
            return "high"

        if any(keyword in url.lower() for keyword in [
            "api",
            "graphql",
            "swagger"
        ]):
            return "medium"

        return "low"
