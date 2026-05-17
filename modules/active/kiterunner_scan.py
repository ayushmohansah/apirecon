from core.utils.tool_runner import ToolRunner
from core.logging.logger import logger

class KiterunnerScanner:

    def __init__(self, base_url):
        self.base_url = base_url

    def run(self):

        logger.info("Starting Kiterunner API discovery")

        command = [
            "kr",
            "scan",
            self.base_url,
            "-x",
            "20"
        ]

        result = ToolRunner.run(command, timeout=1200)

        return result
