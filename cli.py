#!/usr/bin/env python3
"""CLI for Claude Metrics extraction."""

import argparse
import sys
from pathlib import Path
from typing import List, Optional

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

__version__ = "0.1.0"
from metrics_extractor import MetricsExtractor
from sources import ALL_SOURCES


console = Console()


def cmd_extract(args):
    """Extract metrics from Claude Code data."""
    output_dir = Path(args.output_dir)

    # Determine which sources to extract
    sources = args.source if args.source else None

    console.print(f"\n[bold]Claude Metrics Extractor v{__version__}[/bold]\n")

    # Show configuration
    console.print(f"Output directory: [cyan]{output_dir}[/cyan]")
    console.print(f"Include sensitive: [cyan]{args.include_sensitive}[/cyan]")
    console.print(f"Format: [cyan]{args.format}[/cyan]")

    if sources:
        console.print(f"Sources: [cyan]{', '.join(sources)}[/cyan]")
    else:
        console.print(f"Sources: [cyan]all ({len(ALL_SOURCES)})[/cyan]")

    console.print()

    # Create extractor
    extractor = MetricsExtractor(
        output_dir=output_dir,
        include_sensitive=args.include_sensitive,
        sources=sources,
    )

    # Extract with progress
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Extracting...", total=None)

        def on_progress(source_name: str, status: str):
            if status == "extracting":
                progress.update(task, description=f"Extracting [cyan]{source_name}[/cyan]...")
            elif status == "done":
                progress.update(task, description=f"Extracted [green]{source_name}[/green]")
            elif status == "error":
                progress.update(task, description=f"Error: [red]{source_name}[/red]")

        result = extractor.extract_all(progress_callback=on_progress)

    # Write output
    console.print("\n[bold]Writing output...[/bold]")

    if args.format in ("json", "both"):
        json_files = extractor.write_json()
        console.print(f"  JSON files: [green]{len(json_files)} files[/green]")

    if args.format in ("sqlite", "both"):
        db_path = extractor.write_sqlite()
        console.print(f"  SQLite database: [green]{db_path}[/green]")

    # Show summary
    console.print("\n[bold]Extraction Summary[/bold]\n")
    summary = extractor.get_summary()

    table = Table(show_header=True)
    table.add_column("Source", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Key Metrics")

    for source_name, source_summary in summary.get("summaries", {}).items():
        if "error" in source_summary:
            status = "[red]Error[/red]"
            metrics = source_summary["error"]
        else:
            status = "[green]OK[/green]"
            # Get key metrics from summary
            metrics_parts = []
            for key, value in source_summary.items():
                if key != "source" and not key.startswith("_"):
                    if isinstance(value, (int, float)):
                        metrics_parts.append(f"{key}: {value}")
                    elif isinstance(value, list) and len(value) <= 3:
                        metrics_parts.append(f"{key}: {len(value)}")
            metrics = ", ".join(metrics_parts[:3])  # Limit to 3

        table.add_row(source_name, status, metrics or "-")

    console.print(table)

    # Show errors if any
    if result.get("errors"):
        console.print("\n[bold red]Errors:[/bold red]")
        for error in result["errors"]:
            console.print(f"  [red]•[/red] {error['source']}: {error['error']}")

    console.print(f"\n[bold green]Done![/bold green] Output saved to: {output_dir}\n")


def cmd_sources(args):
    """List available data sources."""
    console.print(f"\n[bold]Claude Metrics - Available Sources[/bold]\n")

    table = Table(show_header=True)
    table.add_column("Name", style="cyan")
    table.add_column("Description")
    table.add_column("Paths")

    for source in MetricsExtractor.list_sources():
        paths = "\n".join(source["paths"][:2])
        if len(source["paths"]) > 2:
            paths += f"\n...and {len(source['paths']) - 2} more"

        table.add_row(
            source["name"],
            source["description"],
            paths,
        )

    console.print(table)
    console.print(f"\nTotal: [cyan]{len(ALL_SOURCES)}[/cyan] sources\n")


def cmd_summary(args):
    """Show summary of previously extracted data."""
    output_dir = Path(args.output_dir)
    summary_file = output_dir / "extraction_summary.json"

    if not summary_file.exists():
        console.print(f"[red]Summary file not found:[/red] {summary_file}")
        console.print("Run 'claude-metrics extract' first.")
        sys.exit(1)

    import json
    with open(summary_file) as f:
        summary = json.load(f)

    console.print(f"\n[bold]Extraction Summary[/bold]\n")
    console.print(f"Extracted at: [cyan]{summary.get('extracted_at')}[/cyan]")
    console.print(f"Version: [cyan]{summary.get('version')}[/cyan]")
    console.print(f"Sources: [cyan]{summary.get('source_count')}[/cyan]")

    console.print("\n[bold]Source Details:[/bold]\n")

    for source_name, source_summary in summary.get("summaries", {}).items():
        console.print(f"  [cyan]{source_name}[/cyan]")
        for key, value in source_summary.items():
            if key != "source":
                console.print(f"    {key}: {value}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        prog="claude-metrics",
        description="Extract and analyze Claude Code usage data",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Extract command
    extract_parser = subparsers.add_parser(
        "extract", help="Extract metrics from Claude Code data"
    )
    extract_parser.add_argument(
        "--output-dir", "-o",
        default="./claude_metrics_output",
        help="Output directory (default: ./claude_metrics_output)",
    )
    extract_parser.add_argument(
        "--source", "-s",
        action="append",
        choices=list(ALL_SOURCES.keys()),
        help="Specific source(s) to extract (can repeat, default: all)",
    )
    extract_parser.add_argument(
        "--format", "-f",
        choices=["json", "sqlite", "both"],
        default="both",
        help="Output format (default: both)",
    )
    extract_parser.add_argument(
        "--include-sensitive",
        action="store_true",
        help="Include sensitive data (tokens, keys) - use with caution",
    )
    extract_parser.set_defaults(func=cmd_extract)

    # Sources command
    sources_parser = subparsers.add_parser(
        "sources", help="List available data sources"
    )
    sources_parser.set_defaults(func=cmd_sources)

    # Summary command
    summary_parser = subparsers.add_parser(
        "summary", help="Show summary of extracted data"
    )
    summary_parser.add_argument(
        "output_dir",
        nargs="?",
        default="./claude_metrics_output",
        help="Directory containing extracted data",
    )
    summary_parser.set_defaults(func=cmd_summary)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
