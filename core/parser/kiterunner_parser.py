class KiterunnerParser:

    @staticmethod
    def parse(output):

        findings = []

        for line in output.splitlines():

            if "=>" in line:

                findings.append({
                    "raw": line
                })

        return findings
