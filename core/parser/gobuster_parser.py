import re

class GobusterParser:

    @staticmethod
    def parse(output):

        results = []

        for line in output.splitlines():

            if line.startswith("/"):

                match = re.search(r'([^\s]+)\s+\(Status:\s(\d+)', line)

                if match:

                    results.append({
                        "path": match.group(1),
                        "status_code": int(match.group(2))
                    })

        return results
