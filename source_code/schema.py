from dataclasses import dataclass, field
from re import A
from typing import List
import json

SERVER_FILE_NAME: str = "servers.json"

__info: dict = {}
__info_initialized: bool = False


def _load_json_file(name: str) -> dict:
    with open(name, "R") as f:
        d: dict = json.loads(f.read())
    return d

if not __info_initialized:
    # Load the actual data from JSON
    # TODO: Make JSON files if they don't exist
    print("+++ Loading information from json files")
    servers: dict = _load_json_file(SERVER_FILE_NAME)
    __info_initialized = True

def get_user(server: str, user_id: str) -> User:
    # TODO: Messy shit to actually get user

def add_user(server: str, user_id: str) -> bool:
    return False