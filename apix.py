import typer
from rich.console import Console

from core.config.prompts import collect_scan_inputs
from core.orchestrator.engine import ReconEngine

app = typer.Typer()
console = Console()

@app.command()
def recon():

    config = collect_scan_inputs()

    engine = ReconEngine(config)

    engine.initialize()

    engine.start()

if __name__ == "__main__":
    app()
