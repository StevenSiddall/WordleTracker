from exceptions import SeasonNotFoundException, PreviousSeasonNotClosedException, StateNotOpenException
from schema import Season, Server
from server import get_server
from source_code.data.schema import SeasonState

def has_season(server: Server) -> bool:
    return len(server.seasons) > 0

def _get_season(server_id: str, season_index: int) -> Season:
    server: Server = get_server(server_id)
    if 0 > season_index > len(server.seasons) - 1:
        raise SeasonNotFoundException()
    return server[season_index]


def _get_latest_season(server: Server) -> Season:
    if not has_season(server):
        raise SeasonNotFoundException()
    return server[-1]


def complete_latest_season(server_id: str) -> bool:
    # Returns true / false to indicate whether 
    # there was a latest season to close
    server: Server = get_server(server_id)
    if not has_season(server):
        return False
    server.state = SeasonState.COMPLETED
    return True
    

def create_new_season(server_id: str):
    server: Server = get_server(server_id)
    if has_season(server):
        # Verify prior season has closed
        latest_season: Season = _get_latest_season(server)
        if latest_season.state != SeasonState.COMPLETED:
            raise PreviousSeasonNotClosedException()
    server.seasons.append(Season(str(len(server.seasons)), state=SeasonState.OPEN))


def start_latest_season(server_id: str, start_wordle_index: int):
    server: Server = get_server(server_id)
    if not has_season(server):
        raise SeasonNotFoundException()
    season: Season = _get_latest_season(server)
    if season.state != SeasonState.OPEN:
        raise StateNotOpenException()
    season.state = SeasonState.RUNNING
    season.start_wordle_index = start_wordle_index