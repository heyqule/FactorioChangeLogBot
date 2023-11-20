This is based off Wiwiweb's Discord Notifier. 
https://github.com/Wiwiweb/FactorioModDiscordNotifier

The change here is that it will run off my local server via cron.  Instead of amazon lambda.

#### SETUP STEP

1. Copy activate-env-example.sh to activate-env.sh
2. Change the environment variables to your keys

FACTORIO_DISCORD_CHANNEL: Channel id that the bot will post to. It's an 18-digit number. Right click on a discord channel and "Copy ID" to find it.
FACTORIO_DISCORD_TOKEN: The BOT's "secret" of the discord Application that will post the changelog. See https://discord.com/developers/applications/
FACTORIO_MOD_AUTHOR: Your Factorio Mod Portal name. That's the name the bot will look for to find relevant mods.


3. Add this to crontab
```
* * * * * * python /path/to/your/main.py
```

4. Run it on demand
```
python /path/to/your/main.py
```