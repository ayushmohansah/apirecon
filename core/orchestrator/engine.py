from rich.console import Console
from core.logging.logger import logger
from core.installer.dependency_checker import check_tools
from core.utils.workspace import initialize_workspace
from core.database.db import DatabaseManager
from modules.passive.amass_scan import AmassScanner
from modules.active.httpx_probe import HTTPXProbe
from modules.active.nmap_scan import NmapScanner

console = Console()

class ReconEngine:

    def __init__(self, config):

        self.config = config
        self.scan_dir = None
        self.db = None

    def initialize(self):

        console.print("\n[bold green]Initializing APIX Engine[/bold green]\n")

        self.scan_dir = initialize_workspace(
            self.config["target"]
        )

        logger.info(f"Workspace created: {self.scan_dir}")

        self.db = DatabaseManager(
            f"{self.scan_dir}/apix.db"
        )

        self.db.initialize()

        self.db.insert_metadata(self.config)

        logger.info("SQLite intelligence database initialized")

        missing = check_tools()

        if missing:

            console.print("\n[bold red]Missing Tools Detected:[/bold red]")

            for tool in missing:
                console.print(f" - {tool}")

            console.print(
                "\n[yellow]Automatic installer not implemented yet.[/yellow]"
            )

        else:
            console.print(
                "\n[bold green]All dependencies satisfied.[/bold green]"
            )

    def start(self):

        console.print(
            "\n[bold cyan]Starting reconnaissance workflow...[/bold cyan]\n"
        )

        logger.info("Starting passive reconnaissance")

        amass = AmassScanner(self.config["target"])

        subdomains = amass.run()

        logger.info(f"Amass discovered {len(subdomains)} subdomains")

        logger.info("Starting HTTP probing")

        httpx = HTTPXProbe(self.config["target"])

        httpx_result = httpx.run()

        logger.info(httpx_result["stdout"])

        logger.info("Starting Nmap scanning")

        nmap = NmapScanner(self.config["target"])

        nmap_result = nmap.run()

        logger.info(nmap_result["stdout"])

        logger.info("Recon workflow initialized.")
