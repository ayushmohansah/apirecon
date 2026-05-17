from core.utils.tool_runner import ToolRunner
from core.logging.logger import logger

COMMON_API_WORDLIST = "/usr/share/seclists/Discovery/Web-Content/common.txt"

class GobusterScanner:

    def __init__(self, base_url, threads=20):
        self.base_url = base_url
        self.threads = threads

    def run(self):

        logger.info("Starting Gobuster API discovery")

        command = [
            "gobuster",
            "dir",
            "-u",
            self.base_url,
            "-w",
            COMMON_API_WORDLIST,
            "-t",
            str(self.threads),
            "--no-error"
        ]

        result = ToolRunner.run(command, timeout=600)

        return result
