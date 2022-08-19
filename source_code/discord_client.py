from discord import Client
from constants import DISCORD_AUTH_TOKEN


# Load Discord client, run discord client
client: Client = Client()
__client_initialized: bool = False

if not __client_initialized:
    # NOTE: This code is only ever run once to intialize the client
    print("+++ Initializing discord client. This may take a minute.")
    client.run(DISCORD_AUTH_TOKEN)
    __client_initialized = True

