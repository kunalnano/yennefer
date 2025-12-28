"""
Configuration loader for Jarvis.
"""

from pathlib import Path
import yaml


def load_config(config_path: str = None) -> dict:
    """Load configuration from YAML file."""
    if config_path is None:
        config_path = Path(__file__).parent.parent / "config" / "jarvis.yaml"
    
    config_file = Path(config_path)
    
    if not config_file.exists():
        return {}
    
    with open(config_file, 'r') as f:
        return yaml.safe_load(f) or {}
