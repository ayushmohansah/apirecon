import shutil
import subprocess

from core.logging.logger import logger

APT_MAPPING = {
    "nmap": "nmap",
    "amass": "amass",
    "gobuster": "gobuster"
}

GO_MAPPING = {
    "httpx": "github.com/projectdiscovery/httpx/cmd/httpx@latest",
    "kr": "github.com/assetnote/kiterunner@latest"
}

class AutoInstaller:

    @staticmethod
    def install(tool_name):

        logger.info(f"Attempting automatic installation for: {tool_name}")

        if shutil.which(tool_name):
            logger.info(f"{tool_name} already installed")
            return True

        if tool_name in APT_MAPPING:
            return AutoInstaller._install_apt(tool_name)

        if tool_name in GO_MAPPING:
            return AutoInstaller._install_go(tool_name)

        logger.error(f"No installer mapping found for {tool_name}")
        return False

    @staticmethod
    def _install_apt(tool_name):

        package = APT_MAPPING[tool_name]

        command = [
            "sudo",
            "apt",
            "install",
            "-y",
            package
        ]

        return AutoInstaller._execute(command)

    @staticmethod
    def _install_go(tool_name):

        package = GO_MAPPING[tool_name]

        command = [
            "go",
            "install",
            package
        ]

        return AutoInstaller._execute(command)

    @staticmethod
    def _execute(command):

        try:
            subprocess.run(command, check=True)
            return True

        except Exception as error:
            logger.error(str(error))
            return False
