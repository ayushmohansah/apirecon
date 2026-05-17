from core.utils.tool_runner import ToolRunner
from core.logging.logger import logger

class NmapScanner:

    def __init__(self, target):
        self.target = target

    def run(self):

        logger.info("Starting Nmap service scan")

        command = [
            "nmap",
            "-sV",
            "-Pn",
            self.target
        ]

        result = ToolRunner.run(command)

        return result
