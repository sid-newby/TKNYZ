#!/usr/bin/env python3

# ASCII Art goes here
LOGO = """
console.print(LOGO, style="red")

░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░    ░▒▓██▓▒░
   ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓██▓▒░
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓██▓▒░
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓████████▓▒░

          ⢀⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠻⣿
          ⠈⠙⠻⣿⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠟⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⣿
          ⠐⣾⠛⡷⢧⡝⠛⠿⣿⡿⠻⠿⠛⠙⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠉⠀⠀⠀⠀⠀⢠⣶⣿
          ⠀⠀⠀⠀⠛⠶⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿
          ⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣮⣿⣿⣿⣿⣿
          ⠀⢀⣠⣤⡤⣤⠀⠀⠀⠀⣠⣤⣤⣄⠀⠲⣆⠀⠀⠀⠀⠀⣠⣴⣦⡀⠀⠀⠀⠀⠀⣘⠀⠀⣶⣿⣿⣿⣿⣿
          ⠀⣾⣿⣿⡿⠋⠀⠀⠀⣾𝖉👁️𝖒⠀⠟⠀⠀⠀⢀⣼𝖉👁️𝖒⡆⠀⠀⠀⠀⠁⠀⠀⣽⣿⣿⣿⣿⣿⣿⣿
          ⠀⢻⣿⠋⠀⠀⠀⠀⠀⠻⢿⣿⣿⠿⠟⠀⠀⠀⠀⠀⠀⠻⠿⠿⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠛⣿⣿⣿⣿⣿
          ⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⡤⣶⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿
          ⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣴⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣶⣿⣿⣿⣶⣤⣄⣀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣻⣿⣿⣋⠙⢻⣿⣿⣿⡿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡋⢹⣆⣸⣿⡟⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡌⢉⣿⢿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""

import pandas as pd
import tiktoken
import typer
import questionary
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich import print as rprint
from pathlib import Path
from typing import Optional
import os

# Initialize Rich console and Typer app
console = Console()
app = typer.Typer()

console.print(LOGO, style="red")

# Define the tokenizer
tokenizer = tiktoken.get_encoding("cl100k_base")

# Define the fuckin rad cool dude art
def interactive_mode():
    """Run the token counter in interactive mode."""
    console.print(LOGO, style="red")  # Add this line
    while True:
        interactive_mode()

def count_tokens(text) -> int:
    """Count tokens in a given text."""
    if pd.isna(text):
        return 0
    return len(tokenizer.encode(str(text)))

def process_csv(file_path: Path) -> None:
    """Process a CSV file and display token counts in a table format."""
    try:
        df = pd.read_csv(file_path)

        # Create tables for each row
        for row_idx in track(range(len(df)), description="Processing rows...", style="red"):
            table = Table(title=f"Row {row_idx + 1}", style="red")

            # Add columns
            table.add_column("Column", style="red")
            table.add_column("Original Content", style="red")
            table.add_column("Token Count", style="yellow")

            # Add row data
            for col in df.columns:
                content = str(df.iloc[row_idx][col])
                token_count = count_tokens(content)
                table.add_row(col, content[:50] + "..." if len(content) > 50 else content, str(token_count))

            console.print(table)
            console.print()

    except Exception as e:
        console.print(f"[red]Error processing CSV file: {str(e)}[/red]")

def process_text(file_path: Path) -> None:
    """Process a text file and display total token count."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        token_count = count_tokens(content)

        # Create a simple table for the results
        table = Table(title="Document Token Count", style="red")
        table.add_column("File", style="red")
        table.add_column("Total Tokens", style="yellow")
        table.add_row(file_path.name, str(token_count))

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error processing text file: {str(e)}[/red]")

def interactive_mode():
    """Run the token counter in interactive mode."""
    while True:
        # Main menu
        action = questionary.select(
            "What would you like to do?",
            choices=[
                "Count tokens in a file",
                "Count tokens in text input",
                "Exit"
            ],
            style=questionary.Style([
                ('question', 'fg:cyan bold'),
                ('selected', 'fg:green'),
                ('pointer', 'fg:magenta bold'),
            ])
        ).ask()

        if action == "Exit":
            console.print("[yellow]Goodbye![/yellow]")
            break

        if action == "Count tokens in a file":
            # File type selection
            file_type = questionary.select(
                "What type of file would you like to process?",
                choices=["CSV", "Text", "Auto-detect"],
            ).ask()

            # File selection
            file_path = questionary.path(
                "Enter the path to your file:"
            ).ask()

            if not file_path:
                continue

            path = Path(file_path)
            if not path.exists():
                console.print(f"[red]Error: File '{file_path}' not found[/red]")
                continue

            # Process based on selection
            if file_type == "Auto-detect":
                is_csv = path.suffix.lower() == ".csv"
            else:
                is_csv = file_type == "CSV"

            console.print(f"[yellow]Processing file: {path.name}[/yellow]")

            if is_csv:
                process_csv(path)
            else:
                process_text(path)

        elif action == "Count tokens in text input":
            # Get multiline input
            console.print("[cyan]Enter your text (press Ctrl+D or Ctrl+Z when finished):[/cyan]")
            lines = []
            try:
                while True:
                    line = input()
                    lines.append(line)
            except EOFError:
                text = "\n".join(lines)
                token_count = count_tokens(text)

                # Display results
                table = Table(title="Text Input Token Count", style="red")
                table.add_column("Text Preview", style="red")
                table.add_column("Total Tokens", style="yellow")
                preview = text[:50] + "..." if len(text) > 50 else text
                table.add_row(preview, str(token_count))
                console.print(table)

        # Ask if user wants to continue
        if not questionary.confirm("Would you like to process another file/text?").ask():
            console.print("[yellow]Goodbye![/yellow]")
            break

@app.command()
def main(
    interactive: bool = typer.Option(True, "--no-interactive", "-n", help="Run in non-interactive mode"),
    file_path: Optional[str] = typer.Argument(None, help="Path to the file to analyze"),
    file_type: Optional[str] = typer.Option(None, "--type", "-t", help="Force file type (csv or text)")
):
    """Token counter CLI - Analyze token counts in files or text input."""
    if interactive and not file_path:
        interactive_mode()
        return

    if not file_path:
        console.print("[red]Error: Please provide a file path in non-interactive mode[/red]")
        raise typer.Exit(1)

    path = Path(file_path)
    if not path.exists():
        console.print(f"[red]Error: File '{file_path}' not found[/red]")
        raise typer.Exit(1)

    # Determine file type
    if file_type:
        is_csv = file_type.lower() == "csv"
    else:
        is_csv = path.suffix.lower() == ".csv"

    console.print(f"[yellow]Processing file: {path.name}[/yellow]")

    if is_csv:
        process_csv(path)
    else:
        process_text(path)

if __name__ == "__main__":
    app()