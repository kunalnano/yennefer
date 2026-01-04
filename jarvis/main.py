#!/usr/bin/env python3
"""
Yennefer - AI Assistant

Usage:
    python -m jarvis.main
"""

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # Must be before pygame import

import asyncio
from rich.console import Console
from rich.panel import Panel

from .orchestrator import YenneferOrchestrator
from .config import load_config

console = Console()


def print_banner():
    """Display Yennefer startup banner."""
    banner = """
██╗   ██╗███████╗███╗   ██╗███╗   ██╗███████╗███████╗███████╗██████╗ 
╚██╗ ██╔╝██╔════╝████╗  ██║████╗  ██║██╔════╝██╔════╝██╔════╝██╔══██╗
 ╚████╔╝ █████╗  ██╔██╗ ██║██╔██╗ ██║█████╗  █████╗  █████╗  ██████╔╝
  ╚██╔╝  ██╔══╝  ██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══██╗
   ██║   ███████╗██║ ╚████║██║ ╚████║███████╗██║     ███████╗██║  ██║
   ╚═╝   ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
    """
    console.print(Panel(banner, title="[bold magenta]Yennefer AI[/bold magenta]", 
                        subtitle="v0.3.2", style="magenta"))


async def main():
    """Main entry point."""
    print_banner()
    
    config = load_config()
    console.print("[green]✓[/green] Configuration loaded")
    
    yennefer = YenneferOrchestrator(config)
    await yennefer.run()


def cli():
    """CLI entry point."""
    asyncio.run(main())


if __name__ == "__main__":
    cli()
