
import os
import yaml
from src.simple_mlops import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path
from box.exceptions import BoxValueError

from src.simple_mlops import logger

from pathlib import Path
import yaml
from box import ConfigBox
from src.simple_mlops import logger


def read_yaml(path_to_yaml) -> ConfigBox:
    try:
        path_to_yaml = Path(path_to_yaml)

        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)

        if content is None:
            content = {}

        logger.info(f"Successfully read YAML file: {path_to_yaml}")
        return ConfigBox(content)

    except FileNotFoundError:
        raise FileNotFoundError(f"YAML file not found: {path_to_yaml}")

    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML file: {path_to_yaml}. Error: {e}")

    except Exception as e:
        raise Exception(f"Error reading YAML file {path_to_yaml}: {e}")
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories if they do not exist.

    Args:
        path_to_directories (list): A list of directory paths to create.
    """
    for directory in path_to_directories:
        try:
            os.makedirs(directory, exist_ok=True)
            logger.info(f"Directory created or already exists: {directory}")
        except Exception as e:
            raise ValueError(f"An error occurred while creating directory {directory}: {e}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary as a JSON file.

    Args:
        path (Path): The path to the JSON file.
        data (dict): The dictionary to save.
    """
    try:
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f"Successfully saved JSON file: {path}")
    except Exception as e:
        raise ValueError(f"An error occurred while saving JSON file: {e}")
    
@ensure_annotations
def load_json(path: Path) -> dict:
    """
    Loads a JSON file and returns its contents as a dictionary.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        dict: The contents of the JSON file as a dictionary.
    """
    try:
        with open(path, "r") as json_file:
            data = json.load(json_file)
            logger.info(f"Successfully loaded JSON file: {path}")
        return data
    except Exception as e:
        raise ValueError(f"An error occurred while loading JSON file: {e}")
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data as a binary file using joblib.

    Args:
        data (Any): The data to save.
        path (Path): The path to the binary file.
    """
    try:
        joblib.dump(data, path)
        logger.info(f"Successfully saved binary file: {path}")
    except Exception as e:
        raise ValueError(f"An error occurred while saving binary file: {e}")    
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads a binary file using joblib and returns its contents.

    Args:
        path (Path): The path to the binary file.

    Returns:
        Any: The contents of the binary file.
    """
    try:
        data = joblib.load(path)
        logger.info(f"Successfully loaded binary file: {path}")
        return data
    except Exception as e:
        raise ValueError(f"An error occurred while loading binary file: {e}")    