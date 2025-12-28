#!/usr/bin/env python3
"""
Yennefer - AI Assistant

Usage:
    python -m jarvis.main
"""

import asyncio
from rich.console import Console
from rich.panel import Panel

from .orchestrator import JarvisOrchestrator
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
    console.print(Panel(banner, title="[bold magenta]AI Assistant[/bold magenta]", 
                        subtitle="v0.1.0 - Windows + LM Studio + ElevenLabs", style="magenta"))


async def main():
    """Main entry point."""
    print_banner()
    
    config = load_config()
    console.print("[green]✓[/green] Configuration loaded")
    
    yennefer = JarvisOrchestrator(config)
    await yennefer.run()


def cli():
    """CLI entry point."""
    asyncio.run(main())


if __name__ == "__main__":
    cli()
