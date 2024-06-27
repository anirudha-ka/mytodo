""" This module provides database functionality. """

import configparser
from pathlib import Path

from mytodo import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_todo.json"
)

def get_database_path(config_file: Path) -> Path:
    """ return the current path to the todo database """
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_file["General"]["database"])

def init_database(db_path: Path) -> int:
    """ create the todo database """
    try:
        db_path.write_text("[]") # empty todo list
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR