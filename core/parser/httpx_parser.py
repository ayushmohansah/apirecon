import re

class HTTPXParser:

    @staticmethod
    def parse(output):

        results = []

        for line in output.splitlines():

            result = {
                "raw": line,
                "url": None,
                "status_code": None,
                "title": None,
                "technologies": []
            }

            url_match = re.search(r'(https?://[^\s]+)', line)
            status_match = re.search(r'\[(\d{3})\]', line)

            if url_match:
                result["url"] = url_match.group(1)

            if status_match:
                result["status_code"] = int(status_match.group(1))

            tech_matches = re.findall(r'\[(.*?)\]', line)

            if tech_matches:
                result["technologies"] = tech_matches

            results.append(result)

        return results
