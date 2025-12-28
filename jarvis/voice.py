"""
Voice - Text-to-Speech Output

Supports:
- ElevenLabs (premium, cross-platform)
- macOS native TTS (free, Mac only)
"""

import asyncio
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from rich.console import Console

console = Console()


def clean_for_speech(text: str) -> str:
    """Remove markdown formatting that TTS would read literally."""
    text = re.sub(r'\*+', '', text)
    text = re.sub(r'_+', '', text)
    text = re.sub(r'`+', '', text)
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'  +', ' ', text)
    return text.strip()


class Voice:
    """Multi-backend TTS - ElevenLabs or macOS native."""
    
    def __init__(self, config: dict):
        self.config = config.get('voice_output', {})
        self.engine = self.config.get('engine', 'elevenlabs')
        
        # ElevenLabs settings
        self.voice_id = self.config.get('voice_id', '')
        self.model = self.config.get('model', 'eleven_monolingual_v1')
        self.api_key = self.config.get('api_key') or os.environ.get('ELEVENLABS_API_KEY')
        
        # macOS settings
        self.macos_voice = self.config.get('macos_voice', 'Samantha')
        self.rate = self.config.get('rate', 180)
        
        self.initialized = False
        self._pygame_initialized = False
        self.client = None
        
    async def initialize(self):
        """Initialize TTS engine."""
        # Auto-detect engine if voice_id is set
        if self.voice_id and self.api_key:
            self.engine = 'elevenlabs'
        elif sys.platform == 'darwin' and self.config.get('engine') == 'macos':
            self.engine = 'macos'
        elif self.voice_id and self.api_key:
            self.engine = 'elevenlabs'
        
        if self.engine == 'elevenlabs':
            await self._init_elevenlabs()
        elif self.engine == 'macos':
            await self._init_macos()
        else:
            # Default to ElevenLabs if configured
            if self.api_key and self.voice_id:
                await self._init_elevenlabs()
            elif sys.platform == 'darwin':
                self.engine = 'macos'
                await self._init_macos()
            else:
                console.print("[red]✗[/red] No TTS engine configured")
                console.print("[dim]Add ElevenLabs API key or use macOS native[/dim]")
    
    async def _init_elevenlabs(self):
        """Initialize ElevenLabs."""
        if not self.api_key:
            console.print("[red]✗[/red] ELEVENLABS_API_KEY not set")
            return
        
        try:
            from elevenlabs.client import ElevenLabs
            import pygame
            
            self.client = ElevenLabs(api_key=self.api_key)
            
            pygame.mixer.init()
            self._pygame_initialized = True
            
            self.initialized = True
            self.engine = 'elevenlabs'
            console.print(f"[green]✓[/green] ElevenLabs ready (voice: {self.voice_id})")
            
        except ImportError as e:
            console.print(f"[red]✗[/red] Missing package: {e}")
            console.print("[dim]Run: pip install elevenlabs pygame[/dim]")
        except Exception as e:
            console.print(f"[red]✗[/red] ElevenLabs error: {e}")
    
    async def _init_macos(self):
        """Initialize macOS native TTS."""
        if sys.platform != 'darwin':
            console.print("[red]✗[/red] macOS TTS only available on Mac")
            return
        
        self.initialized = True
        self.engine = 'macos'
        console.print(f"[green]✓[/green] macOS TTS ready (voice: {self.macos_voice})")
    
    async def speak(self, text: str):
        """Generate and play speech."""
        if not text:
            return
            
        console.print(f"[magenta]Yennefer:[/magenta] {text}")
        
        if not self.initialized:
            console.print("[yellow]Voice not initialized[/yellow]")
            return
        
        speech_text = clean_for_speech(text)
        
        if self.engine == 'elevenlabs':
            await self._speak_elevenlabs(speech_text)
        elif self.engine == 'macos':
            await self._speak_macos(speech_text)
    
    async def _speak_elevenlabs(self, text: str):
        """Speak using ElevenLabs."""
        try:
            import pygame
            
            loop = asyncio.get_event_loop()
            audio_generator = await loop.run_in_executor(
                None,
                lambda: self.client.text_to_speech.convert(
                    text=text,
                    voice_id=self.voice_id,
                    model_id=self.model
                )
            )
            
            audio_bytes = b''.join(audio_generator)
            
            with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
                f.write(audio_bytes)
                temp_path = f.name
            
            pygame.mixer.music.load(temp_path)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                await asyncio.sleep(0.1)
            
            pygame.mixer.music.unload()
            Path(temp_path).unlink(missing_ok=True)
            
        except Exception as e:
            console.print(f"[yellow]TTS error: {e}[/yellow]")
    
    async def _speak_macos(self, text: str):
        """Speak using macOS native TTS."""
        try:
            escaped_text = text.replace('"', '\\"')
            cmd = f'say -v {self.macos_voice} -r {self.rate} "{escaped_text}"'
            
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(
                None,
                lambda: subprocess.run(cmd, shell=True, check=True)
            )
            
        except Exception as e:
            console.print(f"[yellow]TTS error: {e}[/yellow]")
    
    def stop(self):
        """Stop current speech."""
        try:
            if self._pygame_initialized:
                import pygame
                pygame.mixer.music.stop()
        except:
            pass
    
    def cleanup(self):
        """Clean up resources."""
        try:
            if self._pygame_initialized:
                import pygame
                pygame.mixer.quit()
        except:
            pass
