This is based off Wiwiweb's Discord Notifier. 
https://github.com/Wiwiweb/FactorioModDiscordNotifier

The change here is that it will run off my local server via cron.  Instead of amazon lambda.

#### SETUP STEP

1. Change the environment variables to your keys in docker-compose.yml

FACTORIO_DISCORD_CHANNEL: Channel id that the bot will post to. It's an 18-digit number. Right click on a discord channel and "Copy ID" to find it.
FACTORIO_DISCORD_TOKEN: The BOT's "secret" of the discord Application that will post the changelog. See https://discord.com/developers/applications/
FACTORIO_MOD_AUTHOR: Your Factorio Mod Portal name. That's the name the bot will look for to find relevant mods.

2. "{} >> data.json" to add data.json file.
3. Run docker compose up
4. ???
5. Profit