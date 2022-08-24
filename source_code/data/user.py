from warnings import WarningMessage
from exceptions import UserNotFoundException, SeasonNotAcceptingNewPlayersException
from season import _get_latest_season

from schema import Server, Season, User, SeasonState

def sign_player_up_for_season(server_id: str, user_id: str, display_name: str):
    season: Season = _get_latest_season(server_id=server_id)
    if season.state != SeasonState.OPEN:
        raise SeasonNotAcceptingNewPlayersException()
    if user_id in season.user_map.keys():
        raise WarningMessage("Attempt to add a user to a season they are already in.")
    season.user_map[user_id] = User(user_id, display_name)


def submit_wordle(
    user_id: str,
    server_id: str,
    num_guesses: int,
):
    # TODO: Ima be honest I have no clue how steve did this. Have to speak with him.
    pass