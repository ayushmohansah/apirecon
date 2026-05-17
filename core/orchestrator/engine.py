from rich.console import Console
from core.logging.logger import logger
from core.installer.dependency_checker import check_tools
from core.utils.workspace import initialize_workspace

console = Console()

class ReconEngine:

    def __init__(self, config):

        self.config = config
        self.scan_dir = None

    def initialize(self):

        console.print("\n[bold green]Initializing APIX Engine[/bold green]\n")

        self.scan_dir = initialize_workspace(
            self.config["target"]
        )

        logger.info(f"Workspace created: {self.scan_dir}")

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

        logger.info("Recon workflow initialized.")
