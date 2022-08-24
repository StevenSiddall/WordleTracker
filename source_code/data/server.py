from exceptions import ServerNotFoundException
from schema import _data, Server, User

def server_exists(server_id: str) -> bool:
    return server_id in _data.servers.keys()

def user_exists_in_server(user_id: str, server_id: str) -> bool:
    return server_exists(server_id) and user_id in _get_server(server_id).user_dict.keys()


def verify_server_exists(server_id: str):
    if not server_exists(server_id):
        raise ServerNotFoundException()


def _get_server(id: str) -> Server:
    if id not in _data.servers.keys():
        raise ServerNotFoundException()
    return _data.servers[id]


def add_server(server_id: str):
    verify_server_exists(server_id)
    # Id in the map should always match the one in the server
    _data.servers[id] = Server(id=server_id)
