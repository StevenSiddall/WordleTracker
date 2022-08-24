from dataclasses import dataclass, field
import os
from typing import List, Dict
from enum import Enum
import pickle

__STORAGE_FILE: str = "data.pkl"


@dataclass
class User:
    id: str = field(default=None)
    display_name: str = field(default="ERROR")

    # Number of attempts for each wordle
    num_attempts_history: List[int] = field(default_factory=list)
    # The total number of guesses, why we aren't tracking this with the length of 
    total_guesses: int = field(default=0)
    submissions: int = field(default=0)


class SeasonState(Enum):
    OPEN = 0        # Accepting new players, not running
    RUNNING = 1     # Now running, no new players
    COMPLETED = 2   # Done running

@dataclass
class Season:
    id: str = field(default=None)
    user_map: Dict[str, User] = field(default_factory=dict)
    start_wordle_index: int = field(default=-1)

    state: SeasonState = field(default_factory=SeasonState.OPEN)

@dataclass
class Server:
    seasons: List[Season] = field(default_factory=list)
    id: str = field(default=None)

@dataclass
class Data:
    servers: Dict[str, Server] = field(default_factory=dict)

def sync_data():
    with open(__STORAGE_FILE, "wb") as f:
        pickle.dump(_data, f)

_data: Data = None
def initialize():
    # Load the actual data from JSON
    print("+++ Loading long term storage")
    if not os.path.exists(__STORAGE_FILE):
        # First time doing this, create empty data and sync to file
        _data = Data()
        sync_data()
    else:
        # Read in binary, pickled objects stored as binary files
        with open(__STORAGE_FILE, "rb") as f:
            _data = pickle.load(f)