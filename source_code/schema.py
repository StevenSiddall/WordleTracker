from dataclasses import dataclass, field
import os
from typing import List, Dict
import pickle
from copy import deepcopy

__STORAGE_FILE: str = "data.pkl"

class ServerNotFoundException(Exception):
    pass

class UserNotFoundException(Exception):
    pass

class SeasonNotFoundException(Exception):
    pass

@dataclass
class Season:
    num_attempts_history: List[int] = field(default_factory=list)
    total_guesses: int = field(default=0)
    submissions: int = field(default=0)

@dataclass
class User:
    display_name: str = field(default="ERROR")
    id: str = field(default=None)
    # NOTE: Active season is always the last season in the list
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


#################################################
#                   GETTERS
#################################################

def __get_server(id: str) -> Server:
    if id not in __data.servers.keys():
        raise ServerNotFoundException()
    return __data.servers[id]


def __get_user_from_server(user_id: str, server_id: str) -> User:
    # Gets the provided user from the server.
    # Verify that the user id is in the server
    server: Server = __get_server(server_id)
    if user_id not in server.user_dict.keys():
        raise UserNotFoundException()
    return server.user_dict[user_id]


def __get_active_season(user_id: str, server_id: str) -> Season:
    # Gets the active season for the user in the server with the
    # provided server id.
    user: User = __get_user_from_server(user_id, server_id)
    if user is None or len(user.seasons) == 0:
        raise SeasonNotFoundException()
    return user.seasons[-1]


def server_exists(server_id: str) -> bool:
    return server_id in __data.servers.keys()

def user_exists_in_server(user_id: str, server_id: str) -> bool:
    return server_exists(server_id) and user_id in __get_server(server_id).user_dict.keys()


#################################################
#                   SETTERS
#################################################

def verify_server_exists(server_id: str):
    if not server_exists(server_id):
        raise ServerNotFoundException()


def verify_user_exists_in_server(user_id: str, server_id: str):
    verify_server_exists(server_id)
    if user_id not in __get_server(server_id).user_dict.keys():
        raise UserNotFoundException()


def add_server(server_id: str):
    verify_server_exists(server_id)
    # Id in the map should always match the one in the server
    __data.servers[id] = Server(id=server_id)


def add_user_to_server(server_id: str, user_id: str, display_name: str):
    verify_server_exists(server_id)
    if user_exists_in_server(user_id, server_id):
        raise Exception("User already exists in server.")
    server: Server = __get_server(server_id)
    server.user_dict[user_id] = User(
        display_name=display_name,
        id = user_id
    )


def start_new_season(server_id: str):
    verify_server_exists(server_id)
    server: Server = __get_server(server_id)
    for user_id in server.user_dict.keys():
        user: User = __get_user_from_server(user_id, server_id)
        user.seasons.append(Season())


def submit_wordle(
    user_id: str,
    server_id: str,
    num_guesses: int,
):
    verify_user_exists_in_server(user_id, server_id)
    season: Season = __get_active_season(user_id, server_id)
    # TODO: Not sure how Steve actually stored this shit.
    # have to talk with him to figure out how to do this.