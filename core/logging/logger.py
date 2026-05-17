from rich.console import Console
from rich.logging import RichHandler
import logging
import os

console = Console()

LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "runtime.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        RichHandler(console=console),
        logging.FileHandler(LOG_FILE)
    ]
)

logger = logging.getLogger("APIX")
