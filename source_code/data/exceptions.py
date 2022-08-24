
class ServerNotFoundException(Exception):
    pass

class UserNotFoundException(Exception):
    pass

class SeasonNotFoundException(Exception):
    pass

class SeasonNotAcceptingNewPlayersException(Exception):
    pass

class PreviousSeasonNotClosedException(Exception):
    pass

class StateNotOpenException(Exception):
    pass