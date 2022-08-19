from dataclasses import dataclass, field
import os
from typing import List, Dict
import pickle

__STORAGE_FILE: str = "data.pkl"

@dataclass
class Season:
    num_attempts_history: List[int] = field(default_factory=list)
    total_guesses: int = field(default=0)
    submissions: int = field(default=0)

@dataclass
class User:
    display_name: str = field(default="ERROR")
    id: str = field(default=None)
    seasons: List[Season] = field(default_factory=list)

@dataclass
class Server:
    user_dict: Dict[str, User] = field(default_factory=dict)
    id: str = field(default=None)

@dataclass
class Data:
    servers: Dict[str, Server] = field(default_factory=dict)


__data: Data = None

def sync_data():
    with open(__STORAGE_FILE, "wb") as f:
        pickle.dump(__data, f)

def get_server(id: str) -> Server:
    if id not in __data.servers.keys():
        return None
    return __data.servers[id]

def add_server(id: str):
    if id in __data.servers.keys():
        raise Exception("Attempt to add a server with an id that already exists. You fucked up.")
    # Id in the map should always match the one in the server
    __data.servers[id] = Server(id=id)

__initialized: bool = False
if not __initialized:
    # Load the actual data from JSON
    print("+++ Loading information from json files")
    if not os.path.exists(__STORAGE_FILE):
        # First time doing this, create empty data and sync to file
        __data = Data()
        sync_data()
    else:
        # Read in binary, pickled objects stored as binary files
        with open(__STORAGE_FILE, "rb") as f:
            __data = pickle.load(f)
    __initialized = True