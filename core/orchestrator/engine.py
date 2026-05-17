from rich.console import Console
from rich.table import Table

from core.logging.logger import logger
from core.installer.dependency_checker import check_tools
from core.utils.workspace import initialize_workspace
from core.database.db import DatabaseManager
from core.parser.target_parser import TargetParser
from core.workflow.router import WorkflowRouter
from core.parser.httpx_parser import HTTPXParser

from modules.passive.amass_scan import AmassScanner
from modules.active.httpx_probe import HTTPXProbe
from modules.active.nmap_scan import NmapScanner
from modules.active.swagger_scan import SwaggerScanner
from modules.active.graphql_scan import GraphQLScanner

console = Console()

class ReconEngine:

    def __init__(self, config):

        self.config = config
        self.scan_dir = None
        self.db = None
        self.target_info = None
        self.modules = None

    def initialize(self):

        console.print("\n[bold green]Initializing APIX Engine[/bold green]\n")

        parser = TargetParser(
            self.config["target"]
        )

        self.target_info = parser.normalize()

        self.modules = WorkflowRouter.determine_modules(
            self.target_info
        )

        self.scan_dir = initialize_workspace(
            self.target_info["host"]
        )

        logger.info(f"Workspace created: {self.scan_dir}")

        self.db = DatabaseManager(
            f"{self.scan_dir}/apix.db"
        )

        self.db.initialize()

        self.db.insert_metadata(self.config)

        logger.info("SQLite intelligence database initialized")

        self._display_target_info()

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

    def _display_target_info(self):

        table = Table(title="Target Intelligence")

        table.add_column("Field")
        table.add_column("Value")

        for key, value in self.target_info.items():
            table.add_row(str(key), str(value))

        console.print(table)

    def start(self):

        console.print(
            "\n[bold cyan]Starting reconnaissance workflow...[/bold cyan]\n"
        )

        if self.modules["amass"]:

            logger.info("Starting passive reconnaissance")

            amass = AmassScanner(
                self.target_info["domain"]
            )

            subdomains = amass.run()

            logger.info(f"Amass discovered {len(subdomains)} subdomains")

        logger.info("Starting HTTP probing")

        httpx = HTTPXProbe(
            self.target_info["base_url"]
        )

        httpx_result = httpx.run()

        parsed_httpx = HTTPXParser.parse(
            httpx_result["stdout"]
        )

        logger.info(parsed_httpx)

        if self.modules["nmap"]:

            logger.info("Starting Nmap scanning")

            nmap = NmapScanner(
                self.target_info["host"]
            )

            nmap_result = nmap.run()

            logger.info(nmap_result["stdout"])

        logger.info("Starting Swagger discovery")

        swagger = SwaggerScanner(
            self.target_info["base_url"]
        )

        swagger_results = swagger.run()

        logger.info(swagger_results)

        logger.info("Starting GraphQL discovery")

        graphql = GraphQLScanner(
            self.target_info["base_url"]
        )

        graphql_results = graphql.run()

        logger.info(graphql_results)

        logger.info("Recon workflow initialized.")
