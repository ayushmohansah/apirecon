from rich.prompt import Prompt, Confirm, IntPrompt
from rich.console import Console

console = Console()

def collect_scan_inputs():

    console.print("\n[bold cyan]APIX Recon Configuration[/bold cyan]\n")

    target = Prompt.ask(
        "[yellow]Target Domain/IP[/yellow]"
    )

    aggressive = Confirm.ask(
        "[yellow]Enable aggressive mode?[/yellow]",
        default=True
    )

    if aggressive:
        console.print(
            "[red]Aggressive mode enables deeper fuzzing, higher concurrency, and recursive endpoint discovery.[/red]"
        )

    threads = IntPrompt.ask(
        "[yellow]Concurrency Threads[/yellow]",
        default=25
    )

    timeout = IntPrompt.ask(
        "[yellow]HTTP Timeout (seconds)[/yellow]",
        default=10
    )

    use_proxy = Confirm.ask(
        "[yellow]Use proxy?[/yellow]",
        default=False
    )

    proxy = None

    if use_proxy:
        proxy = Prompt.ask(
            "[yellow]Proxy URL[/yellow]"
        )

    return {
        "target": target,
        "aggressive": aggressive,
        "threads": threads,
        "timeout": timeout,
        "proxy": proxy
    }
