import shutil
from core.logging.logger import logger

REQUIRED_TOOLS = [
    "nmap",
    "amass",
    "gobuster",
    "kr",
    "httpx"
]

def check_tools():

    missing = []

    logger.info("Checking external dependencies...")

    for tool in REQUIRED_TOOLS:

        if shutil.which(tool):
            logger.info(f"[FOUND] {tool}")
        else:
            logger.warning(f"[MISSING] {tool}")
            missing.append(tool)

    return missing
