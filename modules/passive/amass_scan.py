from core.utils.tool_runner import ToolRunner
from core.logging.logger import logger

class AmassScanner:

    def __init__(self, target):
        self.target = target

    def run(self):

        logger.info("Starting Amass passive enumeration")

        command = [
            "amass",
            "enum",
            "-passive",
            "-d",
            self.target
        ]

        result = ToolRunner.run(command)

        if result["success"]:
            subdomains = result["stdout"].splitlines()
            return subdomains

        return []
