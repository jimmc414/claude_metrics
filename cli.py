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


def cmd_metrics_calculate(args):
    """Calculate derived metrics from Claude Code data."""
    from extraction import TimeFilteredExtractor
    from metrics import DerivedMetricsEngine
    from metrics.definitions import METRIC_DEFINITIONS

    console.print(f"\n[bold]Claude Metrics - Derived Metrics Calculator[/bold]\n")
    console.print(f"Time window: [cyan]{args.days} days[/cyan]")

    categories = list(args.category) if args.category else None
    if categories:
        console.print(f"Categories: [cyan]{', '.join(categories)}[/cyan]")
    else:
        console.print(f"Categories: [cyan]all (A-J)[/cyan]")

    console.print()

    # Extract data with progress
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Extracting data...", total=None)
        extractor = TimeFilteredExtractor(days=args.days)
        data = extractor.extract()
        progress.update(task, description="[green]Data extracted[/green]")

    # Show extraction summary
    console.print(f"Sessions: [cyan]{data.total_sessions}[/cyan]")
    console.print(f"Messages: [cyan]{data.total_messages}[/cyan]")
    console.print(f"Tool calls: [cyan]{data.total_tool_calls}[/cyan]")
    console.print(f"Total cost: [cyan]${data.total_cost_usd:.2f}[/cyan]")
    console.print()

    # Calculate metrics
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Calculating metrics...", total=None)

        def on_progress(metric_id: str, status: str):
            if status == "calculating":
                progress.update(task, description=f"Calculating [cyan]{metric_id}[/cyan]...")
            elif status == "done":
                progress.update(task, description=f"Calculated [green]{metric_id}[/green]")

        engine = DerivedMetricsEngine(data)
        results = engine.calculate_all(categories=categories, progress_callback=on_progress)

    # Show summary
    summary = engine.get_summary()
    console.print(f"\n[bold]Calculation Summary[/bold]\n")
    console.print(f"Metrics calculated: [green]{summary['total_calculated']}[/green]")
    console.print(f"Errors: [{'red' if summary['total_errors'] > 0 else 'green'}]{summary['total_errors']}[/{'red' if summary['total_errors'] > 0 else 'green'}]")

    # Show metrics by category
    console.print("\n[bold]By Category:[/bold]")
    for cat, cat_info in sorted(summary.get("categories", {}).items()):
        console.print(f"  Category {cat}: [cyan]{cat_info['count']} metrics[/cyan]")

    # Output results
    if args.output:
        output_path = Path(args.output)
        engine.to_json(output_path)
        console.print(f"\n[green]Results saved to:[/green] {output_path}")
    else:
        # Show sample metrics
        console.print("\n[bold]Sample Metrics:[/bold]\n")

        table = Table(show_header=True)
        table.add_column("ID", style="cyan")
        table.add_column("Name")
        table.add_column("Value", style="green")
        table.add_column("Unit")

        # Show first 15 metrics
        count = 0
        for metric_id, value in sorted(results.items()):
            if count >= 15:
                break
            definition = METRIC_DEFINITIONS.get(metric_id)
            if definition:
                val_str = str(value.value)
                if isinstance(value.value, float):
                    val_str = f"{value.value:.4f}"
                elif isinstance(value.value, dict):
                    val_str = f"{{...}} ({len(value.value)} items)"
                table.add_row(
                    metric_id,
                    definition.name,
                    val_str[:30],
                    definition.unit or "-",
                )
                count += 1

        console.print(table)
        console.print(f"\n... and {len(results) - 15} more metrics")
        console.print("\nUse [cyan]--output FILE[/cyan] to save all results to JSON")

    # Show errors if any
    errors = engine.get_errors()
    if errors:
        console.print(f"\n[bold red]Errors ({len(errors)}):[/bold red]")
        for err in errors[:5]:
            console.print(f"  [red]•[/red] {err['metric_id']}: {err['error']}")
        if len(errors) > 5:
            console.print(f"  ... and {len(errors) - 5} more errors")


