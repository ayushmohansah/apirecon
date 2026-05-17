from core.utils.tool_runner import ToolRunner
from core.logging.logger import logger

class WaybackScanner:

    def __init__(self, domain):
        self.domain = domain

    def run(self):

        logger.info("Starting historical endpoint discovery")

        command = [
            "waybackurls",
            self.domain
        ]

        result = ToolRunner.run(command, timeout=300)

        findings = []

        for line in result["stdout"].splitlines():
            findings.append({
                "url": line,
                "source": "wayback"
            })

        return findings
