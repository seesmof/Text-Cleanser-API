from rich.console import Console

console = Console()


class Logger:
    @staticmethod
    def show_error(message: str) -> None:
        console.print("[red]" + message + "[/red]")

    @staticmethod
    def show_success(message: str) -> None:
        console.print("[green]" + message + "[/green]")

    @staticmethod
    def show_default(message: str) -> None:
        console.print(message)
