import discord

from discord.ext import commands

selfbot = commands.Bot(command_prefix="s!", self_bot=True, help_command=None, activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"))

@selfbot.event
async def on_ready():
    print("""
Name - {}
Discriminator - {}
ID - {}
Status - {}
""".format(
self.bot.user.name, self.bot.user.discriminator, self.bot.user.id, self.bot.user.status
)

if __name__ == "__main__":
    try:
        self.bot.run(os.getenv("DISCORD-TOKEN"), bot=False)
    except KeyboardInterrupt:
        print("Bot Closing.")
    except discord.PrivilegedIntentsRequired:
        print("Privileged intents are not explicitly granted in the discord developers dashboard.")
    except discord.LoginFailure:
        print("The token seems to be invalid.")
    except discord.ConnectionClosed:
        print("Connection closed.")
    except discord.HTTPException:
        print("]Could not connect to discord.com")
    except discord.GatewayNotFound:
        print("The API is probably having an outage.")
    except Exception as e:
        raise e
