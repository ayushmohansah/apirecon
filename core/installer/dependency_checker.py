import shutil

from core.logging.logger import logger
from core.installer.auto_installer import AutoInstaller

REQUIRED_TOOLS = [
    "nmap",
    "amass",
    "gobuster",
    "kr",
    "httpx"
]

def check_tools(auto_install=True):

    missing = []

    logger.info("Checking external dependencies...")

    for tool in REQUIRED_TOOLS:

        if shutil.which(tool):
            logger.info(f"[FOUND] {tool}")

        else:

            logger.warning(f"[MISSING] {tool}")

            missing.append(tool)

            if auto_install:

                logger.info(f"Attempting installation for {tool}")

                success = AutoInstaller.install(tool)

                if success:
                    logger.info(f"Successfully installed {tool}")
                else:
                    logger.error(f"Failed to install {tool}")

    return missing
