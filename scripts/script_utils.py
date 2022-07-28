"""Contains helper methods that the scripts will utilize to successfully build, test and deploy
CDK application."""
import logging
import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent

def get_path_for_directory(input_dir: str) -> bytes:
    """Get CDK directory path for script."""
    
    for path, dirs, _ in os.walk(ROOT_DIR):
        for source_dir in dirs:
            if 'cache' not in path and source_dir == input_dir:
                return os.path.join(path, source_dir)
    logging.info("Could not find path to '%s' directory.", input_dir)
    return b''