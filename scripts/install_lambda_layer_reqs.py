"""Scripts for installing the dependencies needed for lambda layers."""
import logging
import os
import shutil
import subprocess
from tkinter.messagebox import NO
from typing import AnyStr, List
from script_utils import get_path_for_directory

logging.getLogger().setLevel(logging.INFO)

def main() -> None:
    """Top level method for installing packages required by lambda layers."""
    src_directory = get_path_for_directory("src")
    layer_directories = get_layer_directories(src_directory + "/Layer")
    
    for layer_dir in layer_directories:
        logging.info("Installing dependencies from  %s", layer_dir)
        create_zip_for_layers(layer_dir=layer_dir)
    
    
def get_layer_directories(top_level_dir: bytes) -> List[AnyStr]:
    """Get a list of all layers in layer."""
    
    logging.info("Putting together list of layer directories.")
    dir_paths = []
    for subdir in os.scandir(top_level_dir):
        dir_paths.append(os.path.abspath(subdir))
    return dir_paths


def create_zip_for_layers(layer_dir: bytes) -> None:
    """Create zip files for layers."""
    filename = str(layer_dir)
    filename = filename.rsplit("/", 1)[-1]
    install_requirements(layer_dir)
    logging.info("Creating zip files for %s", filename)
    # subprocess.run(f"zip --quiet -r9 ../{filename}.zip ./*", shell=False, check=True)
    shutil.make_archive(base_name="requirements", format="zip", root_dir=filename, base_dir='python')
    # logging.info("Deleting raw layer directory: %s", layer_dir)
    # shutil.rmtree(layer_dir)
    
    
def install_requirements(path: bytes) -> None:
    """Installs requirements for layers."""
    
    os.chdir(path + "/python")
    os.system("python -m pip install -r requirements.txt -t .")
    os.remove("requirements.txt")
    remove_unnecessary_folders(path + "/python")
    os.chdir(path)
    
    
def remove_unnecessary_folders(path: bytes) -> None:
    """Removes unnecessary folders with extension .dist-info"""
    
    folders = os.listdir(path)
    for folder in folders:
        if folder.endswith(".dist-info"):
            shutil.rmtree(folder)


if __name__ == "__main__":
    main()