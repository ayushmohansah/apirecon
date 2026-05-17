import json

class HTTPXParser:

    @staticmethod
    def parse(output):
        results = []

        for line in output.splitlines():

            try:
                data = json.loads(line)

                results.append({
                    'url': data.get('url'),
                    'status_code': data.get('status_code'),
                    'title': data.get('title'),
                    'technologies': data.get('tech', []),
                    'source': 'httpx'
                })

            except Exception:
                continue

        return results