def cmd_metrics_report(args):
    """Generate a metrics report."""
    from extraction import TimeFilteredExtractor
    from metrics import DerivedMetricsEngine

    console.print(f"\n[bold]Claude Metrics - Report Generator[/bold]\n")
    console.print(f"Time window: [cyan]{args.days} days[/cyan]")

    output_format = getattr(args, "format", "terminal")
    if output_format == "html":
        console.print(f"Format: [cyan]HTML[/cyan]")
    else:
        console.print(f"Theme: [cyan]{args.theme}[/cyan]")
    console.print()

    # Extract data with progress
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Extracting data...", total=None)
        extractor = TimeFilteredExtractor(days=args.days)
        data = extractor.extract()
        progress.update(task, description="[green]Data extracted[/green]")

    # Calculate metrics
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Calculating metrics...", total=None)
        engine = DerivedMetricsEngine(data)
        metrics = engine.calculate_all()
        progress.update(task, description=f"[green]{len(metrics)} metrics calculated[/green]")

    console.print()

    # Generate report based on format
    if output_format == "html":
        from visualizations.html import DashboardGenerator

        output_path = Path(args.output) if args.output else Path("claude_metrics_report.html")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Generating HTML dashboard...", total=None)
            generator = DashboardGenerator(data, metrics)
            generator.generate(output_path)
            progress.update(task, description="[green]Dashboard generated[/green]")

        console.print(f"\n[green]HTML report saved to:[/green] {output_path}")
        console.print(f"Open in a browser to view the interactive dashboard.")

    else:
        from visualizations.terminal import TerminalReport, get_theme

        theme = get_theme(args.theme)
        report = TerminalReport(data, metrics, theme=theme, console=console)

        if args.detail:
            report.print_all_metrics()
        else:
            report.print_full_report()


def cmd_metrics_list(args):
    """List available derived metrics."""
    from metrics.definitions import METRIC_DEFINITIONS, get_metrics_by_category

    console.print(f"\n[bold]Claude Metrics - Available Derived Metrics[/bold]\n")

    if args.category:
        categories = [args.category.upper()]
    else:
        categories = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    for category in categories:
        metrics = get_metrics_by_category(category)
        if not metrics:
            continue

        console.print(f"\n[bold]Category {category}[/bold] ({len(metrics)} metrics)")

        table = Table(show_header=True)
        table.add_column("ID", style="cyan", width=6)
        table.add_column("Name", width=30)
        table.add_column("Type", width=12)
        table.add_column("Description")

        for m in sorted(metrics, key=lambda x: x.id):
            table.add_row(
                m.id,
                m.name,
                m.metric_type.value,
                m.description[:50] + ("..." if len(m.description) > 50 else ""),
            )

        console.print(table)

    total = len(METRIC_DEFINITIONS)
    console.print(f"\n[bold]Total:[/bold] [cyan]{total}[/cyan] derived metrics defined")


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

    # Metrics command group
    metrics_parser = subparsers.add_parser(
        "metrics", help="Derived metrics commands"
    )
    metrics_subparsers = metrics_parser.add_subparsers(dest="metrics_command")

    # Metrics calculate command
    metrics_calc_parser = metrics_subparsers.add_parser(
        "calculate", help="Calculate derived metrics"
    )
    metrics_calc_parser.add_argument(
        "--days", "-d",
        type=int,
        default=30,
        help="Time window in days (default: 30)",
    )
    metrics_calc_parser.add_argument(
        "--category", "-c",
        action="append",
        choices=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        help="Categories to calculate (can repeat, default: all)",
    )
    metrics_calc_parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output JSON file path",
    )
    metrics_calc_parser.set_defaults(func=cmd_metrics_calculate)

    # Metrics list command
    metrics_list_parser = metrics_subparsers.add_parser(
        "list", help="List available derived metrics"
    )
    metrics_list_parser.add_argument(
        "--category", "-c",
        choices=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        help="Filter by category",
    )
    metrics_list_parser.set_defaults(func=cmd_metrics_list)

    # Metrics report command
    metrics_report_parser = metrics_subparsers.add_parser(
        "report", help="Generate a visual metrics report"
    )
    metrics_report_parser.add_argument(
        "--days", "-d",
        type=int,
        default=30,
        help="Time window in days (default: 30)",
    )
    metrics_report_parser.add_argument(
        "--format", "-f",
        choices=["terminal", "html"],
        default="terminal",
        help="Output format (default: terminal)",
    )
    metrics_report_parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output file path (for HTML format)",
    )
    metrics_report_parser.add_argument(
        "--theme", "-t",
        choices=["default", "mono", "dark"],
        default="default",
        help="Color theme for terminal output (default: default)",
    )
    metrics_report_parser.add_argument(
        "--detail",
        action="store_true",
        help="Show detailed metrics by category (terminal only)",
    )
    metrics_report_parser.set_defaults(func=cmd_metrics_report)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    # Handle metrics subcommand
    if args.command == "metrics":
        if not hasattr(args, "metrics_command") or args.metrics_command is None:
            metrics_parser.print_help()
            sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
