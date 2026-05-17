import subprocess
from core.logging.logger import logger

class ToolRunner:

    @staticmethod
    def run(command, timeout=300):

        logger.info(f"Executing: {' '.join(command)}")

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=timeout
            )

            return {
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }

        except subprocess.TimeoutExpired:

            logger.error("Command timed out")

            return {
                "success": False,
                "stdout": "",
                "stderr": "Timeout",
                "returncode": -1
            }
