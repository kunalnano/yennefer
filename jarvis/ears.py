"""
Ears - Text Input Module
"""

import asyncio
from rich.console import Console
from rich.prompt import Prompt

console = Console()


class Ears:
    """Text input handler."""
    
    def __init__(self, config: dict):
        self.config = config.get('voice_input', {})
        
    async def initialize(self):
        """Initialize input handler."""
        console.print("[green]✓[/green] Text input ready")
    
    async def listen(self) -> str:
        """Get text input from user."""
        loop = asyncio.get_event_loop()
        text = await loop.run_in_executor(
            None,
            lambda: Prompt.ask("[cyan]You[/cyan]")
        )
        return text.strip()
    
    def cleanup(self):
        """Nothing to clean up."""
        pass
