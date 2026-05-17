from core.utils.tool_runner import ToolRunner
from core.logging.logger import logger

class HTTPXProbe:

    def __init__(self, target):
        self.target = target

    def run(self):

        logger.info("Starting HTTPX probing")

        command = [
            "httpx",
            "-u",
            self.target,
            "-tech-detect",
            "-status-code",
            "-title"
        ]

        result = ToolRunner.run(command)

        return result
